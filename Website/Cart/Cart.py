from Store.models import Product , Profile

class Cart:
    def __init__(self , request):
        self.session = request.session
        self.request = request
        cart = self.session.get('session_key')

        # If  The User the New , No Session Key! I Create the session

        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # I am writing this so that it is all over the website
        self.cart = cart

    def Add(self , product , quantity):
        product_id = str(product.id)
        product_qty = str(quantity)

        #Logic
        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {'price ' : str(product.price)}
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            carty = str(self.cart)
            carty = carty.replace("\'" , "\"")
            current_user.update(old_cart=str(carty))


    def db_Add(self , product , quantity):
        product_id = str(product)
        product_qty = str(quantity)

        #Logic
        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {'price ' : str(product.price)}
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

        # Deal with logged in user
        if self.request.user.is_authenticated:
            # Get Current The User Profile
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            # Convert {{ '2' : 2 }} to {{ '4' : 5 }}
            carty = str(self.cart)
            carty = carty.replace("\'" , "\"")

            # Save Carty To the profile Model
            current_user.update(old_cart=str(carty))

    def __len__(self):
        return len(self.cart)

    def get_prods(self):
        #Get ids From Carts
        product_ids = self.cart.keys()
        # Search Product in DataBase
        product = Product.objects.filter(id__in = product_ids)

        # Return product the my Products
        return product

    def get_qty(self):
        qty = self.cart
        return qty


    def Update(self, product_id , quantity):
        # Get id product and qty product
        product_id = str(product_id)
        product_qty = int(quantity)

        # Get Cart
        ourcart = self.cart

        # Update Dictionary / Cart
        ourcart[product_id] = product_qty

        self.session.modified = True

        thing = self.cart

        # Deal with logged in user
        if self.request.user.is_authenticated:
            # Get Current The User Profile
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            # Convert {{ '2' : 2 }} to {{ '4' : 5 }}
            carty = str(self.cart)
            carty = carty.replace("\'" , "\"")

            # Save Carty To the profile Model
            current_user.update(old_cart=str(carty))

    def Delete(self , product_id):
        product_id = str(product_id)

        if product_id in self.cart:
            del self.cart[product_id]
        else:
            pass

        self.session.modified = True

        # Deal with logged in user
        if self.request.user.is_authenticated:
            # Get Current The User Profile
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            # Convert {{ '2' : 2 }} to {{ '4' : 5 }}
            carty = str(self.cart)
            carty = carty.replace("\'" , "\"")

            # Save Carty To the profile Model
            current_user.update(old_cart=str(carty))

    def cart_total(self):
        #Get product Ids
        product_ids = self.cart.keys()

        # Get product ib database
        products = Product.objects.filter(id__in = product_ids)

        # Get Quantitys
        qty = self.cart

        # Start counting at 0
        total = 0
        for key , val in qty.items():
            key = int(key)
            for product in products:
                if product.id == key:
                    if product.is_sale == True :
                        total = total + (product.sale_price * val)
                    else:
                        total = total + (product.price * val)

        return total




