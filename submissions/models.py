from django.db import models
from django.contrib.auth.models import User

class Submission(models.Model):
    user = models.ForeignKey(User, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    submitted_at = models.DateTimeField(null=True, blank=True)
    accepted_at = models.DateTimeField(null=True, blank=True)
    accepted_by = models.ForeignKey(User, null=True, blank=True, related_name='accepted_submissions')
    message = models.TextField(blank=True, null=True)

    text = models.TextField()

    @models.permalink
    def get_absolute_url(self):
        return ('submission-edit', tuple(), {'pk': self.id,},)

    @property
    def current_files(self):
        return [x for x in self.image_set.all() if x.file]

    def __unicode__(self):
        return u'Submission by %s (%s)' % (self.user.email or self.user.username, (self.text or '')[:10],)

class Image(models.Model):
    submission = models.ForeignKey(Submission)
    file = models.ImageField()

class Link(models.Model):
    submission = models.ForeignKey(Submission)
    link_to = models.TextField()

