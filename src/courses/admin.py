from django.contrib import admin
from . models import Course, Category, Tag

#admin.site.register(Coruse)
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'available', 'teacher')      #for displaying in admin panel
    list_filter = ('available',)              #for sorting categories
    search_fields = ('name', 'description',)  #search bar


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}