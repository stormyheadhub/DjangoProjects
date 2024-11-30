from django.db import models
# Create your models here.

class UniversityCampus(models.Model):
    campus = models.CharField(max_length=100, default="", blank=True, null=False)
    state = models.CharField(max_length=2, default="", blank=True, null=False)
    campusID = models.IntegerField(max_length=50, default="", blank=True, null=False)
    class Meta:
        app_label = 'universities'
        verbose_name = 'University Campus'
        verbose_name_plural = 'University Campuses'
