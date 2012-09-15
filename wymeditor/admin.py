# -*- coding: utf-8 -*-

from django.contrib import admin
from django.db import models
from wymeditor.widgets import WYMEditor

class RichTextAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': WYMEditor},
    }