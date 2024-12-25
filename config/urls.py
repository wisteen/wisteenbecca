from django.contrib import admin
from django.urls import path,include,re_path
from django.views.generic import TemplateView
from django.views.static import serve
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('proposal/', include('proposal.urls')),
    path('', include('shareafric_app.urls')),

    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]


urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns= urlpatterns+ static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
handler404="shareafric_app.views.handle_error_page"

# Add this line for the set_language functionality
urlpatterns += [
    path('set_language/', include('django.conf.urls.i18n')),
]

from django.conf.urls import handler400, handler403, handler404, handler500
from shareafric_app.views import error_400_view, error_403_view, error_404_view, error_500_view, error_401_view

handler400 = error_400_view
handler403 = error_403_view
handler404 = error_404_view
handler500 = error_500_view