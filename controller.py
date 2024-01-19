import inputs
import vars
import time
import vgamepad as vg
from threading import Thread

gamepad = vg.VX360Gamepad()
xbutton = vg.XUSB_BUTTON

def poll_controller():

    while True:
        keypress = inputs.get_key()
        if keypress.state == "UpArrow": # unfinished ima submit to github and work later
            gamepad.press_button(button=xbutton.XUSB_GAMEPAD_DPAD_UP)
            down_pressed = True
        else:
            gamepad.release_button(button=xbutton.XUSB_GAMEPAD_DPAD_UP)
            down_pressed = False
        time.sleep(60/vars.fps)

Thread(target=poll_controller, daemon=True).start()