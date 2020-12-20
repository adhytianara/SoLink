from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

lst_user =[("Admin","Admin"),("Mitra","Mitra"),("Lembaga Sosial","Lembaga Sosial"),("Kontributor/Pembeli","Kontributor/Pembeli")]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20,
    choices = lst_user,
    default = 'Kontributor/Pembeli')

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()