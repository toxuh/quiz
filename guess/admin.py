from django.contrib import admin

from .models import Theme, Description, Word

admin.site.register(Theme)
admin.site.register(Description)
admin.site.register(Word)