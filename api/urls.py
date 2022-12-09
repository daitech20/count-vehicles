from django.urls import path
from .views import FileInputViewSet

urlpatterns = [
    path('api/count-vehicles', FileInputViewSet.as_view()),
]