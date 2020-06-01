from django.urls import path
from .views import index, by_category, BbCreateView

urlpatterns = [
    path('<int:category_id>/', by_category, name='by_category'),
    path('create/', BbCreateView.as_view(), name='create'),
    path('', index, name='index'),
]