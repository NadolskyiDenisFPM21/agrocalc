from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('main.urls')),    
    # path('', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('doc-gen/', include('docgen.urls')),

    # path('', include('django.contrib.auth.urls')),
]