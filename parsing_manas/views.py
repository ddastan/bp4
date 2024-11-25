from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from . import models, forms

class ManasListView(generic.ListView):
    template_name = 'manas/manas_list.html'
    context_object_name = 'manas'
    model = models.Manas

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')


class ManasFormView(generic.FormView):
    template_name = 'manas/manas_form.html'
    form_class = forms.ManasForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse('200 OK')
        else:
            return super(ManasFormView, self).post(request, *args, **kwargs)







