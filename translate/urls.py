from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib. staticfiles.views import serve
from django.views.decorators.cache import never_cache
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("audio_to_text.urls"))
]


if settings.DEBUG:
    #  enable open media file from admin
    urlpatterns.append(path("static/<path:path>", never_cache(serve)))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [path('__debug__/', include(debug_toolbar.urls)),
                   ] + urlpatterns
