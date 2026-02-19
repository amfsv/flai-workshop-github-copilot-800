from django.test import TestCase
from django.utils import timezone
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout


class UserModelTest(TestCase):
    """Test cases for User model"""
    
    def setUp(self):
        self.user = User.objects.create(
            name="Test User",
            email="test@example.com"
        )
    
    def test_user_creation(self):
        """Test that a user can be created"""
        self.assertEqual(self.user.name, "Test User")
        self.assertEqual(self.user.email, "test@example.com")
        self.assertIsNotNone(self.user.created_at)
    
    def test_user_string_representation(self):
        """Test the string representation of a user"""
        self.assertEqual(str(self.user), "Test User")


class TeamModelTest(TestCase):
    """Test cases for Team model"""
    
    def setUp(self):
        self.team = Team.objects.create(
            name="Test Team",
            description="A test team"
        )
    
    def test_team_creation(self):
        """Test that a team can be created"""
        self.assertEqual(self.team.name, "Test Team")
        self.assertEqual(self.team.description, "A test team")
        self.assertIsNotNone(self.team.created_at)
    
    def test_team_string_representation(self):
        """Test the string representation of a team"""
        self.assertEqual(str(self.team), "Test Team")


class ActivityModelTest(TestCase):
    """Test cases for Activity model"""
    
    def setUp(self):
        self.activity = Activity.objects.create(
            user_id=1,
            activity_type="Running",
            duration=30,
            distance=5.0,
            calories=300,
            date=timezone.now()
        )
    
    def test_activity_creation(self):
        """Test that an activity can be created"""
        self.assertEqual(self.activity.user_id, 1)
        self.assertEqual(self.activity.activity_type, "Running")
        self.assertEqual(self.activity.duration, 30)
        self.assertEqual(self.activity.calories, 300)
    
    def test_activity_string_representation(self):
        """Test the string representation of an activity"""
        self.assertEqual(str(self.activity), "Running - 30 mins")


class LeaderboardModelTest(TestCase):
    """Test cases for Leaderboard model"""
    
    def setUp(self):
        self.leaderboard = Leaderboard.objects.create(
            user_id=1,
            total_calories=1000,
            total_activities=5,
            total_duration=150,
            rank=1
        )
    
    def test_leaderboard_creation(self):
        """Test that a leaderboard entry can be created"""
        self.assertEqual(self.leaderboard.user_id, 1)
        self.assertEqual(self.leaderboard.total_calories, 1000)
        self.assertEqual(self.leaderboard.rank, 1)


class WorkoutModelTest(TestCase):
    """Test cases for Workout model"""
    
    def setUp(self):
        self.workout = Workout.objects.create(
            name="Morning Run",
            description="A quick morning run",
            activity_type="Running",
            difficulty="Medium",
            estimated_duration=30,
            estimated_calories=300
        )
    
    def test_workout_creation(self):
        """Test that a workout can be created"""
        self.assertEqual(self.workout.name, "Morning Run")
        self.assertEqual(self.workout.activity_type, "Running")
        self.assertEqual(self.workout.difficulty, "Medium")
    
    def test_workout_string_representation(self):
        """Test the string representation of a workout"""
        self.assertEqual(str(self.workout), "Morning Run")


class UserAPITest(APITestCase):
    """Test API endpoints for User"""
    
    def test_create_user(self):
        """Test creating a user via API"""
        url = '/api/users/'
        data = {'name': 'API User', 'email': 'api@example.com'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().name, 'API User')


class TeamAPITest(APITestCase):
    """Test API endpoints for Team"""
    
    def test_create_team(self):
        """Test creating a team via API"""
        url = '/api/teams/'
        data = {'name': 'API Team', 'description': 'Team created via API'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Team.objects.count(), 1)


class ActivityAPITest(APITestCase):
    """Test API endpoints for Activity"""
    
    def test_create_activity(self):
        """Test creating an activity via API"""
        url = '/api/activities/'
        data = {
            'user_id': 1,
            'activity_type': 'Running',
            'duration': 30,
            'calories': 300,
            'date': timezone.now().isoformat()
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
