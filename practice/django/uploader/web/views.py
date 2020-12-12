from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
from .forms import UploadFileForm
from .models import FilePath
import uuid
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def paginate_query(request, queryset, count):
    paginator = Paginator(queryset, count)
    page = request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginatot.page(paginator.num_pages)
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
        queryset = FilePath.objects.order_by("-created_at")
        page_obj = paginate_query(request, queryset, settings.PAGE_PER_ITEM)
        context = {
            'form': form,
            'page_obj': page_obj,
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
