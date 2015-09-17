from django.contrib import admin
from models import Submission, Image

class ImageInlineAdmin(admin.TabularInline):
    model = Image

class SubmissionAdmin(admin.ModelAdmin):
    inlines = [ImageInlineAdmin]

admin.site.register(Submission, SubmissionAdmin)
