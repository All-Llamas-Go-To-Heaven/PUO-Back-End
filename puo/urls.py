from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectSubmissionViewSet, PostViewSet, EndorseViewSet



router = DefaultRouter()
router.register(r'project_submissions', ProjectSubmissionViewSet, basename='project_submission')
router.register(r'posts', PostViewSet, basename='post')
router.register(r'endorsements', EndorseViewSet, basename='endorsement')
urlpatterns = router.urls
