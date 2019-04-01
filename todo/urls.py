from django.urls import path
from .views import MyTodoApp, RedirectToA, RedirectToB

urlpatterns = [
    path('', MyTodoApp.as_view(), name="Home"),
    path('a/', RedirectToA.as_view(), name="RedirectA"),
    path('b/', RedirectToB.as_view(), name="RedirectB"),
]
