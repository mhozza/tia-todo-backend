from django.db import models


class ToDo(models.Model):
    checked = models.BooleanField(default=False)
    value = models.TextField(max_length=200)
