from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("random_page/", views.random_page, name="random_page"),
    path("new_page/", views.new_page, name="new_page"),
    path("already_exists/<str:title>", views.already_exists, name="already_exists"),
    path("search/", views.search, name="search"),
    path("results/<str:title>", views.results, name="results"),
    path("not_found/<str:title>", views.not_found, name="not_found"),
    # path("wiki/<str:title>", views.entry, name="wiki")
    path("wiki/edit_page", views.edit_page, name="edit_page"),
    # path("wiki/patch_page", views.patch_page, name="patch_page"),
    path("wiki/<str:title>", views.entry, name="entry")
]
