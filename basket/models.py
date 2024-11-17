from django.db import models
from main_page.models import Book

class Order(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя заказчика")
    phone_number = models.CharField(max_length=15, verbose_name="Телефон")
    email = models.EmailField(blank=True, null=True, verbose_name="Email")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="Книга")

    def __str__(self):
        return f"Заказ {self.name} - {self.book.title}"
