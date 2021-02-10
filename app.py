import pandas as pd


class Purchase(object):
    """ Abstraction of a purchase process """
    def __init__(self, shopping_cart, email_list):
        super(Purchase, self).__init__()
        """
        :param shopping_cart:
            * A pandas dataframe with columns for item name, quantity and price
        :param email_list:
            * A pandas dataframe with a single column of emails
        """
        self.shopping_cart = shopping_cart
        self.clients_cost = email_list
        self.cart_size = shopping_cart.size
        self.clients_size = email_list.size

    @property
    def empty_list(self):
        """
        Check if shopping_cart or email_list are empty
        :return:
            * True if there's at least one empty dataframe
        """
        if self.cart_size == 0 or self.clients_size == 0:
            return True
        return False

    @property
    def total_cost(self):
        """
        Iterates over the shopping cart rows and multiplies each item quantity by its price
        :return:
            * The shopping cart's total cost
        """
        total = 0
        for index, row in self.shopping_cart.iterrows():
            total += row[1] * row[2]
        return total

    def individual_cost(self):
        """
        Iterates over the shopping cart rows and multiplies each item quantity by its price
        :return:
            * A dict with client's email as key and it's individual cost as value
            * -1 in case of empty list as Purchase input
        """
        if self.empty_list:
            return -1

        # Divides the total cost by the number of clients
        cost_per_client = int(self.total_cost // self.clients_size)
        cost_remainder = int(self.total_cost % self.clients_size)

        # Adds the collumn COST to clients_cost dataframe with cost_per_client as each client cost
        self.clients_cost['COST'] = cost_per_client

        # Updates the individual cost by considering the remainder from total cost division
        self.clients_cost.loc[self.clients_size - cost_remainder:, 'COST'] = cost_per_client + 1

        # Returns a dict with email and costs in cents
        return self.clients_cost.set_index('CLIENT')['COST'].to_dict()


def main():
    # Read the shopping and email list from csv
    shopping_cart = pd.read_csv("shopping_list.csv", sep=';')
    email_list = pd.read_csv("email_list.csv")

    # Instantiate a new purchase object
    purchase = Purchase(shopping_cart, email_list)

    # If input is valid prints a dict with each client's cost
    if purchase.individual_cost() == -1:
        print("Invalid input: one or more list is empty")
    else:
        print(purchase.individual_cost())


if __name__ == '__main__':
    main()
