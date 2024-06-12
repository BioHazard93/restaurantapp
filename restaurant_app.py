from base_model import Restaurant, Client, Menu
from order_utils import Printer, OrderCalculator, OrderManager
from menu_utils import MenuPrinter

class RestaurantApp:
    def start(self, application_mode):
      match application_mode:
         case "ORDER":
            self.run_order_process()
         case "table_reservation": 
            self.run_table_reservation_process()
         case _:
            print("No valid application mode is selected")


    def run_order_process(self):

  #create an object of restaurant
      restaurant = Restaurant("Mc Donalds "," Schongau") #argumentet ndahen me , po kur ka stringje ata futen brenda "" dhe pastaj ndahen me ,
      


      #create a client object
      client = Client("Erandi ","+4951654645656")

      menu = Menu()
      menuprinter = MenuPrinter()
      menuprinter.print_menu(menu)

      order_manager = OrderManager()
      order = order_manager.create_order(menu)
      order_manager.get_orders().append(order)


      order_calculator = OrderCalculator()

      order_amount = order_calculator.calculate_order_amount(order)

      printer = Printer()
      printer.print_order_info(restaurant, client, order, order_amount)

    def run_table_reservation_process(self):
       print("table reservation is completed successfully")
restaurant_app = RestaurantApp()
restaurant_app.start("ORDER")