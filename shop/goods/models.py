from django.db import models


class ActiveCpu(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

    def activate(self):
        Cpu.objects.update(is_active=True)


class Cpu(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    active = ActiveCpu()
    objects = models.Manager()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        print('Cpu saved')
        super().save(*args, **kwargs)


class Good(models.Model):
    name = models.CharField('Имя', max_length=256)
    description = models.TextField()
    price = models.FloatField(blank=True, null=True)
    ram = models.IntegerField()
    hdd = models.IntegerField()
    date = models.DateField()
    diagonal = models.FloatField()
    weight = models.FloatField()
    wifi = models.BooleanField()
    cpu = models.ForeignKey(Cpu, verbose_name='Процессор')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def get_rate(self):
        return self.ram + self.hdd


class Image(models.Model):
    image = models.ImageField(upload_to='media')
    good = models.ForeignKey(Good)


class Tag(models.Model):
    name = models.CharField(max_length=256)
    good = models.ManyToManyField(Good)


class Comment(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=200)
    text = models.TextField()
    good = models.ForeignKey(Good)