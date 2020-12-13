from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.conf import settings
from .forms import UploadFileForm
from .models import FilePath
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Document
import uuid
import datetime


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


class DocumentCreateView(CreateView):
    model = Document
    fields = ['upload', ]
    success_url = reverse_lazy('s3') # urls.py の name を指定する
    template_name = "web/document.html" 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        documents = Document.objects.order_by("-id")
        page_obj = paginate_query(self.request, documents, settings.PAGE_PER_ITEM)
        context['page_obj'] = page_obj
        context['path'] = self.request.path

        return context

    def post(self, request, *args, **kwargs):
        file_obj = request.FILES.get('upload')
        if file_obj is not None:
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
        try:
            if form.is_valid():
                self.object = form.save()
                messages.success(request, "アップロードが成功しました。")
                return super().form_valid(form)
        except Exception as e:
            print(e)
        messages.error(request, "アップロードが失敗しました。")
        return self.form_invalid(form)
