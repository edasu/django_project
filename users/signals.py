from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

#reason to do signals we want user profile created for each user
@receiver(post_save, sender=User) #decorator
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    #**kwargs just exepts any additional keyworld argumend and of the function
    instance.profile.save()
