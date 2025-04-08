from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from octofit_tracker.test_data import test_data
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Populate users
        for user_data in test_data['users']:
            User.objects.create(**user_data)

        # Populate teams
        for team_data in test_data['teams']:
            Team.objects.create(**team_data)

        # Populate activities
        for activity_data in test_data['activities']:
            user = User.objects.get(username=activity_data.pop('user'))
            Activity.objects.create(user=user, **activity_data)

        # Populate leaderboard
        for leaderboard_data in test_data['leaderboard']:
            user = User.objects.get(username=leaderboard_data.pop('user'))
            Leaderboard.objects.create(user=user, **leaderboard_data)

        # Populate workouts
        for workout_data in test_data['workouts']:
            Workout.objects.create(**workout_data)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))