from rest_framework import viewsets
from.models import *
from.serializers import *

class CafeteriaViewSet(viewsets.ModelViewSet):
    queryset= Cafeteria.objects.all()
    serializer_class= CafeteriaSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset= Categoria.objects.all()
    serializer_class= CategoriaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset= Producto.objects.select_related('id_categoria').all()
    serializer_class= ProductoSerializer

class RolesViewSet(viewsets.ModelViewSet):
    queryset= Roles.objects.all()
    serializer_class= RolesSerializer

class UsuariosViewSet(viewsets.ModelViewSet):
    queryset= Usuarios.objects.select_related('id_rol').all()
    serializer_class= UsuariosSerializer
    
class PedidoViewSet(viewsets.ModelViewSet):
    queryset= Pedido.objects.select_related('id_usuario').all()
    serializer_class= PedidoSerializer

class DetallePedidoViewSet(viewsets.ModelViewSet):
    queryset= DetallePedido.objects.select_related('id_pedido', 'id_producto').all()
    serializer_class= DetallePedidoSerializer

class PagoViewSet(viewsets.ModelViewSet):
    queryset= Pago.objects.select_related('id_pedido').all()
    serializer_class= PagoSerializer



