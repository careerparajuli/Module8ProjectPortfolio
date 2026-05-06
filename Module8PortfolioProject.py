class ItemToPurchase:

    # Constructor for item information
    def __init__(self, item_name="none", item_description="none",
                 item_price=0, item_quantity=0):

        self.item_name = item_name
        self.item_description = item_description
        self.item_price = item_price
        self.item_quantity = item_quantity

    # Printing item cost
    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity

        print(f"{self.item_name} {self.item_quantity} @ "
              f"${self.item_price:g} = ${total_cost:g}")

    # Printing item description
    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")


class ShoppingCart:

    # Constructor for shopping cart
    def __init__(self, customer_name="none",
                 current_date="January 1, 2020"):

        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    # Adding item to cart
    def add_item(self, item):
        self.cart_items.append(item)

    # Removing item from cart
    def remove_item(self, item_name):

        for item in self.cart_items:

            if item.item_name == item_name:
                self.cart_items.remove(item)
                return

        print("Item not found in cart. Nothing removed.")

    # Modifying item quantity, description, or price
    def modify_item(self, item_to_modify):

        for item in self.cart_items:

            if item.item_name == item_to_modify.item_name:

                if item_to_modify.item_description != "none":
                    item.item_description = item_to_modify.item_description

                if item_to_modify.item_price != 0:
                    item.item_price = item_to_modify.item_price

                if item_to_modify.item_quantity != 0:
                    item.item_quantity = item_to_modify.item_quantity

                return

        print("Item not found in cart. Nothing modified.")

    # Returning total number of items
    def get_num_items_in_cart(self):

        total_quantity = 0

        for item in self.cart_items:
            total_quantity += item.item_quantity

        return total_quantity

    # Returning total cart cost
    def get_cost_of_cart(self):

        total_cost = 0

        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity

        return total_cost

    # Printing shopping cart total
    def print_total(self):

        print(f"{self.customer_name}'s Shopping Cart - "
              f"{self.current_date}")

        print(f"Number of Items: {self.get_num_items_in_cart()}")

        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")

        else:
            for item in self.cart_items:
                item.print_item_cost()

        print(f"Total: ${self.get_cost_of_cart():g}")

    # Printing item descriptions
    def print_descriptions(self):

        print(f"{self.customer_name}'s Shopping Cart - "
              f"{self.current_date}")

        print("Item Descriptions")

        for item in self.cart_items:
            item.print_item_description()


# Displaying menu options
def print_menu(cart):

    option = ""

    while option != "q":

        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")

        option = input("\nChoose an option:\n")

        while option not in ["a", "r", "c", "i", "o", "q"]:
            option = input("Choose an option:\n")

        # Adding item option
        if option == "a":

            print("\nADD ITEM TO CART")

            name = input("Enter the item name:\n")
            description = input("Enter the item description:\n")
            price = float(input("Enter the item price:\n"))
            quantity = int(input("Enter the item quantity:\n"))

            item = ItemToPurchase(name, description,
                                  price, quantity)

            cart.add_item(item)

        # Removing item option
        elif option == "r":

            print("\nREMOVE ITEM FROM CART")

            name = input("Enter name of item to remove:\n")

            cart.remove_item(name)

        # Changing quantity option
        elif option == "c":

            print("\nCHANGE ITEM QUANTITY")

            name = input("Enter the item name:\n")
            quantity = int(input("Enter the new quantity:\n"))

            item = ItemToPurchase(item_name=name,
                                  item_quantity=quantity)

            cart.modify_item(item)

        # Outputing descriptions
        elif option == "i":

            print("\nOUTPUT ITEMS' DESCRIPTIONS")

            cart.print_descriptions()

        # Outputing shopping cart
        elif option == "o":

            print("\nOUTPUT SHOPPING CART")

            cart.print_total()


def main():

    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")

    print(f"\nCustomer name: {customer_name}")
    print(f"Today's date: {current_date}")

    # Creating shopping cart object
    cart = ShoppingCart(customer_name, current_date)

    print_menu(cart)


if __name__ == "__main__":
    main()