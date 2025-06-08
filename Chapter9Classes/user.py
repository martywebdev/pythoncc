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
        print(f"{self.first_name.title()} {self.last_name.title()} is {self.age} years old and lives in {self.location.title()}.")

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}!")

class Admin(User):
    """A simple attempt to model an admin."""
    def __init__(self, first_name, last_name, age, location):
        """Initialize attributes of the parent class."""
        super().__init__(first_name, last_name, age, location)
        self.privileges = Privileges(['can add post', 'can delete post', 'can ban user'])


class Privileges:
    """A simple attempt to model privileges."""
    def __init__(self, privileges):
        """Initialize privileges attribute."""
        self.privileges = privileges

    def show_privileges(self):
        """Print a list of privileges."""
        print("Admin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


admin = Admin('john', 'doe', 30, 'new york')
admin.describe_user()
admin.privileges.show_privileges()