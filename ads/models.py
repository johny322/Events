import datetime

from django.db import models

work_hours_choices = [
    ('Круглые сутки', 'Круглые сутки'),
    ('8-21', 'с 8:00 до 21:00'),
    ('21-8', 'с 21:00 до 8:00'),
]
persons_count_choices = [
    ('1', 'На одного'),
    ('2', 'На двоих'),
    ('3', 'На троих'),
    ('3+', 'Более трёх'),
]


class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название', null=True, blank=False)
    description = models.TextField(verbose_name='Описание', null=True, blank=False)
    start_date = models.DateTimeField(verbose_name='Начальная дата', null=True, blank=True)
    age = models.IntegerField(verbose_name='Возраст', default=0, null=True, blank=False)
    place = models.CharField(max_length=200, verbose_name='Тип места', null=True, blank=False)
    price = models.IntegerField(verbose_name='Цена', default=0, null=True, blank=False)
    area = models.CharField(max_length=100, verbose_name='Районы города', null=True, blank=False)
    card = models.BooleanField(verbose_name='Пушкинская карта', null=True, blank=False)
    time = models.CharField(max_length=200, choices=work_hours_choices, verbose_name='Время работы', null=True,
                            blank=False)
    temporary = models.BooleanField(verbose_name='Временные события', null=True, blank=False)

    people = models.CharField(max_length=100, verbose_name='Количество человек', null=True, blank=False)
    discount = models.BooleanField(verbose_name='Наличие акций', null=True, blank=False)
    image = models.ImageField(upload_to='photos', verbose_name='Фото', null=True, blank=False)
    latitude = models.FloatField(verbose_name='Широта', null=True, blank=True)
    longitude = models.FloatField(verbose_name='Долгота', null=True, blank=True)

    class Meta:
        verbose_name = 'Место посещения'
        verbose_name_plural = 'Места посещения'

    def __str__(self):
        return self.title

    @property
    def get_date_delta(self):
        if not self.start_date:
            return
        now = datetime.datetime.now()
        delta = self.start_date.replace(tzinfo=None) - now
        if delta.days < 0:
            return None
        return delta.days
