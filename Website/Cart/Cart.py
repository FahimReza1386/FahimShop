

class Cart:
    def __init__(self , request):
        self.session = request.session

        Cart = self.session.get('session_key')

        # If  The User the New , No Session Key! I Create the session

        if 'session_key' not in request.session:
            Cart = self.session['session_key'] = {}

        # I am writing this so that it is all over the website

        self.Cart = Cart
