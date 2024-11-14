from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Comment
from .forms import CommentForm

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
    comments = book.comments.all()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.book = book
            comment.save()
            return redirect('book_detail', book_id=book.id)
    else:
        form = CommentForm()

    return render(request, 'book_detail.html', {'book': book, 'comments': comments, 'form': form})
