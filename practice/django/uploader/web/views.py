from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from django.http import HttpResponse
from django.contrib import messages
from .models import FilePath
import uuid

def file_upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            title = request.POST.get('title')
            handle_uploaded_file(title, request.FILES['file'])
            file_obj = request.FILES['file']

            messages.success(request, "アップロードが成功しました。")
        else:
            messages.error(request, "アップロードが失敗しました。")

        return HttpResponseRedirect('/web')

    else:
        form = UploadFileForm()
        queryset = FilePath.objects.all()
        context = {
            'form': form,
            'file_path_list': queryset,
        }
    return render(request, 'file_upload.html', context)

def handle_uploaded_file(title, file_obj):
    title = title if title is not None else file_obj.name
    file_id = str(uuid.uuid4()) + "_" + title
    fp = FilePath(file_id=file_id, title=title)

    path = 'media/' + file_id
    with open(path, 'wb+') as destination:
        for chunk in file_obj.chunks():
            destination.write(chunk)
    
    fp.save()

@require_POST
def file_delete(request):
    if request.method == 'POST':
        pass
    form = UploadFileForm()
    context = {
        'form': form,
    }
    return render(request, 'file_upload.html', context)
