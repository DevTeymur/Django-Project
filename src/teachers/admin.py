from django.contrib import admin
from . models import Teacher

#admin.site.register(Coruse)
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name',)      #for displaying in admin panel
    search_fields = ('name',)     #search bar
