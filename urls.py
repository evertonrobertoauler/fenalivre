from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns("",
    ("^admin/", include(admin.site.urls)),
    url(r'^social_auth/login/', include('social_auth.urls')),
    url(r'^programacao/pdf/', 'evento.views.pdf'),
    url("^$", "mezzanine.pages.views.page", {"slug": "/"}, name="home"),
    ("^", include("mezzanine.urls")),
)

# Adds ``STATIC_URL`` to the context of error pages, so that error
# pages can use JS, CSS and images.
handler404 = "mezzanine.core.views.page_not_found"
handler500 = "mezzanine.core.views.server_error"
