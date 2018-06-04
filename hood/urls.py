from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns=[
    url(r'^$',views.landing,name='landing'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^profile/edit/$',views.edit,name='edit'),
    url(r'^businesses/$',views.biz,name='biz'),
    url(r'^search/$',views.search_results,name='search_results'),
     url(r'^post/$',views.post,name='post'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)