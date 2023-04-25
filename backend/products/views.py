from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, mixins
from products.models import Product
from products.serializers import ProductSerializer, SecondarySerializer

# Create your views here.
class ProductDetail(
    generics.RetrieveAPIView,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.object
        print(context)
        return context
    

    def options(self, request, *args, **kwargs):
        data_ = request.validated_data
        return super().options(data_, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProductCreate(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        data_ = serializer.validated_data
        title = data_.get('title')
        content = data_.get('content')

        print({"title": title, "content": content})
        # return super().perform_create(serializer)

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def check_permissions(self, request):
        obj_request = request
        print(obj_request)

    def perform_create(self, serializer):
        data_ = serializer.validated_data
        title = data_.get('title')
        content = data_.get('content')

        print({"title": title, "content": content})
        # return super().check_permissions(request)

class ProductUpdate(generics.UpdateAPIView,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin):
    queryset = Product.objects.all()
    serializer_class = SecondarySerializer
    lookup_field = "pk"

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
            return super().perform_update(serializer.save())
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
        
    # In order to override the queryset functionality
    """def get_queryset(self):
            return Product.objects.filter(content=self.request.user)"""
        
class ProductDelete(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = SecondarySerializer
    lookup_field = "pk"

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

class ProductMixin(mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    generics.GenericAPIView
    ):
    queryset = Product.objects.all()
    serializer_class = SecondarySerializer
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        pk_ = kwargs.get("pk")
        if pk_ is not None:
            return self.retrieve(request, *args, **kwargs)
        return HttpResponse(self.queryset.all())
        # return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # print(args, kwargs)
        # pk_ = kwargs.get("pk")
        return self.create(request, *args, **kwargs)


        """try:
            if type(pk_) == None:
                print("Attempting object creation!")
                return self.create(request, *args, **kwargs)
            return HttpResponse(self.create)
        except:
            print("Item not created")"""



"""Function Based Views"""
@api_view(["GET", "POST"])
def productView(request, pk=None, *args, **kwargs):
    method_ = request.method

    if method_ == "GET":
        if pk is not None:
            obj = get_object_or_404(Product, pk=pk)
            serializerrr = ProductSerializer(obj, many=False)
            return Response(serializerrr.data)
        queryset = Product.objects.all()
        serializerr  = ProductSerializer(queryset, many=True)
        return Response(serializerr.data)
    
    if method_ == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content')
            if content is None:
                context = title

            serializer.save(content=content)
            print(serializer.data)
            return Response(serializer.data)
        return Response({"Invalid Data", "Data Exception"}, status=400)
        