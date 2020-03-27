from django.contrib import admin
from .models import Client, GameType, Game

admin.site.site_header = "Administratoriaus skydelis"
admin.site.site_title = "Administratoriaus skydelis"
admin.site.index_title = "Pabėgimo kambarys"

admin.site.register(Client)
admin.site.register(GameType)
admin.site.register(Game)