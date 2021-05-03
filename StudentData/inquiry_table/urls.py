from django.urls import path
from .views import newinquiry,listview,update_view,detail_view

urlpatterns=[
    path("new/",newinquiry.as_view(),name="inquiry-new"),
    path("list/",listview.as_view(),name="inquiry-list"),
    path("update/<int:pk>",update_view.as_view(),name="inquiry-update"),
    path("view/<int:pk>",detail_view.as_view(),name="inquiry-view"),
]