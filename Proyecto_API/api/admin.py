import imp
from django.contrib import admin

from .models.languages import Languages
from .models.user import User
from .models.contacts import Contact
# Register your models here.

admin.site.register([User, Languages, Contact])