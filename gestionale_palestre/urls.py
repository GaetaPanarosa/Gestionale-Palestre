from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

from gestionale_palestre import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('core.urls'))
]
urlpatterns += static (settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
urlpatterns += staticfiles_urlpatterns ()