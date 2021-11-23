from rest_framework.routers import DefaultRouter
from materias.views import MateriasViewSet


router = DefaultRouter()
router.register('materias', MateriasViewSet)

urlpatterns = router.urls