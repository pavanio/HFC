from django.db import models
from TFC.models import Organization

class Partner(Organization):
    def __str__(self):
        return self.name
    class Meta:
        proxy=True
        verbose_name = "Partner"
        verbose_name_plural = "Partners"

STATUS_CHOICES = [
    ("Draft", "Draft"),
    ("New / Open", "New / Open"),
    ("Work In Progress", "Work In Progress"),
    ("Resolved", "Resolved")
]

class Problem_Statement(models.Model):
    title = models.CharField(max_length=500)
    summary = models.TextField()
    background_info = models.TextField()
    related_link = models.URLField()
    proposed_solution = models.TextField()
    partner_id = models.ForeignKey(Partner, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Problem_Statement"
        verbose_name_plural = "Problem_Statements"

class Project(models.Model):
    name = models.CharField(max_length=500)
    project_link = models.URLField()
    project_icon = models.ImageField()
    project_desc = models.TextField()
    website_link = models.URLField()
    goal = models.TextField()
    funded_by = models.CharField(max_length=300)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

TYPE_CHOICES = [
    ("Center", "Center"),
    ("Chapter", "Chapter")
]

class Community_Organization(models.Model):
    organization_name = models.CharField(max_length=500)
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    website = models.URLField(blank=True,null=True)
    logo = models.ImageField(blank=True,null=True)
    coordinator_name = models.CharField(max_length=100)
    coordinator_email = models.EmailField()
    coordinator_mobile = models.IntegerField()

    def __str__(self):
        return self.organization_name

    class Meta:
        verbose_name = "Community_Organization"
        verbose_name_plural = "Community_Organizations"



