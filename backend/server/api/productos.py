from rest_framework import serializers, viewsets
from server.models import Producto
from rest_framework import views

class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producto
        fields = ['nombre',
                  'codigo',
                  'precio'
                  ]


class ProductoView(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
