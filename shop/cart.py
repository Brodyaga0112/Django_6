from decimal import Decimal
from django.conf import settings
from .models import Car

class Cart:
    def __init__(self, request):
        """Инициализация корзины"""
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # Сохраняем пустую корзину в сессии
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, car):
        """Добавление автомобиля в корзину"""
        car_id = str(car.id)
        if car_id not in self.cart:
            self.cart[car_id] = {
                'price': str(car.price),
                'model': f"{car.model.brand.name} {car.model.name}",
                'vin': car.vin
            }
            self.save()

    def remove(self, car):
        """Удаление автомобиля из корзины"""
        car_id = str(car.id)
        if car_id in self.cart:
            del self.cart[car_id]
            self.save()

    def get_total_price(self):
        """Подсчет общей стоимости"""
        return sum(Decimal(item['price']) for item in self.cart.values())

    def clear(self):
        """Очистка корзины"""
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def save(self):
        """Сохранение изменений в сессии"""
        self.session.modified = True

    def __iter__(self):
        """Перебор элементов в корзине и получение автомобилей из базы данных"""
        car_ids = self.cart.keys()
        cars = Car.objects.filter(id__in=car_ids)
        cart = self.cart.copy()
        
        for car in cars:
            cart[str(car.id)]['car'] = car

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            yield item

    def __len__(self):
        """Подсчет всех товаров в корзине"""
        return len(self.cart) 