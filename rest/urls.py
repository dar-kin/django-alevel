from rest_framework import routers
from .API.resources import BookViewSet, AuthorViewSet

router = routers.SimpleRouter()
router.register(r'books', BookViewSet)
router.register(r'authors', AuthorViewSet)
urlpatterns = router.urls