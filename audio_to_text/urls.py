from django.urls import path
from .views import IndexView, Resultview


app_name = 'audio_to_text'
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("result/", Resultview.as_view(), name="result"),

]
