from django.db import models


class EmailSubscriber(models.Model):
    email = models.EmailField()
    created_at = models.DateTimeField()
