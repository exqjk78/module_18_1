from django.shortcuts import render

# Create your views here.
def platform(req):
    title = 'ГЛАВНАЯ СТРАНИЦА'
    main_page = 'Главная'
    shop = 'Магазин'
    cart = 'Корзина'
    context = {'title': title,
               'main_page': main_page,
               'shop': shop,
               'cart': cart
    }
    return render(req, 'third_task/platform.html', context)

def shop_page(req):
    title = 'Магазин Пельменей'
    types = 'Пельмени'
    type_1 = 'Сливочные 400 руб./кг'
    type_2 = 'Хинкали 500 руб./кг'
    type_3 = 'Вареники 450 руб./кг'
    buy = 'Купить.'
    back = 'Вернуться обратно'
    context = {'title': title,
               'types': types,
               'type1': type_1,
               'type2': type_2,
               'type3': type_3,
               'buy': buy,
               'back': back
    }
    return render(req, 'third_task/shop.html', context)

def cart_page(req):
    title = 'Корзина'
    message = 'Ваша корзина пуста, а то что вы не можете в неё ничего положить уже не наши проблемы :3'
    back = 'Вернуться обратно'
    context = {'title': title,
               'message': message,
               'back': back
    }
    return render(req, 'third_task/cart.html', context)