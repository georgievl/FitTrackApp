from django.contrib import admin
from .models import (
    UserProfile,
    GoalPlan
)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', 'weight', 'height')
    search_fields = ('user__username',)
    readonly_fields = ('user',)
    fieldsets = (
        (None, {'fields': ('user',)}),
        ('Personal Info', {'fields': ('age', 'weight', 'height')}),
    )


@admin.register(GoalPlan)
class GoalPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'length')
    list_filter = ('length',)
    search_fields = ('name',)
    ordering = ('length',)
