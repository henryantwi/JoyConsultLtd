from decimal import Decimal
from django.conf import settings
from shop.models import Product
from icecream import ic


class Cart:
    """
    A base Cart class, providing some default behaviors
    that can be inherited or overridden, as necessary.
    """
    
    def __init__(self, request):
        self.session = request.session
        ic("Session:", self.session)
        cart = self.session.get(settings.CART_SESSION_ID)
        if settings.CART_SESSION_ID not in request.session:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
            
    def add(self, product, qty):
        """
        Adding and updating the user's cart
        session data
        """
        product_id = str(product.id)

        if product_id in self.cart:
            self.cart[product_id]['qty'] = qty
        else:
            self.cart[product_id] = {
                'price': str(product.price),
                'qty': qty,
            }
            
        self.save()
        
    def __iter__(self):
        """
        Collect the product id in the session data to query the database
        and return products
        """
        product_ids = self.cart.keys()
        products = Product.products.filter(id__in=product_ids)
        cart = self.cart.copy()
        
        for product in products:
            cart[str(product.id)]['product'] = product
            
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item
        
    def __len__(self):
        """
        Get the cart data and count the qty of items
        """
        return sum(item['qty'] for item in self.cart.values())
    
    def get_subtotal_price(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.cart.values())
    
    def get_total_price(self):
        subtotal = sum(Decimal(item['price']) * item['qty'] for item in self.cart.values())

        if subtotal == 0:
            shipping = Decimal(0.00)
        else:
            # shipping = Decimal(11.50)
            shipping = Decimal(00.00)

        total = subtotal + Decimal(shipping)
        ic(total)
        return total
    
    
    def delete(self, product):
        """
        Delete item from session data
        """
        product_id = str(product)   
        
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
               
    def save(self):
        self.session.modified = True
        
    def clear(self):
        # Remove cart from session
        del self.session[settings.CART_SESSION_ID]
        # del self.session['skey']
        self.save()
        
    def update(self, product, qty):
        """
        Update values in session data
        """
        product_id = str(product)
        
        if product_id in self.cart:
            self.cart[product_id]['qty'] = qty
        self.save()

    def get_product_qty(self, product_id) -> int:
        """
        Retrieve the quantity of a specific product in the cart
        """
        product_id = str(product_id)
        if product_id in self.cart:
            return int(self.cart[product_id]['qty'])
        return 0  # Return 0 if the product is not in the cart
