"""GSDivinoSys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path("view_dishes", views.view_dishes, name="view_dishes"),
    path("add_dish", views.add_dish, name="add_dish"),
    path("delete_dish/<int:pk>/", views.delete_dish, name="delete_dish"),
    path("update_dish/<int:pk>/", views.update_dish, name="update_dish"),
    path("view_laundry", views.view_laundry, name="view_laundry"),
    path("add_laundry", views.add_laundry, name="add_laundry"),
    path("delete_laundry/<int:pk>/", views.delete_laundry, name="delete_laundry"),
    path("update_laundry/<int:pk>/", views.update_laundry, name="update_laundry"),
    path("view_aircon", views.view_aircon, name="view_aircon"),
    path("add_aircon", views.add_aircon, name="add_aircon"),
    path("delete_aircon/<int:pk>/", views.delete_aircon, name="delete_aircon"),
    path("update_aircon/<int:pk>/", views.update_aircon, name="update_aircon"),
    path("view_bills", views.view_bills, name="view_bills"),
    path("add_bill", views.add_bill, name="add_bill"),
    path("delete_bill/<int:pk>/", views.delete_bill, name="delete_bill"),
    path("update_bill/<int:pk>/", views.update_bill, name="update_bill"),
    # path("view_wishlists", views.view_wishlists, name="view_wishlists"),
    # path("view_wishlist/<int:pk>", views.view_wishlist_details, name="view_wishlist_details"),
    # path("add_wish", views.add_wish, name="add_wish"),
    # path("delete_wish/<int:pk>/", views.delete_wish, name="delete_wish"),
    # path("update_wish/<int:pk/", views.update_wish, name="update_wish"),
    # path("view_sched", views.view_sched, name="view_sched"),
    # path("add_sched", views.add_sched, name="add_sched"),
    # path("delete_sched/<int:pk>/", views.delete_sched, name="delete_sched"),
    # path("update_sched/<int:pk/", views.update_sched, name="update_sched")
]
