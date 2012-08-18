from django.conf.urls import patterns, include, url
import settings
# Uncomment the next two lines to enable the admin:
import gemuka.admin as admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'gemuka.views.home', name='home'),
    # url(r'^gemuka/', include('gemuka.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # url('r^$', include(admin.site.urls)),
)

# urlpatterns += staticfiles_urlpatterns()
if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )