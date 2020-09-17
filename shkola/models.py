from django.db import models

# Create your models here.

class NomeraUroka(models.Model):
    nomer_uroka = models.PositiveSmallIntegerField()

    def __str__(self):
          return str(self.nomer_uroka)

    class Meta:
        verbose_name = 'Номер Урока'
        verbose_name_plural = 'Номера Уроков'

class NomeraKlassa(models.Model):
    nomer_klassa = models.PositiveSmallIntegerField()

    def __str__(self):
          return str(self.nomer_klassa)

    class Meta:
        verbose_name = 'Номер Класса'
        verbose_name_plural = 'Номера Классов'

class Predmety(models.Model):
    nazvanie_predmeta = models.TextField(max_length=25)

    def __str__(self):
         return self.nazvanie_predmeta

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

class Prepodavately(models.Model):
    imya = models.TextField(max_length=50)
    otchestvo = models.TextField(max_length=50)
    familiya = models.TextField(max_length=50)

    def __str__(self):
         return self.imya + " " + self.otchestvo + " " + self.familiya

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'


class Uroki(models.Model):
    date_field = models.DateField(verbose_name = 'Дата')
    nomer_uroka = models.ForeignKey(NomeraUroka, on_delete=models.CASCADE, verbose_name = 'Номер урока')
    vremya_nachala_uroka = models.TextField(max_length=5, verbose_name = 'Время начала урока')
    nomer_klassa = models.ForeignKey(NomeraKlassa, on_delete=models.CASCADE, verbose_name = 'Номер класса')
    nazvanie_predmeta = models.ForeignKey(Predmety, on_delete=models.CASCADE, verbose_name = 'Название предмета')
    prepodavatel = models.ForeignKey(Prepodavately, on_delete=models.CASCADE, verbose_name = 'Преподаватель')
    tema_uroka = models.TextField(max_length=250, verbose_name = 'Тема Урок')
    ssylka_na_urok = models.TextField(max_length=10000, default="-", verbose_name = 'Ссылка на урок')
    kommentaryi = models.TextField(max_length=10000, verbose_name = 'Комментарий')

    def __str__(self):
        return str(self.date_field) + "    " + str(self.nazvanie_predmeta) + " " + str(self.nomer_klassa)

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'





