from django.conf.urls import url, include
from django.contrib import admin
from projects import urls as projects_urls
from django.contrib.auth import views

app_name = 'projects'



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^project/', include(projects_urls, namespace='project')),  
]















# if settings.DEBUG:
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

