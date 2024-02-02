from django.urls import path
from webapp.views import perform_operation, index

urlpatterns = [
    path('', index, name='index'),
    path('add/', perform_operation, {'operation': 'add'}, name='add'),
    path('subtract/', perform_operation, {'operation': 'subtract'}, name='subtract'),
    path('multiply/', perform_operation, {'operation': 'multiply'}, name='multiply'),
    path('divide/', perform_operation, {'operation': 'divide'}, name='divide'),
]
