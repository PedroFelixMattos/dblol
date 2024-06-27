from django.db import models

# Create your models here.
class Item(models.Model):
        nome = models.CharField(max_length=64)
        ad = models.IntegerField()
        ap = models.IntegerField()
        ad_resist = models.IntegerField()
        ap_resist = models.IntegerField()
        atk_speed = models.FloatField()
        move_speed = models.IntegerField()
        crit = models.IntegerField()
        hability_haste = models.IntegerField()
        lethality = models.FloatField()
        tenacity = models.IntegerField()
        hp_regen = models.FloatField()
        mana_regen = models.FloatField()
        ad_pen = models.FloatField()
        ap_pen = models.FloatField()
        life_steal = models.FloatField()
        reach = models.FloatField()
        custo = models.IntegerField()
        imagem = models.CharField(max_length=300)