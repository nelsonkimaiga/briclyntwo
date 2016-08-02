"""
Briclyn URL Configuration
"""
from django.conf.urls import url, patterns, include
from django.conf import settings
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from briclyn import views

urlpatterns = patterns('',
    url(r'^admin/', admin.site.urls),
    # url(r'^search/', include('haystack.urls')),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',{'next_page': '/'}),
    url(r'^accounts/', include('allauth.urls')),
    
    url(r'^$', views.index, name='index'),
    url(r'^profile/$', views.edit_profile, name='edit'),
    url(r'^home/$', views.home, name='home'),

    url(r'^create/$', views.addnewlisting, name='create'),
    url(r'^listings/$', views.listing_items, name='listings'),
    url(r'^(?P<id>\d+)/$', views.listing_detail, name='detail'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)