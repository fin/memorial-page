import os

from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from models import Submission, Image, Link
from django.forms.models import ModelForm, inlineformset_factory
from django.forms.utils import ErrorList
from django import forms
from datetime import datetime
from django.contrib import messages
from extra_views import InlineFormSet
from extra_views.advanced import UpdateWithInlinesView

class LinkInline(InlineFormSet):
    model = Link
    fields=['link','description']

class SubmissionForm(ModelForm):
    class Meta:
        model = Submission
        widgets={'message': forms.Textarea(attrs={'rows':2, 'cols':15}),
                 'text': forms.Textarea(attrs={'rows':4, 'cols':15})}
        fields = ['text','message','name','email',]

    def save(self, commit=True):
        x = super(SubmissionForm, self).save(commit=False)
        if 'send' in self.data:
            x.submitted_at = datetime.now()
        if commit:
            x.save()
        return x

    def clean_name(self):
        data = self.cleaned_data
        if 'send' in self.data:
            if not data.get('name', None):
                raise forms.ValidationError('Name needed for submission!')
        return data.get('name', None)

    def clean_text(self):
        data = self.cleaned_data
        if 'send' in self.data:
            if not data.get('text', None) and not self.instance.current_files:
                raise forms.ValidationError('Text or Pictures needed for submission!')
        return data.get('text', None)



class SubmissionListView(ListView):
    queryset = Submission.objects.filter(accepted_at__isnull=False).order_by('-accepted_at')

class SubmissionUpdateView(UpdateWithInlinesView):
    model = Submission
    form_class = SubmissionForm
    inlines = [LinkInline]

    def get_queryset(self):
        base_qs = super(SubmissionUpdateView, self).get_queryset()

        sid = self.request.session.get('submission_id',None)
        if not sid:
            sid = Submission.objects.create().pk
        self.request.session['submission_id'] = sid
        return base_qs.filter(pk=sid, accepted_at__isnull=True)

    def form_valid(self, form):
        if 'send' in self.request.POST:
            self.object = form.save()
            if self.object.name:
                self.object.submitted_at = datetime.now()
            self.object.save()
            if self.object.name and (self.object.text or self.object.current_files):
                messages.success(self.request, 'Thank you. A moderator will publish your submission as soon as possible!')
                return HttpResponseRedirect('/')
            else:
                error = form._errors.setdefault('name', ErrorList())
                error.append('Needed for submission!')
                if not self.object.name and not self.object.current_files:
                    error = form._errors.setdefault('text', ErrorList())
                    error.append('Please upload Images or add Text to submit.')
                return super(SubmissionUpdateView, self).form_invalid(form)


        return super(SubmissionUpdateView, self).form_valid(form)


def submission(request):
    sid = request.session.get('submission_id',None)
    if not sid or Submission.objects.get(pk=sid).submitted_at:
        sid = Submission.objects.create().pk
    request.session['submission_id'] = sid
    s, created = Submission.objects.get_or_create(pk=sid,
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
        if request.session['submission_id']==instance.submission.pk:
            os.unlink( instance.file.path )
            instance.delete()
        else:
            success = False
    except Image.DoesNotExist:
        success = False

    return HttpResponse(  'ok, gone' )


def LinkView(InlineFormSetView):
    model = Submission
    inlines = [LinkInline]
