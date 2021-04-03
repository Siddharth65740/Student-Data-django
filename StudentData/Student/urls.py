from django.urls import path
from .views import home,createview,studentlist
urlpatterns=[
    path('',home,name='home'),
    path("new/",createview.as_view(),name="student-create"),
    path("list/",studentlist.as_view(),name="student-list")
]