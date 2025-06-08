from restaurant import Restaurant

class IceCreamStand(Restaurant):
    """Represent aspects of a restaurant, specific to ice cream stands."""
    def __init__(self, name, cuisine_type='ice_cream'):
        """Initialize attributes of the parent class."""
        super().__init__(name, cuisine_type)
        self.__flavors = []
    
    def add_flavors(self, flavors: list) -> None:
        """Add flavors to the ice cream stand.
        
        Args:
            flavors: A list of flavors to add.
        """
        self.__flavors.extend(flavors)

    def show_flavors(self):
        """Display the flavors available."""
        print("\nWe have the following flavors available:")
        for flavor in self.__flavors:
            print(f"- {flavor.title()}")
    

my_ice_cream_stand = IceCreamStand('The Best Ice Cream Stand')
my_ice_cream_stand.describe_restaurant()
# Using the proper method to add flavors
my_ice_cream_stand.add_flavors(['vanilla', 'chocolate', 'black cherry'])
my_ice_cream_stand.show_flavors()