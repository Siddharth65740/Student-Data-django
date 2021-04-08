from .views import create_view,admissionListView,admissionUpdateView
from django.urls import path

urlpatterns=[
    path("new/",create_view.as_view(),name="admission-create"),
    path("list/",admissionListView.as_view(),name="admission-list"),
    path("<int:pk>/update", admissionUpdateView.as_view(), name="admission-update"),
]