from django.urls import path #path function
from . import views # . is shorthand for the current directory
from django.conf.urls.static import static
from django.conf import settings
# one urlpattern per line
urlpatterns = [
    path('', views.Homepage, name='index'),
    path('add/', views.Addnewgif, name='add_new_gif'),
    path('addcategory/', views.Addnewcategory, name='add_new_category'),
    path('category/<int:id>/', views.categorys, name='categorys'),
    path('categories/', views.categories, name='categories'),
    path('Specigif/<int:id>/', views.Spegif, name='Specigif'),
]
