def farenheit_conversion(temperature):
  '''calculates the fahrenheit temperature '''
  farenheit_temperature = temperature * 9 / 5 + 32
  farenheit_temperature = round(farenheit_temperature)
  return (f'{farenheit_temperature}')


def receive_details():
  city = input('enter your current city ')
  temperature = int(input('enter your temperature in degree celcius '))
  farenheit = farenheit_conversion(temperature)
  message = f'It is currently {temperature}ºC ({farenheit}ªF) in {city}.'
  print(message)


receive_details()
