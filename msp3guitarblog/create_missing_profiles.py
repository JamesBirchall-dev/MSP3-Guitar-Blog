from django.contrib.auth.models import User
from blog.models import Profile

# Run this in manage.py shell to create missing profiles for all users.


def create_missing_profiles():
    for user in User.objects.all():
        if not hasattr(user, 'profile'):
            Profile.objects.create(user=user)
            print(f"Created profile for user: {user.username}")
        else:
            print(f"Profile exists for user: {user.username}")


if __name__ == "__main__":
    create_missing_profiles()
