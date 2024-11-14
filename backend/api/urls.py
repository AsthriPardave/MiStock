from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'usuarios', UsuarioViewSet)
router.register(r'productos', ProductosViewSet)
router.register(r'ventas', VentasViewSet)
router.register(r'boletas', BoletaViewSet)
router.register(r'pagos', PagoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]