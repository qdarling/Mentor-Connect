from django.contrib import admin

# Register your models here.

from .models import Room, Topic, Message, User

admin.site.register(User)
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
admin.site.site_header = "MentorConnect  "
admin.site.site_title = "MentorConnect "
admin.site.index_title = "Welcome to our MentorConnect "
