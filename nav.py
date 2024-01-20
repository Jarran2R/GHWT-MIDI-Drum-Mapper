import vars
import time
import keyboard
from threading import Thread
import vgamepad as vg

gamepad = vars.gamepad
xbutton = vg.XUSB_BUTTON

def poll_navigation():
    while True:
        # Up
        if keyboard.get_hotkey_name().casefold() in vars.up and keyboard.get_hotkey_name():
            gamepad.press_button(button=xbutton.XUSB_GAMEPAD_DPAD_UP)
        else:
            gamepad.release_button(button=xbutton.XUSB_GAMEPAD_DPAD_UP)
        
        # Down
        if keyboard.get_hotkey_name().casefold() in vars.down and keyboard.get_hotkey_name():
            gamepad.press_button(button=xbutton.XUSB_GAMEPAD_DPAD_DOWN)
        else:
            gamepad.release_button(button=xbutton.XUSB_GAMEPAD_DPAD_DOWN)
        
        # Left
        if keyboard.get_hotkey_name().casefold() in vars.left and keyboard.get_hotkey_name():
            gamepad.press_button(button=xbutton.XUSB_GAMEPAD_DPAD_LEFT)
        else:
            gamepad.release_button(button=xbutton.XUSB_GAMEPAD_DPAD_LEFT)
        
        # Right
        if keyboard.get_hotkey_name().casefold() in vars.right and keyboard.get_hotkey_name():
            gamepad.press_button(button=xbutton.XUSB_GAMEPAD_DPAD_RIGHT)
        else:
            gamepad.release_button(button=xbutton.XUSB_GAMEPAD_DPAD_RIGHT)
        
        # Start
        if keyboard.get_hotkey_name().casefold() in vars.start and keyboard.get_hotkey_name():
            gamepad.press_button(button=xbutton.XUSB_GAMEPAD_START)
        else:
            gamepad.release_button(button=xbutton.XUSB_GAMEPAD_START)
        
        # Back
        if keyboard.get_hotkey_name().casefold() in vars.back and keyboard.get_hotkey_name():
            gamepad.press_button(button=xbutton.XUSB_GAMEPAD_BACK)
        else:
            gamepad.release_button(button=xbutton.XUSB_GAMEPAD_BACK)
        gamepad.update()
        time.sleep(1/vars.fps)

Thread(target=poll_navigation, daemon=True).start()