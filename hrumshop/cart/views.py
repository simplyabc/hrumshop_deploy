from catalog.utils import DataMixin
from .models import Order, Cart
from catalog.models import Product
from django.views.generic import TemplateView, ListView, CreateView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import OrderAddForm


# cart добавляется перед id продукта, чтобы точно знать, что этот элемент сессии принадлежит корзине
def cart_add(request):
    data = request.POST
    request.session[f"cart_{data.get('id')}"] = data.get('quantity')
    return HttpResponse()


def product_cart_remove(request):
    data = request.POST
    del request.session[f"cart_{data.get('id')}"]
    return HttpResponse()


class OrderAdd(DataMixin, CreateView):
    form_class = OrderAddForm
    model = Order
    template_name = 'cart/order.html'
    success_url = 'order_accepted'

    def get_context_data(self, *, objects_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Оформление заказа'
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        instance = form.save()
        print(instance)
        cart_total_price = self.get_cart_price()['cart_total_price']
        Order.objects.filter(pk=instance.id).update(total_price=cart_total_price)
        cart_session = self.get_cart_session().items()
        for k, v in cart_session:
            Cart.objects.create(order=Order.objects.get(pk=instance.id),
                                product=Product.objects.get(pk=k),
                                quantity=v)
        return redirect(self.success_url)


class OrderAccepted(DataMixin, TemplateView):
    template_name = 'cart/order_accepted.html'

    def get_context_data(self, *, objects_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Заказ принят'
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))


class CartList(DataMixin, ListView):
    model = Product
    template_name = 'cart/cart.html'
    context_object_name = 'cart_products'

    def get_queryset(self):
        return Product.objects.filter(pk__in=list(self.get_cart_session().keys()))

    def get_context_data(self, *, objects_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Корзина'
        context['cart_session'] = self.get_cart_session()
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))


def cart_order(request):
    return render(request, 'cart/order.html', )
