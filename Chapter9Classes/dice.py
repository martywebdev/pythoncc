from random import randint

class Die:
    """A simple attempt to model a die."""
    def __init__(self, sides=6):
        """Initialize the die with a default of 6 sides."""
        self.sides = sides

    def roll_die(self):
        """Roll the die and print a random number between 1 and the number of sides."""
        return randint(1, self.sides)
    

    
# Create a 6-sided die and roll it 10 times
six_sided_die = Die()
print(six_sided_die.roll_die())

ten_sided_die = Die(10)
print(ten_sided_die.roll_die())