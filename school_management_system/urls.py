from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/', include('accounts.urls')),
    path('academics/', include('academics.urls')),
    path('classes/', include('classes.urls')),

]
