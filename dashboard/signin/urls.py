from django.urls import path
from signin import views

app_name = "signin"
urlpatterns = [
    path("", views.login_page, name="login_page")
]