from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CreateUserView, AuthorViewSet, QuoteViewSet

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'quotes', QuoteViewSet)

urlpatterns = router.urls
urlpatterns += [
    path('register/', CreateUserView.as_view(), name='register'),
]
