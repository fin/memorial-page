from django.conf.urls import patterns, include, url

from views import submission, SubmissionListView, SubmissionUpdateView, ImageCreateView, delete_image


urlpatterns = patterns(
    "",
    url(r"^$", SubmissionListView.as_view(), name='home'),
    url(r"^submit/", submission, name='submit'),
    url(r"^edit/(?P<pk>[0-9]+)/$", SubmissionUpdateView.as_view(), name='submission-edit'),
    url(r"^edit/(?P<pk>[0-9]+)/upload_image/$", ImageCreateView.as_view(), name='jfu-upload'),
    url(r"^edit/(?P<pk>[0-9]+)/delete_image/$", delete_image, name='jfu-delete'),
    url(r"^edit/(?P<pk>[0-9]+)/links/$", delete_image, name='link-inlines'),
)
