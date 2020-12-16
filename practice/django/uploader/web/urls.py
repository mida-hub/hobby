from django.urls import path
from . import views


app_name = 'web'
urlpatterns = [
    path('local/', views.file_upload, name='file_upload'),
    path('s3/root', views.RootDocumentCreateView.as_view(), name='s3_root'),
    path('s3/schema', views.SchemaDocumentCreateView.as_view(), name='s3_schema'),
    path('download/<int:pk>/<str:doc>', views.download, name='download'),
]
