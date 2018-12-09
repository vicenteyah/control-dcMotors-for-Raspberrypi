import curses
import time
import RPi.GPIO as GPIO
#Control por teclado para pi-Robot explorer
#establece el modo de numeracion y define los pines de salida
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
# pin para Pulse Width Modulation servo superior GPIO-22
GPIO.setup(15, GPIO.OUT)
GPIO.setup(29, GPIO.OUT)  # pin para pwm servo inferior GPIO-5

#abre la  curses window, apaga el eco del teclado en la pantalla
#activa instantáneamente la respuesta de la tecla sin esperar y utiliza valores especiales para las teclas del cursor
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

p = GPIO.PWM(15, 50)
p.start(7.5)
p2 = GPIO.PWM(29, 50)
p2.start(7.5)

#Funciones para mover los servos porta camara


def _servoup_():
    p.ChangeDutyCycle(6.5)
    time.sleep(0.5)
    return


def _servodown_():
    p.ChangeDutyCycle(10.5)
    time.sleep(0.5)
    return


def _servoleft_():
    p2.ChangeDutyCycle(6.5)
    time.sleep(0.5)
    return


def _servoright_():
    p2.ChangeDutyCycle(12.5)
    time.sleep(0.5)
    return

#funciones para acelerar el carro


def forward():
    GPIO.output(16, False)
    GPIO.output(18, True)
    GPIO.output(22, True)
    GPIO.output(33, True)
    GPIO.output(35, False)
    GPIO.output(37, True)
    return


def backward():
    GPIO.output(16, True)
    GPIO.output(18, False)
    GPIO.output(22, True)
    GPIO.output(33, False)
    GPIO.output(35, True)
    GPIO.output(37, True)
    return


def turnRight():
    GPIO.output(16, True)
    GPIO.output(18, False)
    GPIO.output(22, True)
    GPIO.output(33, True)
    GPIO.output(35, False)
    GPIO.output(37, True)
    return


def turnLeft():
    GPIO.output(16, False)
    GPIO.output(18, True)
    GPIO.output(22, True)
    GPIO.output(33, False)
    GPIO.output(35, True)
    GPIO.output(37, True)
    return


def Control():
    try:
        while True:
            char = screen.getch()
            if char == ord('q'):
                break
            elif char == curses.KEY_UP:
               forward()

            elif char == curses.KEY_DOWN:
                backward()

            elif char == curses.KEY_RIGHT:
                turnLeft()

            elif char == curses.KEY_LEFT:
                turnRight()

            elif char == ord('w'):
                _servoup_()

            elif char == ord('s'):
                _servodown_()

            elif char == ord('d'):
                _servoleft_()

            elif char == ord('a'):
                _servoright_()

            elif char == ord('-'):
                GPIO.output(16, False)
                GPIO.output(18, False)
                GPIO.output(22, False)
                GPIO.output(33, False)
                GPIO.output(35, False)
                GPIO.output(37, False)
    finally:
        curses.nocbreak()
        screen.keypad(0)
        curses.echo()
        curses.endwin()
        GPIO.cleanup()
        p.stop()
        p2.stop()


if __name__ == '__main__':

    Control()
