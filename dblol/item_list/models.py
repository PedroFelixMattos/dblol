from django.db import models

# Create your models here.
class Item(models.Model):
        nome = models.CharField(max_length=64)
        ad = models.IntegerField(null= True)
        ap = models.IntegerField(null= True)
        ad_resist = models.IntegerField(null= True)
        ap_resist = models.IntegerField(null= True)
        atk_speed = models.FloatField(null= True)
        move_speed = models.IntegerField(null= True)
        crit = models.IntegerField(null= True)
        hability_haste = models.IntegerField(null= True)
        lethality = models.FloatField(null= True)
        tenacity = models.IntegerField(null= True)
        hp_regen = models.FloatField(null= True)
        mana_regen = models.FloatField(null= True)
        ad_pen = models.FloatField(null= True)
        ap_pen = models.FloatField(null= True)
        life_steal = models.FloatField(null= True)
        reach = models.FloatField(null= True)
        custo = models.IntegerField(null= False)
        imagem = models.CharField(max_length=300)