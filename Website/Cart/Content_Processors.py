from .Cart import Cart


def Cart(request):

    return {'cart' : Cart(request)}