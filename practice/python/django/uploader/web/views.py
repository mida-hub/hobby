from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.conf import settings
from .forms import UploadFileForm
from .models import FilePath
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import RootDocument
from .models import SchemaDocument
import uuid
import datetime
from django.shortcuts import get_object_or_404
from django.http import FileResponse


def download(request, pk, doc):
    if doc == 'root':
        doc_model = RootDocument
    elif doc == 'schema':
        doc_model = SchemaDocument

    upload_file = get_object_or_404(doc_model, pk=pk)
    download_file = upload_file.upload
    return FileResponse(download_file)


def paginate_query(request, queryset, count):
    paginator = Paginator(queryset, count)
    page = request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return page_obj


def file_upload(request):
    if request.method == 'POST':
        try:
            form = UploadFileForm(request.POST, request.FILES)
            if not form.is_valid():
                raise Exception('Validation Error')
            file_obj = request.FILES['file']
            handle_uploaded_file(file_obj)
            messages.success(request, "アップロードが成功しました。")
        except Exception as e:
            messages.error(request, "アップロードが失敗しました。")
            print(e)
        
        return HttpResponseRedirect('/web')

    else:
        form = UploadFileForm()
        queryset = FilePath.objects.order_by("-id")
        page_obj = paginate_query(request, queryset, settings.PAGE_PER_ITEM)
        context = {
            'form': form,
            'page_obj': page_obj,
            'path': request.path
        }
    return render(request, 'file_upload.html', context)


def handle_uploaded_file(file_obj):
    title = file_obj.name

    if '.' in title:
        file_id = '.'.join(title.split('.')[:-1]) + '_' + str(uuid.uuid4()) + '.' + title.split('.')[-1]
    else:
        file_id = title + '_' + str(uuid.uuid4())

    fp = FilePath(file_id=file_id, title=title)
    path = 'media/' + file_id
    with open(path, 'wb+') as destination:
        for chunk in file_obj.chunks():
            destination.write(chunk)
    
    fp.save()


class S3UploadCreateView(CreateView):
    def post(self, request, *args, **kwargs):
        file_obj = request.FILES.get('upload')
        if file_obj is not None:
            file_name_org = file_obj.name
            file_name = file_obj.name
            dt_now = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            if '.' in file_name:
                file_name = '.'.join(file_name.split('.')[:-1]) + '_' + dt_now + '.' + file_name.split('.')[-1]
            else:
                file_name += '_' + dt_now

            file_obj.name = file_name
            request.FILES['upload'] = file_obj

        # super().post(request, *args, **kwargs) を参考に override
        self.object = None
        form = self.get_form()
        if not form.is_valid():
            messages.error(request, "アップロードが失敗しました。データが不正です。")
            return self.form_invalid(form)
        try:
            self.object = form.save(commit=False)
            self.object.file_name = file_name_org
            self.object.save()
            messages.success(request, "アップロードが成功しました。")
        except Exception as e:
            print(e)
            messages.error(request, "アップロードが失敗しました。S3へアクセスできません。")
            return self.form_invalid(form)

        return self.form_valid(form)


class RootDocumentCreateView(S3UploadCreateView):
    model = RootDocument
    fields = ['upload',]
    success_url = reverse_lazy('s3_root') # urls.py の name を指定する
    template_name = "web/document.html" 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        documents = RootDocument.objects.order_by("-id")
        page_obj = paginate_query(self.request, documents, settings.PAGE_PER_ITEM)
        context['page_obj'] = page_obj
        context['path'] = self.request.path
        context['doc'] = 'root'

        return context


class SchemaDocumentCreateView(S3UploadCreateView):
    model = SchemaDocument
    fields = ['upload',]
    success_url = reverse_lazy('s3_schema') # urls.py の name を指定する
    template_name = "web/document.html" 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        documents = SchemaDocument.objects.order_by("-id")
        page_obj = paginate_query(self.request, documents, settings.PAGE_PER_ITEM)
        context['page_obj'] = page_obj
        context['path'] = self.request.path
        context['doc'] = 'schema'

        return context
