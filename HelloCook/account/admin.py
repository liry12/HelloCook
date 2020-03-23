from django.contrib import admin
from .models import UserProfile, UserInfo


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone')
    list_filter = ('phone',)


admin.site.register(UserProfile, UserProfileAdmin)


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ("user", 'age', 'profession', 'aboutme', 'photo')
    list_filter = ("age",  "profession")


admin.site.register(UserInfo, UserInfoAdmin)
