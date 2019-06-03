from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ExtraUser, AudioFileModel


admin.site.register(ExtraUser, UserAdmin)


@admin.register(AudioFileModel)
class AudioFileAdmin(admin.ModelAdmin):

    list_display = ("__str__", "audio_file", "description")
    fields = ("audio_file", "description")
    list_display_links = ("description", )
    #list_editable = ("audio_file", )
