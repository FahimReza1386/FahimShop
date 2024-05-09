

class Cart:
    def __init__(self , request):
        self.session = request.session

        Cart = self.session.get('session_key')

        # If  The User the New , No Session Key! I Create the session

        if 'session_key' not in request.session:
            Cart = self.session['session_key'] = {}

        # I am writing this so that it is all over the website

        self.Cart = Cart

    def Add(self , product):
        product_id = str(product.id)

        #Logic
        if product_id in self.Cart:
            pass
        else:
            self.Cart[product_id] = {'price ' : str(product.price)}

        self.session.modified = True
