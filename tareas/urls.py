from rest_framework.routers import DefaultRouter
from tareas.views import TareasViewSet


router = DefaultRouter()
router.register('tareas', TareasViewSet)

urlpatterns = router.urls