from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from AdminApp.models import Workstation
from AdminApp.serializers import WorkstationSerializer

from web3pkg.BlockchainClient import Client

client = Client("http://127.0.0.1:8545")


# Create your views here.
@csrf_exempt
def workstationApi(request, id=0):
    if request.method == 'GET':
        workstations = Workstation.objects.all()
        workstations_serializer = WorkstationSerializer(workstations, many=True)
        return JsonResponse(workstations_serializer.data, safe=False)

    elif request.method == 'POST':
        workstation_data = JSONParser().parse(request)
        workstations_serializer = WorkstationSerializer(data=workstation_data)
        istransactionok = False
        if workstations_serializer.is_valid():
            idws = str(workstation_data['WorkstationId'])
            xpos = int(workstation_data['Xposition'])
            ypos = int(workstation_data['Yposition'])
            wssts = workstation_data['Status']
            #non invio la transazione alla blockchain
            #client.addWorkspace(idws, xpos, ypos, wssts)
            istransactionok = True
        if istransactionok:
            workstations_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)

        return JsonResponse("Failed to Add.", safe=False)

    elif request.method == 'DELETE':
        workstation = Workstation.objects.get(WorkstationId=id)
        workstation.delete()
        # non invio la transazione alla blockchain
        #client.removeWorkspace(str(id))
        return JsonResponse("Deleted Succeffully!!", safe=False)
