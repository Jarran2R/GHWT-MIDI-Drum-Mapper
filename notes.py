import sys
import vars
import time
import vgamepad as vg

gamepad = vg.VX360Gamepad()
gamepad.reset()
gamepad.update()
xbutton = vg.XUSB_BUTTON

def notes_callback():
    if not vars.notes_active:

        green_pressed = False # A
        red_pressed = False # B
        yellow_pressed = False # Y
        blue_pressed = False # X
        orange_pressed = False # RB
        kick_pressed = False # LB

        # Green
        while vars.green_messages or vars.red_messages or vars.yellow_messages or vars.blue_messages or vars.orange_messages or vars.kick_messages:
            vars.notes_active = True
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

            # Red
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

            # Yellow
            if vars.yellow_messages and not yellow_pressed:
                gamepad.press_button(button=xbutton.XUSB_GAMEPAD_X)
                vars.yellow_velocity = vars.yellow_messages[0].velocity
                yellow_pressed = True
            elif yellow_pressed:
                gamepad.release_button(button=xbutton.XUSB_GAMEPAD_X)
                yellow_pressed = False
                if vars.queue_inputs:
                    del vars.yellow_messages[0]
                else:
                    vars.yellow_messages.clear()

            # Blue
            if vars.blue_messages and not blue_pressed:
                gamepad.press_button(button=xbutton.XUSB_GAMEPAD_Y)
                vars.blue_velocity = vars.blue_messages[0].velocity
                blue_pressed = True
            elif blue_pressed:
                gamepad.release_button(button=xbutton.XUSB_GAMEPAD_Y)
                blue_pressed = False
                if vars.queue_inputs:
                    del vars.blue_messages[0]
                else:
                    vars.blue_messages.clear()

            # Orange
            if vars.orange_messages and not orange_pressed:
                gamepad.press_button(button=xbutton.XUSB_GAMEPAD_RIGHT_SHOULDER)
                vars.orange_velocity = vars.orange_messages[0].velocity
                orange_pressed = True
            elif orange_pressed:
                gamepad.release_button(button=xbutton.XUSB_GAMEPAD_RIGHT_SHOULDER)
                orange_pressed = False
                if vars.queue_inputs:
                    del vars.orange_messages[0]
                else:
                    vars.orange_messages.clear()

            # Kick
            if vars.kick_messages and not kick_pressed:
                gamepad.press_button(button=xbutton.XUSB_GAMEPAD_LEFT_SHOULDER)
                vars.kick_velocity = vars.kick_messages[0].velocity
                kick_pressed = True
            elif kick_pressed:
                gamepad.release_button(button=xbutton.XUSB_GAMEPAD_LEFT_SHOULDER)
                kick_pressed = False
                if vars.queue_inputs:
                    del vars.kick_messages[0]
                else:
                    vars.kick_messages.clear()
            
            # Set velocity and update
            gamepad.left_joystick(x_value=0, y_value=vars.red_velocity * 256 + vars.green_velocity)
            gamepad.right_joystick(x_value=vars.blue_velocity * 256 + vars.yellow_velocity, y_value=vars.kick_velocity * 256 + vars.orange_velocity)
            gamepad.update()
            time.sleep(1/vars.fps)
        vars.notes_active = False
    sys.exit()