from django.db import models
import uuid 

class Organization(models.Model):
    org_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 500)
    website = models.URLField()
    partner_desc = models.TextField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField() 
    logo = models.ImageField(upload_to = 'organization/', null=True, blank=True)
    address = models.TextField()
    city = models.CharField(max_length = 100)
    state = models.CharField(max_length = 100)
    zip_code =  models.CharField(max_length = 100)
    subdomain =  models.CharField(max_length = 100,blank = True)
    thankyou_template =  models.CharField(max_length = 500,blank = True)
    upi_id = models.CharField(max_length = 100,blank = True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Organization"
        verbose_name_plural = "Organizations"



class Team_Member(models.Model):
    member_id = models.AutoField(primary_key =True)
    organization = models.ForeignKey(Organization,on_delete=models.CASCADE, verbose_name='organization')
    member_name = models.CharField(max_length = 500)
    member_email = models.EmailField() 
    member_phone_number = models.CharField(max_length = 20)
    password = models.CharField(max_length=20)
    auth_token = models.UUIDField(default = uuid.uuid4, editable = False)
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.member_name
    class Meta: 
        verbose_name = "Team_Member"
        verbose_name_plural = "Team_Members"


