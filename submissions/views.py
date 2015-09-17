import os

from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from models import Submission, Image, Link


class SubmissionListView(ListView):
    queryset = Submission.objects.filter(accepted_at__isnull=False)


class SubmissionUpdateView(UpdateView):
    model = Submission
    fields = ['text','message']

    def get_queryset(self):
        base_qs = super(SubmissionUpdateView, self).get_queryset()
        return base_qs.filter(user=self.request.user, submitted_at__isnull=True)


def submission(request):
    s, created = Submission.objects.get_or_create(user=request.user,
        submitted_at__isnull=True)
    return HttpResponseRedirect(s.get_absolute_url())

class ImageCreateView(CreateView):
    model = Image
    fields = ['file']

    def form_valid(self, form):
        form.instance.submission = Submission.objects.get(pk=self.kwargs['pk'], submitted_at__isnull=True)
        self.object = form.save()
        data = {'status': 'success', 'removeLink': reverse('jfu-delete', kwargs={'pk': self.object.pk})}
        response = JsonResponse(data)
        return response

    def form_invalid(self, form):
        return HttpResponse('Not an Image', status=500)

def delete_image(request, pk):
    success = True
    try:
        instance = Image.objects.get( pk = pk )
        if instance.submission.user == request.user:
            os.unlink( instance.file.path )
            instance.delete()
        else:
            success = False
    except Image.DoesNotExist:
        success = False

    return HttpResponse(  'ok, gone' )

