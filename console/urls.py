from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('security/', include('security.urls')),
    path('admin/', admin.site.urls),
]
