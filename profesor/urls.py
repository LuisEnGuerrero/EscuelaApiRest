from rest_framework.routers import DefaultRouter
from profesor.views import ProfesoresViewSet


router = DefaultRouter()
router.register('profesores', ProfesoresViewSet)

urlpatterns = router.urls