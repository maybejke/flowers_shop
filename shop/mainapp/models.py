from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse

from django.utils.text import slugify
from time import time


# Create your models here.

ONE_HUNDERD_PERCENTS: int = 100


def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    time_slug = str(int(time()))
    return f'{new_slug}-{time_slug}'


class Product(models.Model):
    class Meta:
        ordering = ('title', 'pub_date')
        verbose_name = 'Продукт'
        verbose_name_plural = "Продукты"
        index_together = (('id', 'slug'),)

    title = models.CharField('Название', max_length=200, db_index=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True, db_index=True)
    description = models.TextField(blank=True, null=True)
    pub_date = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(
        'Category', verbose_name='Категории', blank=True, related_name='products')
    price = models.PositiveIntegerField(verbose_name='Цена за шт', default=0)
    main_page = models.BooleanField('На главную', default=False)
    special_price = models.BooleanField('Акция', default=False, blank=True, null=True)
    discount = models.PositiveIntegerField(verbose_name='Размер скидки',
                                           default=0,validators=[MinValueValidator(0), MaxValueValidator(100)],
                                           blank=True, null=True,
                                           help_text='Скидка указывается  в диапозоне от 0 до 100')

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})

    # цена продукта со скидкой для отображения на странице
    def discount_product(self):
        if self.discount != 0:
            self.price = (self.price * (1 / (self.discount / ONE_HUNDERD_PERCENTS)))
            return self.price
        else:
            return self.price




class Category(models.Model):
    class Meta:
        ordering = ('title',)
        verbose_name = 'Категория'
        verbose_name_plural = "Категории"

    title = models.CharField('Название', max_length=120)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})


class Picture(models.Model):
    class Meta:
        ordering = ('title',)
        verbose_name = 'Картинка'
        verbose_name_plural = "Картинки"

    title = models.CharField('Название', max_length=200, db_index=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='pictures')
    related_obj = models.ForeignKey(Product, verbose_name='pictures', null=True,
                                    blank=True, on_delete=models.CASCADE, related_name='pictures')

    def __str__(self):
        return f'{self.title}'


class ConnectUs(models.Model):
    class Meta:
        ordering = ('name', )
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'

    name = models.CharField('Имя', max_length=25)
    phone = models.CharField('Телефон', max_length=20)
    description = models.TextField('Сообщение', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'