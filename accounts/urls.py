from django.urls import path
from accounts import views
urlpatterns = [
    path("example/", views.ExampleView.as_view(), name="example"),
]