from django.db import models
from TFC.models import Organization

class Partner(Organization):
    def __str__(self):
        return self.name
    class Meta:
        proxy=True
        verbose_name = "Partner"
        verbose_name_plural = "Partners"

