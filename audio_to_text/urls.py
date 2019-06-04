from django.urls import path
from .views import IndexView, ResultView


app_name = 'audio_to_text'
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("result/<int:pk>/<str:language>/<int:duration>/", ResultView.as_view(), name="result"),

]
