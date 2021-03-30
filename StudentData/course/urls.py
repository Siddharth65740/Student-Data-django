from django.urls import path
from .views import newcourse

urlpatterns=[
    path("new/",newcourse.as_view(),name="course-new")
]