from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import generic

from .forms import Create
from .models import Product


# Create your views here.
class Index(generic.TemplateView):
    template_name = 'index.html'


class ProductList(generic.ListView):
    models = Product
    template_name = 'product_list.html'
    context_object_name = 'all_products'

    def get_queryset(self):
        return Product.objects.all()


class AboutUs(generic.TemplateView):
    template_name = 'about_us.html'


class Contact(generic.TemplateView):
    template_name = 'contact.html'


class Create(generic.CreateView):
    model = Product
    form_class = Create
    template_name = 'create.html'
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect('login')
        return super().dispatch(request, *args, **kwargs)



