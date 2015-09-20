from django.conf.urls import patterns, include, url

from views import submission, SubmissionListView, SubmissionUpdateView, ImageCreateView, delete_image
from django.views.decorators.cache import cache_page


urlpatterns = patterns(
    "",
    url(r"^$", cache_page(60*15)(SubmissionListView.as_view()), name='home'),
    url(r"^submit/", submission, name='submit'),
    url(r"^edit/(?P<pk>[0-9]+)/$", SubmissionUpdateView.as_view(), name='submission-edit'),
    url(r"^edit/(?P<pk>[0-9]+)/upload_image/$", ImageCreateView.as_view(), name='jfu-upload'),
    url(r"^edit/(?P<pk>[0-9]+)/delete_image/$", delete_image, name='jfu-delete'),
    url(r"^edit/(?P<pk>[0-9]+)/links/$", delete_image, name='link-inlines'),
)
