import RPi.GPIO as GPIO
import time

buzzer_pin = 16
led_pin = 21

notes = {
    'E7': 4500,
}

alarm = [
    notes['E7'], notes['E7'], 0, 0, 0, notes['E7'], notes['E7'],
    notes['E7'], notes['E7'], 0, 0, 0, notes['E7'], notes['E7'],
    notes['E7'], notes['E7'], 0, 0, 0, notes['E7'], notes['E7'],
    notes['E7'], notes['E7'], 0, 0, 0, notes['E7'], notes['E7'],
    notes['E7'], notes['E7'], 0, 0, 0, notes['E7'], notes['E7'],
    notes['E7'], notes['E7'], 0, 0, 0, notes['E7'], notes['E7'],
    notes['E7'], notes['E7'], 0, 0, 0, notes['E7'], notes['E7'],
    notes['E7'], notes['E7'], 0, 0, 0, notes['E7'], notes['E7'],
    notes['E7'], notes['E7'], 0, 0, 0, notes['E7'], notes['E7'],
    notes['E7'], notes['E7'], 0, 0, 0, notes['E7'], notes['E7'],
    notes['E7'], notes['E7'], 0, 0, 0, notes['E7'], notes['E7']
]
tempo = [
    12, 12, 12, 12, 12, 12, 12,
    12, 12, 12, 12, 12, 12, 12,
    12, 12, 12, 12, 12, 12, 12,
    12, 12, 12, 12, 12, 12, 12,
    12, 12, 12, 12, 12, 12, 12,
    12, 12, 12, 12, 12, 12, 12,
    12, 12, 12, 12, 12, 12, 12,
    12, 12, 12, 12, 12, 12, 12,
    12, 12, 12, 12, 12, 12, 12,
    12, 12, 12, 12, 12, 12, 12,
    12, 12, 12, 12, 12, 12, 12,
]

def buzz(frequency, length):
    if (frequency == 0):
        time.sleep(length)
        return
    period = 1.0 / frequency
    delayValue = period / 2
    numCycles = int(length * frequency)

    for i in range(numCycles):
        GPIO.output(buzzer_pin, True)
        time.sleep(delayValue)
        GPIO.output(buzzer_pin, False)
        time.sleep(delayValue)

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(buzzer_pin, GPIO.IN)
    GPIO.setup(buzzer_pin, GPIO.OUT)
    GPIO.setup(led_pin, GPIO.OUT)
    GPIO.output(led_pin, GPIO.HIGH)

def destroy():
    GPIO.cleanup()

def play(GPIO, tempo, pace=0.800):
    print ("INTRUDER ALERT!")
    for i in range(0, len(alarm)):

        noteDuration = pace / tempo[i]
        buzz(alarm[i], noteDuration)

        pauseBetweenNotes = noteDuration * 1.30
        time.sleep(pauseBetweenNotes)

if __name__ == '__main__':
    try:
        setup()
        play(alarm, tempo, 0.800)
        GPIO.output(led_pin, GPIO.LOW), destroy()
    except KeyboardInterrupt:
        GPIO.output(led_pin, GPIO.LOW), destroy()
