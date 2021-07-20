from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.http import JsonResponse
from .models import *

class BirdTypeViewSet(ViewSet):
    def list(self, request):
        return Response({'success':True})


    def jsondata(request):
        data =list(Xml.objects.values())

        return JsonResponse(data, safe=False)