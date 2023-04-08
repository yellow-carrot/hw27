from django.http import JsonResponse
from django.shortcuts import render
from django.views import View


# Create your views here.

class StatusView(View):

    def get(self, request, *args, **kwargs):
        return JsonResponse({"status": "ok"}, status=200)


