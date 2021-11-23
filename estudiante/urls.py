from rest_framework.routers import DefaultRouter
from estudiante.views import EstudianteViewSet


router = DefaultRouter()
router.register('estudiantes', EstudianteViewSet)

urlpatterns = router.urls