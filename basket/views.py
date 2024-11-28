from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .models import Order
from .forms import OrderForm
from django.views import generic
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

@method_decorator(cache_page(60 * 15), name='dispatch')
class OrderListView(generic.ListView):
    template_name = 'order_list.html'
    context_object_name = 'order_list'
    model = Order

    def get_queryset(self):
        return self.model.objects.select_related().order_by('-id')


class CreateOrderView(generic.CreateView):
    template_name = 'create_order.html'
    form_class = OrderForm
    success_url = '/order_class/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateOrderView, self).form_valid(form=form)


class UpdateOrderView(generic.UpdateView):
    template_name = 'update_order.html'
    form_class = OrderForm
    success_url = 'order_class/'


    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateOrderView, self).form_valid(form=form)

    def get_object(self, **kwargs):
        order_id = self.kwargs.get('id')
        return get_object_or_404(Order, id=order_id)

class DeleteOrderView(generic.DeleteView):
    template_name = 'confirm_delete.html'
    success_url = 'order_class/'

    def get_object(self, **kwargs):
        todo_id = self.kwargs.get('id')
        return get_object_or_404(Order, id=todo_id)
