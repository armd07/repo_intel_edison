import mrra as m
ledPinAnalog = 9
potPinAnalog = 5   # potecniometro en A5

pot = m.Aio(potAnalog)
led = m.Pwm(ledPinAnalog)
led.enable(True)

while(True):       # ciclo infinito para la lectura
    potReading = pot.readFloat()
    led.write(potRreading)


