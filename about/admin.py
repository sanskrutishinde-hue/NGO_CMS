from django.contrib import admin
from .models import OurStory, CoreValue, Program, TeamMember


@admin.register(OurStory)
class OurStoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'created_at', 'updated_at')
    search_fields = ('content',)


@admin.register(CoreValue)
class CoreValueAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'created_at', 'updated_at')
    search_fields = ('value',)


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'created_at', 'updated_at')
    search_fields = ('name', 'description')


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'role', 'image_url', 'created_at', 'updated_at')
    search_fields = ('name', 'role')