from django.urls import path
from teachers.views import TeacherListView, TeacherDetailView

urlpatterns = [
    path('', TeacherListView.as_view(), name="teachers"),   #index is function name
    path('teacher/<int:pk>', TeacherDetailView.as_view(), name="teacher_detail"),
    #path('categories/<slug:category_slug>', views.category_list, name="courses_by_category"),
    #path('tags/<slug:tag_slug>', views.tag_list, name='courses_by_tag'),
]
