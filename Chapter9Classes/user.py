class User:
    """A simple attempt to model a user."""
    def __init__(self, first_name, last_name, age, location):
        """Initialize first name, last name, age and location attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
    
    def describe_user(self):
        """Print a summary of the user's information."""
        print(f"{self.first_name} {self.last_name} is {self.age} years old and lives in {self.location.title()}.")

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"Hello, {self.first_name} {self.last_name}!")