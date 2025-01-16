from django.shortcuts import render

# Create your views here.
def platform(req):
    title = ' - Главная'
    main_page = 'Главная'
    shop = 'Магазин'
    cart = 'Корзина'
    context = {'title1': title,
               'main_page': main_page,
               'shop': shop,
               'cart': cart
    }
    return render(req, 'fourth_task/platform.html', context)

def shop_page(req):
    title = ' - Магазин'
    types = 'Пельмени'
    pelmeni = ['Сливочные 400 руб./кг', 'Хинкали 500 руб./кг', 'Вареники 450 руб./кг']
    buy = 'Купить.'
    back = 'Вернуться обратно'
    context = {'title2': title,
               'types': types,
               'pelmeni': pelmeni,
               'buy': buy,
               'back': back
    }
    return render(req, 'fourth_task/shop.html', context)

def cart_page(req):
    title = ' - Корзина'
    message = 'Ваша корзина пуста, а то что вы не можете в неё ничего положить уже не наши проблемы :3'
    back = 'Вернуться обратно'
    context = {'title3': title,
               'message': message,
               'back': back
    }
    return render(req, 'fourth_task/cart.html', context)