from django.shortcuts import render, reverse
from django.views.generic.list import ListView
from .models import AudioFileModel
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .utilities import get_text_from_audio, translate_lng_lo_lng
from django.contrib import messages


class IndexView(ListView):
    """Index page controller"""
    model = AudioFileModel
    template_name = "audio_to_text/index.html"

    def post(self, request, *args, **kwargs):
        post_data = self.request.POST.get("languages", None)
        try:
            duration = int(self.request.POST.get("dur", None))
        except ValueError:
            duration = 0
        try:
            language = post_data.split(",")[0]
            pk = int(post_data.split(",")[1])
        except IndexError:
            messages.add_message(request, messages.WARNING, message=
            "Please choose language to translate to", fail_silently=True)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        return HttpResponseRedirect(reverse_lazy("audio_to_text:result",
                                                 args=(pk, language, duration)))


class ResultView(TemplateView):
    """Result page controller"""
    template_name = "audio_to_text/result.html"

    def get_context_data(self, **kwargs):
        context = TemplateView.get_context_data(self, **kwargs)
        obj = AudioFileModel.objects.get(pk=self.kwargs.get("pk"))

        text = get_text_from_audio(obj.filename(), duration=
        None if self.kwargs.get("duration") == 0 else self.kwargs.get("duration"))

        translated_text = translate_lng_lo_lng(text, dest=self.kwargs.get("language"))
        context["text"] = translated_text
        return context

