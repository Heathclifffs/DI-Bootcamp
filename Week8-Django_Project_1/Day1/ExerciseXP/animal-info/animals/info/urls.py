from django.urls import path
from . import views

urlpatterns = [
    path('family/<int:id>', views.family, name='family'),
    path('animal/<int:id>', views.animal, name='animal'),

]