from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
# from .models import Order
# from .forms import OrderForm
from django.views import generic
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from MobileDevices.models import Device, Category
from MobileDevices.forms import DeviceForm


# Create your views here.

@method_decorator(cache_page(60 * 15), name='dispatch')
class DeviceListView(generic.ListView):
    template_name = 'device_list.html'
    context_object_name = 'device_list'
    model = Device
    form_class = DeviceForm
    def get_queryset(self):
        return self.model.objects.select_related().order_by('-id')

    def get_queryset(self):
        category_name = self.request.GET.get('category')
        if category_name:
            category = get_object_or_404(Category, name=category_name)
            return Device.objects.filter(category=category)
        return Device.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        return super().form_valid(form)

@method_decorator(cache_page(60 * 15), name='dispatch')
class DeviceDetailView(generic.DetailView):
    template_name = 'device_detail.html'
    context_object_name = 'device'
    model = Device
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        related_devices = Device.objects.filter(category=self.object.category).exclude(id=self.object.id)[:5]
        context['related_devices'] = related_devices
        return context













