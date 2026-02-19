from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Admin configuration for User model"""
    list_display = ['id', 'name', 'email', 'team_id', 'created_at']
    list_filter = ['team_id', 'created_at']
    search_fields = ['name', 'email']
    readonly_fields = ['created_at']


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    """Admin configuration for Team model"""
    list_display = ['id', 'name', 'description', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'description']
    readonly_fields = ['created_at']


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    """Admin configuration for Activity model"""
    list_display = ['id', 'user_id', 'activity_type', 'duration', 'distance', 'calories', 'date', 'created_at']
    list_filter = ['activity_type', 'date', 'created_at']
    search_fields = ['activity_type']
    readonly_fields = ['created_at']
    date_hierarchy = 'date'


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    """Admin configuration for Leaderboard model"""
    list_display = ['id', 'user_id', 'total_calories', 'total_activities', 'total_duration', 'rank', 'updated_at']
    list_filter = ['rank', 'updated_at']
    search_fields = ['user_id']
    readonly_fields = ['updated_at']
    ordering = ['rank']


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    """Admin configuration for Workout model"""
    list_display = ['id', 'name', 'activity_type', 'difficulty', 'estimated_duration', 'estimated_calories', 'created_at']
    list_filter = ['activity_type', 'difficulty', 'created_at']
    search_fields = ['name', 'description', 'activity_type']
    readonly_fields = ['created_at']
