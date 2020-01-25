from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from social.models import MyProfile, MyPost, FollowUser


class MyProfileAdmin(ModelAdmin):
    list_display = ['name']
    search_fields = ['msg','status','phone_no']
    list_filter = ['status','gender']
admin.site.register(MyProfile,MyProfileAdmin)

class MyPostAdmin(ModelAdmin):
    list_display = ["subject","cr_date","uploaded_by"]
    search_fields = ["subject","msg","uploaded_by"]
    list_filter = ["cr_date","uploaded_by"]
admin.site.register(MyPost,MyPostAdmin)


class FollowUserAdmin(ModelAdmin):
    list_display = ["profile","followed_by"]
    search_fields = ["profile","followed_by"]
    list_filter = ["profile","followed_by"]
admin.site.register(FollowUser,FollowUserAdmin)

