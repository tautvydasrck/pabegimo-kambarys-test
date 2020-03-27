from django.db import models
from pytz import timezone 

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    juridical = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class GameType(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    def __str__(self):
        return self.name

class Game(models.Model):
    date_time = models.DateTimeField()
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    game_type = models.ForeignKey(GameType, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.IntegerField()
    hall = models.BooleanField(default=False)
    def __str__(self):
        timezone_local = timezone('Europe/Vilnius')
        date_time_local = self.date_time.astimezone(timezone_local)
        return date_time_local.strftime("%Y-%m-%d %H:%M") + " " + str(self.client)