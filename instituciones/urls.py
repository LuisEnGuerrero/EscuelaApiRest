from rest_framework.routers import DefaultRouter
from instituciones.views import InstitucionesViewSet


router = DefaultRouter()
router.register('instituciones', InstitucionesViewSet)

urlpatterns = router.urls