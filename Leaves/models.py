from django.db import models
from django.contrib.auth.models import User


class Leave(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Emp_id = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=30, default='Successfully applied')

    def __str__(self):
        return f"{self.user.username} - {self.start_date} to {self.end_date} ({self.status})"
