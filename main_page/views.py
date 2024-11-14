from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render, get_object_or_404
from .models import Book

def about_me(request):
    return HttpResponse("Информация обо мне: Меня зовут Дастан, мне 15 лет, родился и живу в Бишкеке, увлекаюсь программированием и прохожу курс в Geeks на 4 месяце.")

def about_my_pets(request):
    pet_name = "Бобик"
    pet_image_url = "/bp4/media/bobik.jpeg"
    return HttpResponse(f"Мой питомец: {pet_name} <br><img src='{pet_image_url}' alt='Мой питомец'>")

def system_time(request):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse(f"Системное время: {current_time}")


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_detail.html', {'book': book})
