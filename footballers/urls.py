from django.urls import path, re_path
from .views import *

urlpatterns = [
    path("", index, name='main'),
    path("about/", about, name='about'),
    path("addpage/", addpage, name='addpage'),
    path("contact/", contact, name='contact'),
    path("login/", login, name='login'),
    path("post/<slug:post_id>", show_post, name='post'),
    path("category/<slug:category_name>", show_category, name='category')
]