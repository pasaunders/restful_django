from django.db import models


class User(models.Model):
    """Create user model."""

    name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
