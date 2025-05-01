from django.urls import path
from . import views

app_name = 'app_main'

urlpatterns = [
    path('', views.home, name='home'),
    path('add_author/', views.add_author, name='add_author'),
    path('author/<int:author_id>/', views.author, name='author'),
    path('add_quote/', views.add_quote, name='add_quote'),
    path('edit/<int:author_id>', views.edit, name='edit'),
    path('remove/<int:author_id>', views.remove, name='remove'),
]
