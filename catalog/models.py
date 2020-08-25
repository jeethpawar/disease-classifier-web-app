from django.db import models



class Symptom(models.Model):
    name = models.CharField(max_length=200)
    value = models.BooleanField(default=False)
    severe = models.BooleanField(default=False)
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.my_field_name

