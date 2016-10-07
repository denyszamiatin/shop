from django.db import models


class Cpu(models.Model):
    name = models.CharField(max_length=256)


class Good(models.Model):
    """

    """
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.FloatField(blank=True, null=True)
    ram = models.IntegerField()
    hdd = models.IntegerField()
    date = models.DateField()
    diagonal = models.FloatField()
    weight = models.FloatField()
    wifi = models.BooleanField()
    cpu = models.ForeignKey(Cpu)


class Image(models.Model):
    image = models.ImageField(upload_to='media')
    good = models.ForeignKey(Good)


class Tag(models.Model):
    name = models.CharField(max_length=256)
    good = models.ManyToManyField(Good)
