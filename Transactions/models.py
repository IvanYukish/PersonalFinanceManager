from django.db import models
from Categories.models import Category


# Create your models here.
class TypeOperation(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None)

    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'Тип операції'
        verbose_name_plural = 'Типи операцій'

    def __str__(self):
        return "{0}".format(self.name)


class Transactions(models.Model):
    category = models.ForeignKey(Category, blank=True, null=True, default=None, on_delete=models.CASCADE)
    typeOper = models.ForeignKey(TypeOperation, blank=True, null=True, default=None, on_delete=models.CASCADE)
    suma = models.DecimalField(max_digits=10000, decimal_places=2, default=0)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    description = models.TextField(blank=True, null=True, default=None)



    class Meta:
        verbose_name = 'Транзакція'
        verbose_name_plural = 'Транзакції'

    def __str__(self):
        return "Category {0}".format(self.category)
