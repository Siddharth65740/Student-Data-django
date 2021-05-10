from .views import create_view,paymentListView,paymentUpdateView,delete_payment,detail_payment
from django.urls import path

urlpatterns=[
    path("new/",create_view.as_view(),name="payment-create"),
    path("list/",paymentListView.as_view(),name="payment-list"),
    path("<int:pk>/update",paymentUpdateView.as_view(), name="payment-update"),
    path("detail/<int:pk>",detail_payment.as_view(),name="payment-detail"),
    path("delete/<int:pk>",delete_payment.as_view(), name="payment-delete"),

]