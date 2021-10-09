from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f"{self.user.username} profile"

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (200, 200)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Bio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(
        max_length=200, default='404 bio not found', null=True)

    def __str__(self):
        return f"{self.user.username} Bio"


def profileCreated(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


def bioCreated(sender, instance, created, **kwargs):
    if created:
        Bio.objects.create(user=instance)


post_save.connect(profileCreated, sender=User)
post_save.connect(bioCreated, sender=User)
