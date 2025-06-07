class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        print(f"{self.name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.name} is now open!")

    def set_number_served(self, number_served):
        self.number_served = number_served
        print(f"{self.name} has served {self.number_served} customers.")

    def increment_number_served(self, increment):
        self.number_served += increment
        print(f"{self.name} has served {self.number_served} customers.")
    