from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .models import Order
from .forms import OrderForm

def order_list(request):
    query = request.GET.get('q')  # Получаем значение из строки поиска
    if query:
        orders = Order.objects.filter(
            Q(name__icontains=query) |
            Q(phone_number__icontains=query) |
            Q(email__icontains=query) |
            Q(book__title__icontains=query)
        )
    else:
        orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders, 'query': query})

def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'order_form.html', {'form': form})

def order_update(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm(instance=order)
    return render(request, 'order_form.html', {'form': form})

def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('order_list')
    return render(request, 'order_confirm_delete.html', {'basket': order})
