def total_import_cart(request):
    total = 0
    if request.user.is_authenticated:
        if 'cart' in request.session:
            for key, value in request.session['cart'].items():
                total = total + (float(value['price'])*value['cantidad'])
    return {'total_import_cart': total}


