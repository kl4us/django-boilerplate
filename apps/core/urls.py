from django.urls import path
from .views import IndexView

app_name = 'core' # Namespace per usare {% url 'core:index' %}

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]