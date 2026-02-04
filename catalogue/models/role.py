from django.db import models
from django.contrib.auth.models import User

class Role(models.Model):
    role = models.CharField(max_length=30)
    users = models.ManyToManyField(User, related_name='roles', db_table='role_user')

    def __str__(self):
        return self.role

    class Meta:
        db_table = "roles"
