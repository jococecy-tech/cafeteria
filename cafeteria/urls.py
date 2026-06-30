from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r"detallepedido", DetallePedidoViewSet)
router.register(r"cafeteria", CafeteriaViewSet)
router.register(r"categorias", CategoriaViewSet)
router.register(r"producto", ProductoViewSet)
router.register(r"usuarios", UsuariosViewSet)
router.register(r"roles", RolesViewSet)
router.register(r"pedido", PedidoViewSet)
router.register(r"pago", PagoViewSet)


urlpatterns= [path("api/", include(router.urls)),]