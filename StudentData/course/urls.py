from django.urls import path
from .views import newcourse,listview

urlpatterns=[
    path("new/",newcourse.as_view(),name="course-new"),
    path("list/",listview.as_view(),name="course-list")
]