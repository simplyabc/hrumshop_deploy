from .models import Category, Product
from django.views.generic import View

toolbar = [
    #{'name': 'Главная', 'url_name': 'main', 'src': ''},
    {'name': 'Доставка', 'url_name': 'transport', 'src': '../../static/catalog/images/transport.png'},
    {'name': 'Корзина', 'url_name': 'cart', 'src': '../../static/catalog/images/cart.png'},
]


class DataMixin(View):
    def get_cart_session(self):
        return {int(k[5:]): int(v) for k, v in self.request.session.items() if 'cart' in k}

    def get_dynamic_data(self):
        cart_id = []
        cart_price = []
        for k, v in self.get_cart_session().items():
                cart_id.append(str(k))
                cart_price.append(str(v*Product.objects.get(pk=k).price))
        return {'cart_id': ' '.join(cart_id),
                'cart_price': ' '.join(cart_price),
                'cart_total_price': sum([float(i) for i in cart_price]),
                }

    def get_user_context(self, **kwargs):
        dynamic_data = self.get_dynamic_data()
        context = kwargs
        context['toolbar'] = toolbar
        context['cats'] = Category.objects.all()

        context['cart_id'] = dynamic_data['cart_id']
        context['cart_price'] = dynamic_data['cart_price']
        context['cart_total_price'] = dynamic_data['cart_total_price']

        return context
