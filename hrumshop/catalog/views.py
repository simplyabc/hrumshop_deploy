from .utils import *
from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import redirect


def main(request):
    return redirect('category/lakomstva/')


class ProductsList(DataMixin, ListView):
    model = Product
    template_name = 'catalog/category.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, objects_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = Category.objects.get(slug=self.kwargs['slug'])
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))


class ProductDetail(DataMixin, DetailView):
    model = Product
    template_name = 'catalog/product.html'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))


class Transport(DataMixin, TemplateView):
    template_name = 'catalog/transport.html'

    def get_context_data(self, *, objects_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Доставка'
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))


class About(DataMixin, TemplateView):
    template_name = 'catalog/about.html'

    def get_context_data(self, *, objects_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'О нас'
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))



