from django.urls import path
from . import views
from .views import RegisterView


app_name = 'blog'

urlpatterns = (
    path("", views.PostView.as_view()),
    path("<int:page_id>/", views.PostDetails.as_view()),
    path("review/<int:post_id>/", views.AddComments.as_view(), name="add_comments"),
    path("profile/", views.profile_view, name="profile"),
    path('register/', RegisterView.as_view(), name="register")
)
