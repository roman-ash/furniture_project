from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(
        max_length=64,
        verbose_name='имя',
        unique=True,
    )
    description = models.TextField(
        verbose_name='описание',
        blank=True,
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    update = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=128,
        verbose_name='имя продукта'
    )
    image = models.ImageField(
        upload_to='products_images',
        blank=True
    )
    short_desc = models.CharField(
        max_length=60,
        verbose_name='краткое описание',
        blank=True
    )
    description = models.TextField(
        verbose_name='описание продукта',
        blank=True
    )
    price = models.DecimalField(
        max_digits=8,
        verbose_name='цена',
        decimal_places=2
    )
    quantity = models.PositiveIntegerField(
        verbose_name='количество на складе',
        default=0
    )

    def __str__(self):
        return f'{self.name} ({self.category.name})'


"""
    created = models.DateTimeField(    # !!OperationalError at/products/ no such column: furnitureapp_product.created
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )
    is_active = models.BooleanField(verbose_name='активна', default=True)

    class Meta:
        ordering = ['-updated']
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
"""
