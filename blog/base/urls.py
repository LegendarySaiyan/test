from django.urls import path
from .views import DataView

app_name = "infos"

urlpatterns = [
    path('infos/', DataView.as_view()),
]
