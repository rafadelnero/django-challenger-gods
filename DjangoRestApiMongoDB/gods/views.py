from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from gods.models import God
from gods.serializers import GodSerializer


@api_view(['GET', 'POST', 'DELETE'])
def god_list(request):
    if request.method == 'GET':
        print('Test')
        gods = God.objects.all()
        
        name = request.GET.get('name', None)
        if name is not None:
            gods = gods.filter(name__icontains=name)
        
        gods_serializer = GodSerializer(gods, many=True)
        return JsonResponse(gods_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        god_serializer = GodSerializer(data=tutorial_data)
        if god_serializer.is_valid():
            god_serializer.save()
            return JsonResponse(god_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(god_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = God.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def god_detail(request, pk):
    try: 
        god = God.objects.get(pk=pk)
    except God.DoesNotExist:
        return JsonResponse({'message': 'The God does not exist'}, status=status.HTTP_404_NOT_FOUND)
 
    if request.method == 'GET': 
        god_serializer = GodSerializer(god)
        return JsonResponse(god_serializer.data)
 
    elif request.method == 'PUT': 
        god_data = JSONParser().parse(request)
        god_serializer = GodSerializer(god, data=god_data)
        if god_serializer.is_valid():
            god_serializer.save()
            return JsonResponse(god_serializer.data)
        return JsonResponse(god_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    elif request.method == 'DELETE': 
        god.delete()
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def god_list_greek(request):
    gods = God.objects.filter(published=True)
        
    if request.method == 'GET': 
        gods_serializer = GodSerializer(gods, many=True)
        return JsonResponse(gods_serializer.data, safe=False)

