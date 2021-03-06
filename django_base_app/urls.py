from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns(
    '',
    url(r'^$', 'django_base_app.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.SHOW_DEBUG_TOOLBAR:
    import debug_toolbar
    urlpatterns += patterns(
        '',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
