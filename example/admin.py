from django.contrib import admin
from wymeditor.admin import RichTextAdmin
from example.models import TestModel

class TestModelAdmin(RichTextAdmin):
    pass

admin.site.register(TestModel, TestModelAdmin)