from django.urls import path
from landing.views import Index

# default html, when user clicks on the url they get diected to the landing page
urlpatterns = [
    path('', Index.as_view(), name='index'),
]
