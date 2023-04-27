from django.urls import path
from . import views


urlpatterns = [
    path('csvjson/', views.CsvJsonView.as_view()),
]