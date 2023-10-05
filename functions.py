import math

def math_results(number1, number2=math.pi):

  total = number1 + number2
  sorted_info = sorted([number1, number2])
  return total, sorted_info


def make_car(manufacturer, model, **user_info):
  user_info['manufacturer'] = manufacturer
  user_info['model'] = model
  return user_info

if __name__ == '__main__':

    print(math_results(10))
    print(math_results(10,5))

    car = make_car('subaru', 'outback', color='blue',
    tow_package=True)
    print(car)