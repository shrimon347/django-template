from django.urls import path

from .views import dashboard_view, delete_prayer,prayer_view, update_prayer

urlpatterns = [
    path("", dashboard_view, name="dashboard"),
    path("prayer/", prayer_view, name="prayer" ),
    path("update/<int:pk>/", update_prayer, name="update_prayer" ),
    path("delete/<int:pk>/", delete_prayer, name="delete_prayer" ),

]
