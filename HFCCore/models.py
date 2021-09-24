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
STATUS_CHOICES = [
    ("Draft", "Draft"),
    ("New / Open", "New / Open"),
    ("Work In Progress", "Work In Progress"),
    ("Resolved", "Resolved")
]
TYPE_CHOICES = [
    ("Center", "Center"),
    ("Chapter", "Chapter")
]

MEMBER_TYPE_CHOICE = [
    ('Contributor', 'Contributor'),
    ('Mentor', 'Mentor')
]

PROJECT_INVOLVEMENT = [
    ('Funding','Funding'),
    ('Execution','Execution'),
    ('Adoption','Adoption'),
    ('Promotion','Promotion')
]

PUBLIC = [
    ('True','True'),
    ('False','False'),
]
class Issue_Area(models.Model):
    issue_area = models.CharField(max_length = 100)
    issue_sub_header = models.TextField(blank = True, help_text ='This text is used for SEO purpose')
    issue_area_slug = AutoSlugField(populate_from = 'issue_area')
    issue_brief = models.TextField(blank = True)
    issue_overview = models.TextField(blank = True)
    context = models.TextField(blank = True)
    technology_intervention = models.TextField(blank = True)
    related_information = models.TextField(blank = True)
    def __str__(self):
        return self.issue_area 

class Partner(Organization):
    def __str__(self):
        return self.name
    class Meta:
        proxy = True
        verbose_name = "Partner"
        verbose_name_plural = "Partners"

class Problem_Statement(models.Model):
    problem_statement = models.CharField(max_length = 500)
    overview = models.TextField()
    background_info = models.TextField()
    related_link = models.TextField()
    name = models.TextField()
    email = models.TextField()
    phone_number = models.TextField()
    about_yourself = models.TextField()

    proposed_solution = models.TextField(blank = True)
    partner_id = models.ForeignKey(Partner, on_delete = models.CASCADE,blank = True,null = True)
    status = models.CharField(max_length = 100, choices = STATUS_CHOICES)
    title_slug = AutoSlugField(populate_from ='problem_statement')
    issue_area = models.ManyToManyField('Issue_Area')
    def __str__(self):
        return self.problem_statement
    def issuearea(self):
        return " , ".join([issue_area.issue_area for issue_area  in self.issue_area.all()])
    class Meta:
        verbose_name = "Problem_Statement"
        verbose_name_plural = "Problem_Statements"

class Project(models.Model):
    name = models.CharField(max_length = 500)
    project_link = models.URLField()
    project_icon = models.ImageField(blank = True,null = True)
    project_overview = models.TextField()
    website_link = models.URLField(blank = True,null = True)
    goal = models.TextField(blank = True,null = True)
    project_slug = AutoSlugField(populate_from = 'name',blank = True,null = True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

class Community_Organization(models.Model):
    organization_name = models.CharField(max_length = 500)
    type = models.CharField(max_length = 100, choices = TYPE_CHOICES)
    website = models.URLField(blank = True,null = True)
    logo = models.ImageField(blank = True,null = True)
    coordinator_name = models.CharField(max_length = 100)
    coordinator_email = models.EmailField()
    coordinator_mobile = models.IntegerField()
    organization_name_slug = AutoSlugField(populate_from = 'organization_name',blank = True,null = True)
    project = models.ManyToManyField('Project',blank = True,null = True)
    city = models.CharField(max_length = 50,blank = True,null = True)
    is_public = models.CharField(choices = PUBLIC, max_length = 10,blank = True,null = True, default ="False" )
    def __str__(self):
        return self.organization_name
    def get_project(self):
        return ",".join([project.name for project  in self.project.all()])
    class Meta:
        verbose_name = "Community_Organization"
        verbose_name_plural = "Community_Organizations"

class Community_Member(Candidate):
    type = models.CharField(max_length = 50, choices = MEMBER_TYPE_CHOICE, default = "Contributor")
    years_of_experience = models.CharField(choices = EXPERIENCE,max_length = 200)
    coder_profile = models.URLField(blank = True,null = True)
    linkedin_profile = models.URLField(blank = True,null = True)
    organization_id = models.ForeignKey(Community_Organization, on_delete = models.CASCADE,blank = True,null = True)
    image = models.ImageField(blank = True,null = True)
    commit = models.IntegerField(blank = True,null = True)
    avatar_url= models.URLField(blank = True,null = True)
    project = models.ManyToManyField('Project',blank = True,null = True)
    def __str__(self):
        return self.name
    def get_project(self):
        return ",".join([project.name for project  in self.project.all()])
    class Meta:
        verbose_name = "Community_Member"
        verbose_name_plural = "Community_Members"
    def save(self, *args, **kwargs):
        yoexp = self.years_of_experience
        if yoexp == "No Experience" or yoexp == "1+ years" or yoexp == "2+ years":
            self.level_of_expertise = "Entry Level"
        elif yoexp == "3+ years" or  yoexp == "5+ years":
            self.level_of_expertise = "Intermediate"
        elif yoexp == "10+ years" or yoexp == "15+ years":
            self.level_of_expertise = "Advanced"
        else:
            self.level_of_expertise = "Expert"
        super(Community_Member,self).save(*args, **kwargs) 

class Project_Partner(models.Model):
    project_id = models.ForeignKey(Project, on_delete = models.CASCADE,verbose_name ="Project")
    partner = models.ManyToManyField('Partner',blank = True)
    project_involvement = models.CharField(max_length = 50, choices = PROJECT_INVOLVEMENT)
    def get_partner(self):
        return ",".join([ partner.name for  partner  in self. partner.all()])
