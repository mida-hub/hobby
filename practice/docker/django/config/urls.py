from django.contrib import admin
from django.urls import include
from django.urls import path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', RedirectView.as_view(url='/accounts/home/')),
    path('auth/', include('social_django.urls', namespace='social')),
]
