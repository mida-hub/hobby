from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from django.http import HttpResponse
from django.contrib import messages

def file_upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            title = request.POST.get('title')
            handle_uploaded_file(title, request.FILES['file'])
            file_obj = request.FILES['file']

            messages.success(request, "アップロードが成功しました。")

            return HttpResponseRedirect('/web')
        else:
            messages.error(request, "アップロードが失敗しました。")
            return HttpResponseRedirect('/web')
    else:
        form = UploadFileForm()
    return render(request, 'file_upload.html', {'form': form})

def handle_uploaded_file(title, file_obj):
    title = title if title is not None else file_obj.name
    file_path = 'media/' + title
    with open(file_path, 'wb+') as destination:
        for chunk in file_obj.chunks():
            destination.write(chunk)
