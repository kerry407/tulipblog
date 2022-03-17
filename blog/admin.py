from django.contrib import admin
from .models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','category','author', 'status','updated', 'date_posted']
    list_filter = ['status','updated']
    search_fields = ('title',)
    raw_id_fields = ('author',)
    date_hierarchy = 'updated'
    ordering = ('status', 'updated')

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name','email','post','body','created_on','active']
    list_filter = ['active','created_on']
    search_fields = ['name','created_on','email']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


class ContactMessageAdmin(admin.ModelAdmin):
    list_display=('name','email','message','status', 'note')
    readonly_fields = ('name', 'email', 'message')
    list_filter= ['status']
    list_display_links = ('status','name','note')
    search_fields = ('name','email', 'message','status', 'note')
    list_per_page = 20

class SubscribeAdmin(admin.ModelAdmin):
    list_display = ['full_name','email','subscribed_at']

class AboutAdmin(admin.ModelAdmin):
    list_display = ['about']


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Subscribe, SubscribeAdmin)