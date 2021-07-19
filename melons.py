"""Classes for melon orders."""

import random
import datetime

class TooManyMelonsError(ValueError):
    """Error to raise if too many melons have been ordered."""

    def __init__(self):
        """Initialize TooManyMelonsError using init methods from ValueError."""

        super().__init__("Melon order quantity exceeded 100.")


class AbstractMelonOrder():
    """An abstract base class that other Melon Order classes inherit from.

    Attributes:
        - species: a string describing what type of melon
        - qty: an integer describing the quantity of melons
    """

    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes."""

        self.species = species

        if qty > 100:
            raise TooManyMelonsError

        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax


    def get_base_price(self):
        """Calculates the base price of the order depending on whatever promotions
            might be occurring and what day and time of the week it is.

        Arguments:
            DateTime = a string representing the day of the week and time of the order

        Return:
            - a float representing the base price for the melon."""

        #Calculate base price based on splurge pricing (choose a random integer btwn 5 and 9
        # to compute base price)
        base_price = random.randint(5,9)

        #Calculate rush hour pricing by adding extra $4 to each melon ordered between
        #8am-11am M-F
        now = datetime.datetime.now()

        if now.hour >= 8 and now.hour <= 11 and now.weekday() < 5:
            base_price += 4

        return base_price


    def get_total(self):
        """Calculates the price of the order, including tax.

        Arguments:
            None

        Returns:
            - total: a float describing the total price
        """

        base_price = self.get_base_price()

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