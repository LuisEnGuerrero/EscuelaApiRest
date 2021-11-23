from rest_framework.routers import DefaultRouter
from grupo.views import GrupoViewSet


router = DefaultRouter()
router.register('grupos', GrupoViewSet)

urlpatterns = router.urls