from django.contrib import admin
from models import Submission, Image
from django.core.exceptions import PermissionDenied
from datetime import datetime

class ImageInlineAdmin(admin.TabularInline):
    model = Image

class SubmissionAdmin(admin.ModelAdmin):
    inlines = [ImageInlineAdmin]

    actions = ['approve']
    list_filter = ('accepted_at',)

    def approve(self, request, queryset):
        opts = self.model._meta
        if not self.has_change_permission(request):
            raise PermissionDenied
        queryset.update(accepted_at=datetime.now(),
                        accepted_by=request.user)
        self.message_user(request, "Successfully marked submissions as accepted.")

        return None

admin.site.register(Submission, SubmissionAdmin)
