from django.db import models


class Symptoms(models.Model):
    """Models representing all symptoms in the dataset"""
    symptom_name = models.CharField(max_length=300)

    def __str__(self):
        """String for representing the model object"""
        return self.symptom_name
