from django.urls import path
from . import views

app_name = 'game_registration'
urlpatterns = [
    path('', views.index, name='index'),
    path('edit_game/<int:game_id>', views.edit_game, name='edit_game'),
    path('game_types', views.game_types, name='game_types'),
    path('edit_game_submit/<int:game_id>', views.edit_game_submit, name='edit_game_submit'),
    path('delete_game/<int:game_id>', views.delete_game, name='delete_game'),
    path('new_game', views.new_game, name='new_game'),
    path('new_game_submit', views.new_game_submit, name='new_game_submit'),
    path('game_types_edit/<int:game_type_id>', views.game_types_edit, name='game_types_edit'),
    path('game_types_new_submit', views.game_types_new_submit, name='game_types_new_submit'),
    path('game_types_delete/<int:game_type_id>', views.game_types_delete, name='game_types_delete')
]