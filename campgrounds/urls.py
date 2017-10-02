from django.conf.urls import url
from . import views

# urls
app_name = 'campgrounds'

urlpatterns = [
	#campground urls
	url(r'^$', views.CampgroundList.as_view(), name='all'),
	url(r'^new/$', views.CreateCampground.as_view(), name='create'),
	url(r'^(?P<pk>\d+)$', views.CampgroundDetail.as_view(), name='details'),
	url(r'^update/(?P<pk>\d+)/$', views.UpdateCampground.as_view(), name='update'),
	url(r'^delete/(?P<pk>\d+)/$', views.DeleteCampground.as_view(), name='delete'),
	#review urls
	url(r'^(?P<pk>\d+)/reviews/$', views.add_review_to_campground, name='add_review')
]