
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from store.views import detail,search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('store.urls')),
    path('article<int:id_article>',detail,name="detail"),
    path('article/recherche', search, name="search"),
    path('auth/', include('app_auth.urls')),
    path('my-admin/', include('app_admin.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
      