from django.conf.urls import patterns, include, url
from rest_framework import routers
from projects import views as pviews
from page import views as sviews

from django.contrib import admin
admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'users', pviews.UserViewSet)
router.register(r'groups', pviews.GroupViewSet)
router.register(r'projects', pviews.ProjectViewSet)
router.register(r'updates', pviews.UpdateViewSet)

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'projectmanager.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),

	url(r'^admin/', include(admin.site.urls)),
	url(r'^api/', include(router.urls)),
	url(r'^update-list/(?P<pk>[^/]+)/$', pviews.UpdateListing.as_view(), name='update-listing'),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^projectdet/', sviews.projectdet, name='projectdet'),
	url(r'^', sviews.home, name='home'),
)