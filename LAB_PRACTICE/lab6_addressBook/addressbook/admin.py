from django.contrib import admin
from .models import Person, Address, Message, Mark

admin.site.register(Person)
admin.site.register(Address)
admin.site.register(Message)
admin.site.register(Mark)