from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_CHOICES = [
        ('organizer', 'Organizer'),
        ('attendee', 'Attendee'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='attendee')


class Organizer(models.Model):
    user=models.OneToOneField(User , related_name='organizer', on_delete=models.CASCADE , blank=False) # so what happend was i was tring to make the related_name = user one thing is that if the user is attedee we can't store here and it won't be stored so no need to complecate
    org_name=models.CharField(max_length=100)
    contact_no=models.CharField(max_length=13)
    web=models.URLField(blank=True , null=True)

    def __str__(self):
        
        return f" the orginizer is {self.org_name} and contact info is {self.contact_no} "
    
class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, blank=True)
    location = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    organizer = models.ForeignKey(Organizer, related_name='events', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} | {self.location} ({self.start_date} - {self.end_date})"
