from django.db import models


class Attend(models.Model):
    attend_name = models.CharField(max_length=100)
    attend_day = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.attend_name
