"""Classes for melon orders."""

class AbstractMelonClass():
    """An abstract base class that other Melon Order classes inherit from.

    Attributes:
        - species: a string describing what type of melon
        - qty: an integer describing the quantity of melons
    """

    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax

    def get_total(self):
        """Calculates the price of the order, including tax.

        Arguments:
            None

        Returns:
            - total: a float describing the total price
        """

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        return total


    def mark_shipped(self):
        """Record the fact than an order has been shipped.

        Arguments:
            None

        Return:
            None
        """

        self.shipped = True


class DomesticMelonOrder(AbstractMelonClass):
    """A melon order within the USA.

    Inherits attributes and methods from AbstractMelonClass"""

    def __init__(self, species, qty):
        super().__init__(species, qty, "domestic", 0.08)


class InternationalMelonOrder(AbstractMelonClass):
    """An international (non-US) melon order.

    Inherits attributes and methods from AbstractMelonClass."""

    def __init__(self, species, qty, country_code):
        super().__init__(species, qty, "international", 0.17)
        """Initialize melon order attributes."""

        self.country_code = country_code


    def get_country_code(self):
        """Return the country code."""

        return self.country_code
