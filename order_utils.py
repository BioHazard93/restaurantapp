from base_model import Order, OrderAmount, OrderItem
from base_enum import OrderItemSize

class Printer:

    def print_order_info(self, restaurant, client, order, order_amount):
       self.__print_order_info_header(client)
       order_products = order.get_order_items()
       for order_product in order_products:
           self.__print_order_item_info(order_product)
       self.__print_order_info_footer(restaurant, order_amount)

    def __print_order_item_info(self, order_item):
        product = order_item.get_product()
        total_order_item_price = order_item.get_order_item_price() * order_item.get_quantity()

        print(str(order_item.get_quantity()) + " x | " + str(product.get_product_id()) + " . " + product.get_name() + 
             " | " + str(order_item.get_order_item_price()) + " | "  + str(total_order_item_price) + " Euro")
   
    def __print_order_info_header(self, client):
        print("--------------------------------------------")
        print("order from: "+str(client.get_name()) + ": ")
        print("Contact Number: " + str(client.get_phone()))
        print("=============================================")

    def __print_order_info_footer(self, restaurant, order_amount):
        print("=============================================")
        print("the total price of order is: ")
        print("SUB total: " +str(order_amount.get_total_order_amount())+ " Euro")
        print("VAT 18%: " + str(order_amount.get_total_order_amount_vat()) + " Euro")
        print("TOTAL: " + str(order_amount.get_total_order_amount_with_vat()) + " Euro")
        print("==============================================================")
        print(restaurant.get_name() + "in"+ restaurant.get_address())

   

class OrderCalculator:
    def calculate_total_order_amount(self, order):
        order_items = order.get_order_items()
        total_order_amount = 0.0
        for order_item in order_items:
            total_order_amount += self.calculate_order_item_price(order_item)

        return total_order_amount
    
    def calculate_order_item_price(self, order_item):
        size_rate_amount = self.get_size_rate_amount(order_item.get_order_item_size())
        
        product = order_item.get_product()
        total_order_item_price_single = product.get_price() * size_rate_amount
        order_item.set_order_item_price(total_order_item_price_single)

        return total_order_item_price_single * order_item.get_quantity()
    
    def get_size_rate_amount(self, order_item_size):
        match order_item_size:
            case OrderItemSize.SMALL:
                # 30% discount for small size
                return 0.7
            case OrderItemSize.MEDIUM:
                # standard price, no discount or additional amount(price stays the same)
                return 1
            case OrderItemSize.LARGE:
                # 20% in additioin for large size
                return 1.2
            case OrderItemSize.XXL:
                #25% in addition for extra large size
                return 1.25
            case _:
                print("no valid order item size" + order_item_size)
                return 1



    
    def calculate_total_order_amount_vat(self, total_order_amount):
        return total_order_amount * 18/100
    
    def calculate_order_amount(self, order):
        total_order_amount = self.calculate_total_order_amount(order)
        total_order_amount_vat = self.calculate_total_order_amount_vat(total_order_amount)
        total_order_amount_with_vat = total_order_amount + total_order_amount_vat
        order_amount = OrderAmount(total_order_amount, total_order_amount_vat, total_order_amount_with_vat)
        return order_amount
    



class OrderManager:

    def __init__(self):
        self.__orders = []

    def get_orders(self):
            return self.__orders


    def create_order(self, menu):

        order = Order()
       

        self.add_order_item(order, menu.get_menu_items().get(100), 1, OrderItemSize.XXL)
        self.add_order_item(order, menu.get_menu_items().get(101), 2, OrderItemSize.MEDIUM)
        self.add_order_item(order, menu.get_menu_items().get(200), 1, OrderItemSize.LARGE)
        self.add_order_item(order, menu.get_menu_items().get(201), 3, OrderItemSize.SMALL)

        return order
        
    def add_order_item(self, order, product, quantity, order_item_size):
        order_item = self.create_order_item(product, order_item_size, quantity)
        order.get_order_items().append(order_item)


    def create_order_item(self, product, order_item_size, quantity):
        order_item = OrderItem(product, order_item_size, quantity)
        return order_item


