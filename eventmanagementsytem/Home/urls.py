from django.contrib import admin
from django.urls import path
from Home import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home),
    path("event/", views.event, name="event"),
    path("location/", views.location, name="location"),
    path("creatEvent/", views.creatEvent, name="creatEvent"),
    path("creatLocation/", views.creatLocation, name="creatLocations"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout, name="logout"),
    path("editEvent/<int:number>/", views.editEvent, name="edit"),
    path("editLocation/<int:number>/", views.editLocation, name="edit"),
    path("delete/<str:c>/<int:number>/", views.delete, name="delete")
]