from django.urls import path
from . import views

urlpatterns = [
    path('', views.file_upload, name='file_upload'),
    path('upload/', views.DocumentCreateView.as_view(), name='s3'),
    # path('upload/schema', views.SchemaDocumentCreateView.as_view(), name='s3'),
]
