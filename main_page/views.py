from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def about_me(request):
    return HttpResponse("Информация обо мне: Меня зовут Дастан, мне 15 лет, родился и живу в Бишкеке, увлекаюсь программированием и прохожу курс в Geeks на 4 месяце.")

def about_my_pets(request):
    pet_name = "Бобик"
    pet_image_url = "/bp4/media/bobik.jpeg"
    return HttpResponse(f"Мой питомец: {pet_name} <br><img src='{pet_image_url}' alt='Мой питомец'>")

def system_time(request):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse(f"Системное время: {current_time}")
