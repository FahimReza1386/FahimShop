from .Cart import Cart


def Carts(request):
    return {'Cart' : Cart(request)}