from django.db import models
from TFC.models import Organization
from ScreeningApp.models import *
from autoslug import AutoSlugField

EXPERIENCE=(
    ('No Experience', 'No Experience'),
    ('1+ years', '1+ years'),
    ('2+ years','2+ years'),
    ('3+ years','3+ years'),
    ('5+ years','5+ years'),
    ('10+ years','10+ years'),
    ('15+ years','15+ years'),
    ('20+ years','20+ years'),
)
class Issue_Area(models.Model):
    issue_area = models.CharField(max_length=100)
    issue_area_slug =AutoSlugField(populate_from='issue_area')
    def __str__(self):
        return self.issue_area 

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
    related_link = models.TextField(blank=True)
    proposed_solution = models.TextField(blank=True)
    partner_id = models.ForeignKey(Partner, on_delete=models.CASCADE,blank=True,null=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    title_slug=AutoSlugField(populate_from='title')
    issue_area = models.ManyToManyField('Issue_Area')
    

    def __str__(self):
        return self.title
    def issuearea(self):
        return ",".join([issue_area.issue_area for issue_area  in self.issue_area.all()])
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
    organization_name_slug = AutoSlugField(populate_from='organization_name',blank=True,null=True)


    def __str__(self):
        return self.organization_name

    class Meta:
        verbose_name = "Community_Organization"
        verbose_name_plural = "Community_Organizations"

MEMBER_TYPE_CHOICE = [
    ('Contributor', 'Contributor'),
    ('Mentor', 'Mentor')
]
class Community_Member(Candidate):
    type = models.CharField(max_length=50, choices=MEMBER_TYPE_CHOICE, default="Contributor")
    years_of_experience=models.CharField(choices=EXPERIENCE,max_length=200)
    coder_profile = models.URLField()
    linkedin_profile = models.URLField()
    organization_id=models.ForeignKey(Community_Organization, on_delete=models.CASCADE,blank=True,null=True)
    image = models.ImageField(blank=True,null=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Community_Member"
        verbose_name_plural = "Community_Members"

    def save(self, *args, **kwargs):     
        
        yoexp=self.years_of_experience
        if yoexp =="No Experience" or yoexp == "1+ years" or yoexp == "2+ years":
            self.level_of_expertise="Entry Level"
        elif yoexp == "3+ years" or  yoexp == "5+ years":
            self.level_of_expertise="Intermediate"
        elif yoexp == "10+ years" or yoexp == "15+ years":
            self.level_of_expertise="Advanced"
        else:
            self.level_of_expertise="Expert"
        super(Community_Member,self).save(*args, **kwargs) 

