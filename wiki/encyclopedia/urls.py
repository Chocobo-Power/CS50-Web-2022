from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("random_page/", views.random_page, name="random_page"),
    path("new_page/", views.new_page, name="new_page"),
    path("search/", views.search, name="search"),
    # path("wiki/<str:title>", views.entry, name="wiki")
    path("wiki/edit_page", views.edit_page, name="edit_page"),
    # path("wiki/patch_page", views.patch_page, name="patch_page"),
    path("wiki/<str:title>", views.entry, name="entry")
]
