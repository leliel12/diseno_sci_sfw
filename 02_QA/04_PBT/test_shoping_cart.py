from hypothesis import given, strategies as st
from hypothesis.stateful import (
    RuleBasedStateMachine,
    rule,
    invariant,
    precondition,
)


class ShoppingCart:
    """
    A shopping cart for an e-commerce application.

    This class handles the logic for adding and removing items from the cart,
    as well as calculating the total cost of the purchase.

    Attributes
    ----------
    items : dict
        A dictionary storing the items in the cart.
        The key is the item name and the value is another dictionary
        with 'price' and 'quantity'.
    total : float
        The current total cost of all items in the cart.

    """

    def __init__(self):
        """
        Initialize an empty shopping cart.
        """
        self.items = {}
        self.total = 0

    def add_item(self, item, price, quantity):
        """
        Add an item to the cart or update its quantity if it already exists.

        Parameters
        ----------
        item : str
            The name of the item to add.
        price : float
            The unit price of the item.
        quantity : int
            The quantity of the item to add.

        Notes
        -----
        If the item already exists in the cart, its quantity will be increased.
        The cart total is automatically updated.
        """
        if item in self.items:
            self.items[item]["quantity"] += quantity
        else:
            self.items[item] = {"price": price, "quantity": quantity}
        self.total += price * quantity

    def remove_item(self, item, quantity):
        """
        Remove a specific quantity of an item from the cart.

        Parameters
        ----------
        item : str
            The name of the item to remove.
        quantity : int
            The quantity of the item to remove.

        Notes
        -----
        If the quantity to remove is greater than or equal to the quantity
        in the cart, the item will be completely removed.

        The cart total is automatically updated.

        """
        if item in self.items:
            if quantity >= self.items[item]["quantity"]:
                self.total -= (
                    self.items[item]["price"] * self.items[item]["quantity"]
                )
                del self.items[item]
            else:
                self.items[item]["quantity"] -= quantity
                self.total -= self.items[item]["price"] * quantity

    def get_total(self):
        """
        Get the current total cost of the cart.

        Returns
        -------
        float
            The total cost of all items in the cart.
        """
        return self.total

    def get_item_quantity(self, item):
        """
        Get the quantity of a specific item in the cart.

        Parameters
        ----------
        item : str
            The name of the item to query.

        Returns
        -------
        int
            The quantity of the item in the cart. Returns 0 if the item is
            not in the cart.

        """
        return self.items.get(item, {}).get("quantity", 0)


# ==============================================================================
# TEST
# ==============================================================================


class ShoppingCartStateMachine(RuleBasedStateMachine):
    """
    A state machine for testing the ShoppingCart class.

    This class defines rules and invariants for stateful testing of the
    ShoppingCart, using Hypothesis for property-based testing.

    Attributes
    ----------
    cart : ShoppingCart
        The shopping cart instance being tested.
    """

    def __init__(self):
        """
        Initialize the state machine with an empty shopping cart.
        """
        super().__init__()
        self.cart = ShoppingCart()

    @rule(
        item=st.text(),
        price=st.decimals(min_value=0.01, max_value=1000),
        quantity=st.integers(min_value=1, max_value=10),
    )
    def add_to_cart(self, item, price, quantity):
        """
        Rule for adding an item to the cart.

        Parameters
        ----------
        item : str
            The name of the item to add.
        price : float
            The price of the item.
        quantity : int
            The quantity of the item to add.
        """
        self.cart.add_item(item, price, quantity)

    @rule(item=st.text(), quantity=st.integers(min_value=1, max_value=10))
    @precondition(lambda self: bool(self.cart.items))
    def remove_from_cart(self, item, quantity):
        """
        Rule for removing an item from the cart.

        Parameters
        ----------
        item : str
            The name of the item to remove.
        quantity : int
            The quantity of the item to remove.

        Notes
        -----
        This rule only applies when the cart is not empty.
        """
        self.cart.remove_item(item, quantity)

    @rule(
        item=st.text(), new_price=st.decimals(min_value=0.01, max_value=1000)
    )
    @precondition(lambda self: bool(self.cart.items))
    def update_item_price(self, item, new_price):
        """
        Rule for updating the price of an item in the cart.

        Parameters
        ----------
        item : str
            The name of the item to update.
        new_price : float
            The new price for the item.

        Notes
        -----
        This rule only applies when the cart is not empty.
        """
        if item in self.cart.items:
            old_price = self.cart.items[item]["price"]
            quantity = self.cart.items[item]["quantity"]
            price_difference = new_price - old_price
            self.cart.total += price_difference * quantity
            self.cart.items[item]["price"] = new_price

    @invariant()
    def total_always_non_negative(self):
        """
        Invariant to ensure that the cart total is always non-negative.

        Raises
        ------
        AssertionError
            If the cart total becomes negative.
        """
        assert self.cart.get_total() >= 0, "Total should never be negative"

    @invariant()
    def total_matches_sum_of_items(self):
        """
        Invariant to ensure that the cart total matches the sum of item prices.

        Raises
        ------
        AssertionError
            If the cart total does not match the sum of item prices.
        """
        calculated_total = sum(
            item["price"] * item["quantity"]
            for item in self.cart.items.values()
        )
        assert (
            abs(self.cart.get_total() - calculated_total) < 0.01
        ), "Total should match sum of item prices"


TestShoppingCart = ShoppingCartStateMachine.TestCase
