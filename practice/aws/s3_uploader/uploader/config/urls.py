from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('web/', include('web.urls')),
    path('admin/', admin.site.urls),
]
