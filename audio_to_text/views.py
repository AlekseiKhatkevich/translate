from django.shortcuts import render, reverse
from django.views.generic.list import ListView
from .models import AudioFileModel
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


class IndexView(ListView):
    model = AudioFileModel
    template_name = "audio_to_text/index.html"

    def post(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse_lazy("audio_to_text:result"))


class Resultview(TemplateView):
    template_name = "audio_to_text/result.html"
