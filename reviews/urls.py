from django.urls import path
from .views import home_page,review

urlpatterns = [
    path('search/',home_page,name="home_page"),
    path("search/comment/",review,name="review")
]