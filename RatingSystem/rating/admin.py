from django.contrib import admin

from .models import *


class PersonAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'pub_date', 'change_date', 'is_scum']
	list_display_links = ['name']
	prepopulated_fields = {'slug': ('name', )}
	search_fields = ['name', 'is_scum']

class MarkAdmin(admin.ModelAdmin):
	list_display = ['from_person', 'to_person', 'mark']
	list_display_links = ['from_person', 'to_person']
	search_fields = ['from_person', 'to_person', 'mark']

class CommentAdmin(admin.ModelAdmin):
	list_display = ['from_person', 'to_person', 'slug', 'pub_date', 'change_date']
	list_display_links = ['from_person', 'to_person']
	search_fields = ['from_person', 'to_person', 'pub_date']

class CommentMarkAdmin(admin.ModelAdmin):
	list_display = ['from_person', 'comment', 'is_positive']
	list_display_links = ['from_person', 'comment']
	search_fields = ['from_person', 'comment', 'is_positive']


admin.site.register(Person, PersonAdmin)
admin.site.register(Mark, MarkAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(CommentMark, CommentMarkAdmin)
