import mouse
import time
import keyboard

timeLength = 0.1

autoPressing = False
holdingDownKey = False

if __name__ == '__main__':
    while True:
        if (autoPressing):
            mouse.press()
            time.sleep(timeLength)
            mouse.release()

        if keyboard.is_pressed('ctrl+space') and not holdingDownKey:
            autoPressing = not autoPressing
            print(f'Autoclicker is {autoPressing}')
            holdingDownKey = True
        elif not keyboard.is_pressed('ctrl+space'):
            holdingDownKey = False

        if keyboard.is_pressed('ctrl+backspace'):
            break;