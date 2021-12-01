from django.urls import path
from . import views

urlpatterns=[
    path("", views.home),
    path("<int:id>", views.single),
    path("brackfast", views.brackfast),
    path("lunch", views.lunch),
    path("dinner", views.dinner),
    path("snacks", views.snacks),
    path("search", views.searchresult),
    path("order/<int:itemID>", views.orderItem)
]