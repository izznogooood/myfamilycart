from django.contrib import admin

from .models import Profile, Word


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
