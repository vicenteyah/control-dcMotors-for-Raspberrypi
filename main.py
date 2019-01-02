from carControl import *

if __name__ == "__main__":
    try:
        Control()
    finally:
        curses.nocbreak()
        screen.keypad(0)
        curses.echo()
        curses.endwin()
        GPIO.cleanup()
        p.stop()
        p2.stop()
