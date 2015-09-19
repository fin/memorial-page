from django.contrib import admin
from models import Submission, Image
from django.core.exceptions import PermissionDenied
from django_object_actions import DjangoObjectActions
from django.contrib.admin import SimpleListFilter
from datetime import datetime

class ModerationFilter(SimpleListFilter):
    title = 'Accepted'
    parameter_name = 'accepted'

    def lookups(self, request, model_admin):
        return (('unsent', 'Noch nicht abgesendet',),
                ('sent_not_accepted', 'Abgeschickt und nicht akzeptiert',),
                ('sent_accepted', 'Abgeschickt und akzeptiert',),)

    def queryset(self, request, queryset):
        submitted_at__isnull = self.value() == 'unsent'
        accepted_at__isnull = not self.value() == 'sent_accepted'
        return queryset.filter(accepted_at__isnull=accepted_at__isnull,
                submitted_at__isnull=submitted_at__isnull)

class ImageInlineAdmin(admin.TabularInline):
    model = Image

class SubmissionAdmin(DjangoObjectActions, admin.ModelAdmin):
    inlines = [ImageInlineAdmin]

    actions = ['approve']
    list_filter = ('accepted_at',ModerationFilter)

    def approve(self, request, queryset):
        for x in queryset:
            self.approve_obj(self, request, x)

        return None

    def approve_obj(self, request, obj):
        if not self.has_change_permission(request):
            raise PermissionDenied
        obj.accepted_at=datetime.now()
        obj.accepted_by=request.user
        obj.save()
        self.message_user(request, "Successfully marked submissions as accepted.")
    approve_obj.label = 'Approve'

    objectactions = ['approve_obj']




admin.site.register(Submission, SubmissionAdmin)
