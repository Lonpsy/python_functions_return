def farenheit_conversion(celcius_temperature):
  '''calculates the fahrenheit temperature '''
  farenheit_temperature = celcius_temperature * 9 / 5 + 32
  farenheit_temperature = round(farenheit_temperature)
  return (f'{farenheit_temperature}')


def message():
  farenheit = farenheit_conversion(temperature)
  message = f'It is currently {temperature}ºC ({farenheit}ªF) in {city}.'
  print(message)

city = input('enter your current city ')
temperature = int(input('enter your temperature in degree celcius '))
message()
