from django.urls import path
from .views import studentview,list_view,update_view,detail_student,delete_student
urlpatterns=[
    path("new/",studentview.as_view(),name="student-create"),
    path("list/",list_view.as_view(),name="student-list"),
    path("update/<int:pk>",update_view.as_view(),name="student-update"),
    path("detail/<int:pk>",detail_student.as_view(),name="student-detail"),
    path("delete/<int:pk>", delete_student.as_view(), name="student-delete")

]