# profiles/models.py
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    THEME_CHOICES = [
        ('light', 'Light'),
        ('dark', 'Dark'),
        ('minimal', 'Minimal'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    # ===== STYLE SETTINGS =====
    theme = models.CharField(
        max_length=20,
        choices=THEME_CHOICES,
        default='light'
    )

    background_color = models.CharField(
        max_length=20,
        default='#f3f4f6'  # gray-100
    )

    button_color = models.CharField(
        max_length=20,
        default='#000000'
    )

    button_text_color = models.CharField(
        max_length=20,
        default='#ffffff'
    )

    font_family = models.CharField(
        max_length=50,
        default='sans-serif'
    )

    def __str__(self):
        return self.user.username
