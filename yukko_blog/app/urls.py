from django.urls import path
from . import views

urlpatterns = [
    path("", views.about, name='About_page'),
    path("posts", views.posts, name='Posts_page'),
    path("mail", views.mail, name='Mail_page'),
    path("posts/<int:post_id>/", views.post_detail, name='post_detail'),
]