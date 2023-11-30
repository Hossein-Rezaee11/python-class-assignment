class Fraction:
    def __init__(self, numerator, denominator):
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise ValueError("Numerator and denominator must be integers.")
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        result = Fraction(new_numerator, new_denominator)
        return result

    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        result = Fraction(new_numerator, new_denominator)
        return result

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        result = Fraction(new_numerator, new_denominator)
        return result

    def __truediv__(self, other):
        if other.numerator == 0:
            raise ValueError("Cannot divide by zero.")
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        result = Fraction(new_numerator, new_denominator)
    
        return result


# Example usage:
fraction1 = Fraction(1, 2)
fraction2 = Fraction(3, 4)

sum_fraction = fraction1 + fraction2
print(f"Sum: {sum_fraction}")

difference_fraction = fraction1 - fraction2
print(f"Difference: {difference_fraction}")

product_fraction = fraction1 * fraction2
print(f"Product: {product_fraction}")

quotient_fraction = fraction1 / fraction2
print(f"Quotient: {quotient_fraction}")

