from django.db import models
from django.contrib.auth.models import User

class Routine(models.Model):
    GAME_CHOICES = [
        ('VALORANT', 'Valorant'),
        ('CS2', 'Counter-Strike 2'),
        ('FORTNITE', 'Fortnite')
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    game = models.CharField(max_length=10, choices=GAME_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# Create your models here.
