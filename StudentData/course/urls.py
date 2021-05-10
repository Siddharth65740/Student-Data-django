from django.urls import path
from .views import newcourse,listview,update_view,delete_view,detail_view,get_fees,get,chartdemo

urlpatterns=[
    path("new/",newcourse.as_view(),name="course-new"),
    path("list/",listview.as_view(),name="course-list"),
    path("update/<int:pk>",update_view.as_view(),name="course-update"),
    path("view/<int:pk>",detail_view.as_view(),name="course-view"),
    path("delete/<int:pk>",delete_view.as_view(),name="course-delete"),
    path("get_fees/<int:course_id>/",get_fees,name="get_fees"),
    path("get_chart_Data",get,name="get-chart"),
    path("chart/",chartdemo, name="chart")

]