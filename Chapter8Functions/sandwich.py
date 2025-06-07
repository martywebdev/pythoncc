import pizza

pizza.make_pizza(20, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


def sandwiches(*ingredients):
    print("Your sandwich will have the following ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")


sandwiches('ham', 'cheese', 'lettuce')

def user_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = user_profile('albert', 'einstein', location='princeton', field='physics')

print(user_profile)


def cars(manufacturer, model, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

car = cars('subaru', 'outback', color='blue', tow_package=True)
print(car)