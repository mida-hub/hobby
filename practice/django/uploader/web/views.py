from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from django.http import HttpResponse
from django.contrib import messages
from .models import FilePath
import uuid

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
        queryset = FilePath.objects.all()
        context = {
            'form': form,
            'file_path_list': queryset,
        }
    return render(request, 'file_upload.html', context)

def handle_uploaded_file(file_obj):
    title = file_obj.name

    if '.' in title:
        file_id = title.split('.')[0] + '_' + str(uuid.uuid4()) + '.' + title.split('.')[1]
    else:
        file_id = title + '_' + str(uuid.uuid4())

    fp = FilePath(file_id=file_id, title=title)
    path = 'media/' + file_id
    with open(path, 'wb+') as destination:
        for chunk in file_obj.chunks():
            destination.write(chunk)
    
    fp.save()
