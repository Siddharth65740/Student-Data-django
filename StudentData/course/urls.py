from django.urls import path
from .views import newcourse,listview,update_view,delete_view,detail_view

urlpatterns=[
    path("new/",newcourse.as_view(),name="course-new"),
    path("list/",listview.as_view(),name="course-list"),
    path("update/<int:pk>",update_view.as_view(),name="course-update"),
    path("view/<int:pk>",detail_view.as_view(),name="course-view"),
    path("delete/<int:pk>",delete_view.as_view(),name="course-delete")
]