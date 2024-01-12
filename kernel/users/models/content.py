from django.db import models
from users.models import UserProfile

class SavedContent(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    content_name = models.CharField(max_length=100)
    content_id = models.IntegerField()

    def __str__(self):
        return f"{self.user_profile.user.username}'s saved {self.content_name}"
