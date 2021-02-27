from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from AdminApp.models import Workstation
from AdminApp.serializers import WorkstationSerializer

# Create your views here.
@csrf_exempt
def workstationApi(request):
    if request.method == 'GET':
        workstations = Workstation.objects.all()
        workstations_serializer = WorkstationSerializer(workstations, many=True)
        return JsonResponse(workstations_serializer.data, safe=False)

    elif request.method == 'POST':
        workstation_data = JSONParser().parse(request)
        workstations_serializer = WorkstationSerializer(data=workstation_data)
        if workstations_serializer.is_valid():
            workstations_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)
