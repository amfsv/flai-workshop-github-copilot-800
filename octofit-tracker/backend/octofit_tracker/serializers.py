from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model"""
    id = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'team_id', 'created_at']
        read_only_fields = ['created_at']


class TeamSerializer(serializers.ModelSerializer):
    """Serializer for Team model"""
    id = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'created_at']
        read_only_fields = ['created_at']


class ActivitySerializer(serializers.ModelSerializer):
    """Serializer for Activity model"""
    id = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Activity
        fields = ['id', 'user_id', 'activity_type', 'duration', 'distance', 'calories', 'date', 'created_at']
        read_only_fields = ['created_at']


class LeaderboardSerializer(serializers.ModelSerializer):
    """Serializer for Leaderboard model"""
    id = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Leaderboard
        fields = ['id', 'user_id', 'total_calories', 'total_activities', 'total_duration', 'rank', 'updated_at']
        read_only_fields = ['updated_at']


class WorkoutSerializer(serializers.ModelSerializer):
    """Serializer for Workout model"""
    id = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'activity_type', 'difficulty', 'estimated_duration', 'estimated_calories', 'created_at']
        read_only_fields = ['created_at']
