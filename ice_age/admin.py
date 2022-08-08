from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile, Posts


class ProfileLine(admin.StackedInline):
    model = Profile


class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']  # интерфейс
    inlines = [ProfileLine]


admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Posts)
# admin.site.register(Profile)
