import json
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.models import Product
from products.serializers import ProductSerializer, SecondarySerializer




# Create your views here.
@api_view(["POST"])
def api_nyumbani(request, *args, **kwargs):

    """# to return a byte string
    body = request.body
    # from the purpose of interoperability
    data = {}
    try:
        # turning a string of Json data
        data = json.loads(body) # turns a string of Json data -> into a python dict

    except:
        pass
    print(data)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type"""

    serializer = ProductSerializer(data = request.data)
    if serializer.is_valid(raise_exception=True):
        print(serializer.data)
        return Response(serializer.data)
        
    return Response({"Invalid data": "DataExcpetionError"}, status=400)



    # return JsonResponse(data)