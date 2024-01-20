import sys
import vars
import time
import vgamepad as vg

gamepad = vars.gamepad
gamepad.reset()
gamepad.update()
xbutton = vg.XUSB_BUTTON

def notes_callback():
    green_pressed = False # A
    red_pressed = False # B
    yellow_pressed = False # Y
    blue_pressed = False # X
    orange_pressed = False # RB
    kick_pressed = False # LB

    # Green
    if not vars.green_active:
        while vars.green_messages:
            vars.green_active = True
            if not green_pressed:
                gamepad.press_button(button=xbutton.XUSB_GAMEPAD_A)
                vars.green_velocity = vars.green_messages[0].velocity
                green_pressed = True
            else:
                gamepad.release_button(button=xbutton.XUSB_GAMEPAD_A)
                green_pressed = False
                if vars.queue_inputs:
                    del vars.green_messages[0]
                else:
                    vars.green_messages.clear()
            gamepad.left_joystick(x_value=0, y_value=vars.red_velocity * 256 + vars.green_velocity)
            gamepad.right_joystick(x_value=vars.blue_velocity * 256 + vars.yellow_velocity, y_value=vars.kick_velocity * 256 + vars.orange_velocity)
            gamepad.update()
            time.sleep(1/vars.fps)
        vars.green_active = False

    # Red
    if not vars.red_active:
        while vars.red_messages:
            vars.red_active = True
            if not red_pressed:
                gamepad.press_button(button=xbutton.XUSB_GAMEPAD_B)
                vars.red_velocity = vars.red_messages[0].velocity
                red_pressed = True
            else:
                gamepad.release_button(button=xbutton.XUSB_GAMEPAD_B)
                red_pressed = False
                if vars.queue_inputs:
                    del vars.red_messages[0]
                else:
                    vars.red_messages.clear()
            gamepad.left_joystick(x_value=0, y_value=vars.red_velocity * 256 + vars.green_velocity)
            gamepad.right_joystick(x_value=vars.blue_velocity * 256 + vars.yellow_velocity, y_value=vars.kick_velocity * 256 + vars.orange_velocity)
            gamepad.update()
            time.sleep(1/vars.fps)
        vars.red_active = False

    # Yellow
    if not vars.yellow_active:
        while vars.yellow_messages:
            vars.yellow_active = True
            if not yellow_pressed:
                gamepad.press_button(button=xbutton.XUSB_GAMEPAD_X)
                vars.yellow_velocity = vars.yellow_messages[0].velocity
                yellow_pressed = True
            else:
                gamepad.release_button(button=xbutton.XUSB_GAMEPAD_X)
                yellow_pressed = False
                if vars.queue_inputs:
                    del vars.yellow_messages[0]
                else:
                    vars.yellow_messages.clear()
            gamepad.left_joystick(x_value=0, y_value=vars.red_velocity * 256 + vars.green_velocity)
            gamepad.right_joystick(x_value=vars.blue_velocity * 256 + vars.yellow_velocity, y_value=vars.kick_velocity * 256 + vars.orange_velocity)
            gamepad.update()
            time.sleep(1/vars.fps)
        vars.yellow_active = False

    # Blue
    if not vars.blue_active:
        while vars.blue_messages:
            vars.blue_active = True
            if not blue_pressed:
                gamepad.press_button(button=xbutton.XUSB_GAMEPAD_Y)
                vars.blue_velocity = vars.blue_messages[0].velocity
                blue_pressed = True
            else:
                gamepad.release_button(button=xbutton.XUSB_GAMEPAD_Y)
                blue_pressed = False
                if vars.queue_inputs:
                    del vars.blue_messages[0]
                else:
                    vars.blue_messages.clear()
            gamepad.left_joystick(x_value=0, y_value=vars.red_velocity * 256 + vars.green_velocity)
            gamepad.right_joystick(x_value=vars.blue_velocity * 256 + vars.yellow_velocity, y_value=vars.kick_velocity * 256 + vars.orange_velocity)
            gamepad.update()
            time.sleep(1/vars.fps)
        vars.blue_active = False

    # Orange
    if not vars.orange_active:
        while vars.orange_messages:
            vars.orange_active = True
            if not orange_pressed:
                gamepad.press_button(button=xbutton.XUSB_GAMEPAD_RIGHT_SHOULDER)
                vars.orange_velocity = vars.orange_messages[0].velocity
                orange_pressed = True
            else:
                gamepad.release_button(button=xbutton.XUSB_GAMEPAD_RIGHT_SHOULDER)
                orange_pressed = False
                if vars.queue_inputs:
                    del vars.orange_messages[0]
                else:
                    vars.orange_messages.clear()
            gamepad.left_joystick(x_value=0, y_value=vars.red_velocity * 256 + vars.green_velocity)
            gamepad.right_joystick(x_value=vars.blue_velocity * 256 + vars.yellow_velocity, y_value=vars.kick_velocity * 256 + vars.orange_velocity)
            gamepad.update()
            time.sleep(1/vars.fps)
        vars.orange_active = False

    # Kick
    if not vars.kick_active:
        while vars.kick_messages:
            vars.kick_active = True
            if not kick_pressed:
                gamepad.press_button(button=xbutton.XUSB_GAMEPAD_LEFT_SHOULDER)
                vars.kick_velocity = vars.kick_messages[0].velocity
                kick_pressed = True
            else:
                gamepad.release_button(button=xbutton.XUSB_GAMEPAD_LEFT_SHOULDER)
                kick_pressed = False
                if vars.queue_inputs:
                    del vars.kick_messages[0]
                else:
                    vars.kick_messages.clear()
            gamepad.left_joystick(x_value=0, y_value=vars.red_velocity * 256 + vars.green_velocity)
            gamepad.right_joystick(x_value=vars.blue_velocity * 256 + vars.yellow_velocity, y_value=vars.kick_velocity * 256 + vars.orange_velocity)
            gamepad.update()
            time.sleep(1/vars.fps)
        vars.kick_active = False
    sys.exit()