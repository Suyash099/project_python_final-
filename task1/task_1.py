# Ask the user Y or N and keep asking until they give a right answer
def get_yes_no_input(prompt):
    """
    Ask the user a yes/no question until a valid response is given.

    Parameters:
    prompt (str): The question to ask the user.

    Returns:
    str: 'y' for yes, 'n' for no.
    """
    while True:
        answer = input(prompt).lower()
        if answer == 'y' or answer == 'n':
            return answer
        else:
            print("Type 'Y' for Yes or 'N' for No, please!")

# Calculates the cost of pizzas with some discounts and conditions
def calculate_pizza_price(tuesday, num_pizzas, delivery, app):
    """
    Calculate the price of pizzas with possible discounts for Tuesday, delivery, and app usage.

    Parameters:
    tuesday (str): 'y' if it's Tuesday, otherwise 'n'.
    num_pizzas (int): The number of pizzas ordered.
    delivery (str): 'y' if delivery is required, otherwise 'n'.
    app (str): 'y' if the order was placed using the app, otherwise 'n'.

    Returns:
    float: The total price of the pizza order.
    """
    pizza_cost = 12
    delivery_fee = 2.5
    tuesday_discount = 0.5
    app_discount = 0.25

    price = num_pizzas * pizza_cost

    # Discount for Tuesday
    if tuesday == 'y':
        price -= price * tuesday_discount

    # Add delivery cost if needed
    if delivery == 'y' and num_pizzas < 5:
        price += delivery_fee

    # Discount for using the app
    if app == 'y':
        price -= price * app_discount

    return round(price, 2)

# Main program for calculating pizza prices
def main():
    """
    Main function to run the pizza price calculator program.
    Interacts with the user to get order details and calculate the price.
    """
    print("BPP Pizza Price Calculator")
    print( "=" * len("BPP Pizza Price Calculator"))

    while True:
        try:
            num_pizzas = int(input("\nHow many pizzas ordered?"))
            if num_pizzas <= 0:
                print("Enter a positive number, please!")
                continue

            delivery = get_yes_no_input("Is delivery required? (y/n) ")
            tuesday = get_yes_no_input("Is it Tuesday? (y/n) ")
            app = get_yes_no_input("Did the Customer use the app? (y/n) ")

            total = calculate_pizza_price(tuesday, num_pizzas, delivery, app)
            print(f"\nTotal to pay: Â£{total}")
            break

        except ValueError:
            print("Whoops, enter a number for the pizzas!")

if __name__ == "__main__":
    main()