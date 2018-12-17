from django.urls import path

from . import views


app_name = "generic_app"
urlpatterns = [
    path('', views.GenericCreateView.as_view(), name='create_generic'),
]
