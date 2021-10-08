from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/client/', include('client.urls')),
    path('api/manager/', include('manager.urls')),
    path('api/user/', include('user.urls')),
]
