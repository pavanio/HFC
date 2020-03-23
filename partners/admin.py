from django.contrib import admin

# Register your models here.
from .models import Partner
from .models import Address

admin.site.register(Partner)
admin.site.register(Address)