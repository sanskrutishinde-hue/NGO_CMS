from django.contrib import admin
from .models import Banner, VisionMission, Statistic, Initiative


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_order', 'status')
    list_filter = ('status',)
    search_fields = ('title',)


@admin.register(VisionMission)
class VisionMissionAdmin(admin.ModelAdmin):
    list_display = ('vision_title', 'mission_title', 'last_updated')


@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ('label', 'value', 'display_order', 'status')
    list_filter = ('status',)
    search_fields = ('label',)


@admin.register(Initiative)
class InitiativeAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_order', 'status')
    list_filter = ('status',)
    search_fields = ('title',)