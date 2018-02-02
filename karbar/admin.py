from django.contrib import admin
from .models import MyUser, Message


class MemberAdmin(admin.ModelAdmin):
    list_display = ['pk', 'user']


admin.site.register(MyUser, MemberAdmin)
admin.site.register(Message)


