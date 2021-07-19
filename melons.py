"""Classes for melon orders."""

class AbstractMelonOrder():
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

        if self.species == "christmas" or self.species == "Christmas":
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == "international" and self.qty < 10:
            total += 3

        return total


    def mark_shipped(self):
        """Record the fact than an order has been shipped.

        Arguments:
            None

        Return:
            None
        """

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA.

    Inherits attributes and methods from AbstractMelonOrder.
    """

    def __init__(self, species, qty):
        super().__init__(species, qty, "domestic", 0.08)
        """Initialize domestic melon order attributes."""


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order.

    Inherits attributes and methods from AbstractMelonOrder.
    """

    def __init__(self, species, qty, country_code):
        super().__init__(species, qty, "international", 0.17)
        """Initialize international melon order attributes."""

        self.country_code = country_code


    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    """A melon order made by the US government.

    Inherits attributes and methods from AbstractMelonOrder.
    """

    def __init__(self, species, qty):
        super().__init__(self, species, qty, 'government', 0.0)
        """Initialize government melon order attributes."""

        self.passed_inspection = False

    def mark_inspection(self, passed):
        """Takes a Boolean inut and updates whether or not melon has passed inspection.

        Arguments:
            - Boolean value for whether or not melon has passed inspection.

        Return:
            None
        """

        self.passed_inspection = passed