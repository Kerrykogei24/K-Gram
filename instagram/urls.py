from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.index,name = 'timeline'),
    url(r'^newpost/$',views.new_post,name='newpost'),
    url(r'^editprofile/$',views.edit_profile,name='editprofile'),
    url(r'^accounts/profile/$',views.profile,name='profile'),
    url(r'^singlepic/(\d+)',views.single_pic,name='singlepic'),
    url(r'^search/',views.search_results,name = 'search_results'),
    url(r'^logout/$',views.logout_request,name="logout"),
    url(r'^comment/<int:id>/',views.comment,name='comment'),
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)