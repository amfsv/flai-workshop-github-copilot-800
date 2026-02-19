from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import datetime, timedelta
import random


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Clearing existing data...')
        # Delete existing data using Django ORM
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Existing data cleared'))

        # Create teams
        self.stdout.write('Creating teams...')
        team_marvel = Team.objects.create(
            name='Team Marvel',
            description='Earth\'s Mightiest Heroes unite for fitness!'
        )
        team_dc = Team.objects.create(
            name='Team DC',
            description='Justice League training program for peak performance!'
        )
        self.stdout.write(self.style.SUCCESS(f'Created teams: {team_marvel.name}, {team_dc.name}'))

        # Create superhero users
        self.stdout.write('Creating superhero users...')
        marvel_heroes = [
            {'name': 'Tony Stark', 'email': 'ironman@avengers.com', 'team_id': team_marvel.id},
            {'name': 'Steve Rogers', 'email': 'captain@avengers.com', 'team_id': team_marvel.id},
            {'name': 'Natasha Romanoff', 'email': 'blackwidow@avengers.com', 'team_id': team_marvel.id},
            {'name': 'Thor Odinson', 'email': 'thor@asgard.com', 'team_id': team_marvel.id},
            {'name': 'Bruce Banner', 'email': 'hulk@avengers.com', 'team_id': team_marvel.id},
            {'name': 'Peter Parker', 'email': 'spiderman@avengers.com', 'team_id': team_marvel.id},
        ]
        
        dc_heroes = [
            {'name': 'Clark Kent', 'email': 'superman@justiceleague.com', 'team_id': team_dc.id},
            {'name': 'Bruce Wayne', 'email': 'batman@justiceleague.com', 'team_id': team_dc.id},
            {'name': 'Diana Prince', 'email': 'wonderwoman@justiceleague.com', 'team_id': team_dc.id},
            {'name': 'Barry Allen', 'email': 'flash@justiceleague.com', 'team_id': team_dc.id},
            {'name': 'Arthur Curry', 'email': 'aquaman@justiceleague.com', 'team_id': team_dc.id},
            {'name': 'Victor Stone', 'email': 'cyborg@justiceleague.com', 'team_id': team_dc.id},
        ]
        
        all_heroes = marvel_heroes + dc_heroes
        users = []
        for hero in all_heroes:
            user = User.objects.create(**hero)
            users.append(user)
            self.stdout.write(f'  Created user: {user.name}')

        # Create activities
        self.stdout.write('Creating activities...')
        activity_types = ['Running', 'Cycling', 'Swimming', 'Weightlifting', 'Yoga', 'Boxing', 'HIIT']
        activity_count = 0
        
        for user in users:
            # Each user gets 5-10 random activities
            num_activities = random.randint(5, 10)
            for i in range(num_activities):
                activity_type = random.choice(activity_types)
                duration = random.randint(20, 120)  # 20-120 minutes
                distance = round(random.uniform(1.0, 20.0), 2) if activity_type in ['Running', 'Cycling', 'Swimming'] else None
                calories = duration * random.randint(5, 12)  # Rough calorie calculation
                days_ago = random.randint(0, 30)
                date = datetime.now() - timedelta(days=days_ago)
                
                Activity.objects.create(
                    user_id=user.id,
                    activity_type=activity_type,
                    duration=duration,
                    distance=distance,
                    calories=calories,
                    date=date
                )
                activity_count += 1
        
        self.stdout.write(self.style.SUCCESS(f'Created {activity_count} activities'))

        # Create leaderboard entries
        self.stdout.write('Creating leaderboard entries...')
        for user in users:
            # Calculate user stats
            user_activities = Activity.objects.filter(user_id=user.id)
            total_calories = sum(a.calories for a in user_activities)
            total_activities = user_activities.count()
            total_duration = sum(a.duration for a in user_activities)
            
            Leaderboard.objects.create(
                user_id=user.id,
                total_calories=total_calories,
                total_activities=total_activities,
                total_duration=total_duration,
                rank=0  # Will update ranks after
            )
        
        # Update leaderboard ranks
        leaderboard_entries = Leaderboard.objects.all().order_by('-total_calories')
        for idx, entry in enumerate(leaderboard_entries, start=1):
            entry.rank = idx
            entry.save()
        
        self.stdout.write(self.style.SUCCESS(f'Created {len(users)} leaderboard entries'))

        # Create workout suggestions
        self.stdout.write('Creating workout suggestions...')
        workouts = [
            {
                'name': 'Iron Man Cardio Blast',
                'description': 'High-intensity interval training inspired by Tony Stark\'s armor testing routines',
                'activity_type': 'HIIT',
                'difficulty': 'Hard',
                'estimated_duration': 45,
                'estimated_calories': 500
            },
            {
                'name': 'Captain America Circuit',
                'description': 'Full-body strength and endurance circuit training for peak performance',
                'activity_type': 'Weightlifting',
                'difficulty': 'Medium',
                'estimated_duration': 60,
                'estimated_calories': 450
            },
            {
                'name': 'Thor Thunder Run',
                'description': 'Powerful running workout to build godlike stamina',
                'activity_type': 'Running',
                'difficulty': 'Hard',
                'estimated_duration': 50,
                'estimated_calories': 600
            },
            {
                'name': 'Black Widow Flexibility Flow',
                'description': 'Yoga and flexibility routine for agility and balance',
                'activity_type': 'Yoga',
                'difficulty': 'Easy',
                'estimated_duration': 30,
                'estimated_calories': 150
            },
            {
                'name': 'Superman Strength Session',
                'description': 'Ultimate strength training workout with compound movements',
                'activity_type': 'Weightlifting',
                'difficulty': 'Hard',
                'estimated_duration': 75,
                'estimated_calories': 550
            },
            {
                'name': 'Batman Combat Training',
                'description': 'Martial arts inspired boxing and combat conditioning',
                'activity_type': 'Boxing',
                'difficulty': 'Medium',
                'estimated_duration': 45,
                'estimated_calories': 450
            },
            {
                'name': 'Wonder Woman Warrior Workout',
                'description': 'Balanced strength and cardio training for warrior conditioning',
                'activity_type': 'HIIT',
                'difficulty': 'Medium',
                'estimated_duration': 40,
                'estimated_calories': 400
            },
            {
                'name': 'Flash Speed Training',
                'description': 'Sprint intervals and speed work to maximize velocity',
                'activity_type': 'Running',
                'difficulty': 'Hard',
                'estimated_duration': 35,
                'estimated_calories': 450
            },
            {
                'name': 'Aquaman Swim Challenge',
                'description': 'Endurance swimming workout for total body conditioning',
                'activity_type': 'Swimming',
                'difficulty': 'Medium',
                'estimated_duration': 60,
                'estimated_calories': 500
            },
            {
                'name': 'Spider-Man Wall Climb Circuit',
                'description': 'Bodyweight climbing and calisthenics routine',
                'activity_type': 'HIIT',
                'difficulty': 'Easy',
                'estimated_duration': 30,
                'estimated_calories': 300
            },
        ]
        
        for workout_data in workouts:
            Workout.objects.create(**workout_data)
        
        self.stdout.write(self.style.SUCCESS(f'Created {len(workouts)} workout suggestions'))
        
        # Summary
        self.stdout.write(self.style.SUCCESS('\n=== Database Population Complete ==='))
        self.stdout.write(f'Teams: {Team.objects.count()}')
        self.stdout.write(f'Users: {User.objects.count()}')
        self.stdout.write(f'Activities: {Activity.objects.count()}')
        self.stdout.write(f'Leaderboard entries: {Leaderboard.objects.count()}')
        self.stdout.write(f'Workouts: {Workout.objects.count()}')
