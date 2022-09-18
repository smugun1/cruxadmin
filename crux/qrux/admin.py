from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Farm_items, Contact

# Register your models here.


admin.site.unregister(Group)
admin.site.register(Farm_items)
admin.site.register(Contact)


