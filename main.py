from threading import Thread
import sys
import midi
import notes
import nav
import vars
import tkinter as tk
from tkinter import ttk
import mido

# who needs classes lmao

def midi_callback(message):
    midi.midi_callback(message)
    Thread(target=notes.notes_callback).start()

# Updates the dropdown right before clicking
def update_dropdown():
    vars.midi_list = mido.get_input_names()
    select_midi['values'] = [x[:-2] for x in vars.midi_list]

# Updates the selected midi device whenever selected
def update_midi(event):
    vars.selected_midi = mido.get_input_names()[select_midi.current()]
    print(vars.selected_midi)
    events = []
    if vars.inport != ():
        vars.inport.close()
    print(vars.inport)
    vars.inport = mido.open_input(name=vars.selected_midi)
    vars.inport.callback = midi_callback
    print(vars.inport)

def update_fps():
    vars.fps = int(select_fps.get())
    print(vars.fps)

def update_queue_inputs():
    vars.queue_inputs = queue_inputs.get()
    print(vars.queue_inputs)

def open_mappings():
    def close_mappings():
        mappings.destroy()
        root.wm_attributes('-disabled', False)
        root.focus_force()
    
    def update_mappings():
        vars.green = {int(e) if e.isdigit() else e for e in green_entry.get().split(', ')}
        vars.red = {int(e) if e.isdigit() else e for e in red_entry.get().split(', ')}
        vars.yellow = {int(e) if e.isdigit() else e for e in yellow_entry.get().split(', ')}
        vars.blue = {int(e) if e.isdigit() else e for e in blue_entry.get().split(', ')}
        vars.orange = {int(e) if e.isdigit() else e for e in orange_entry.get().split(', ')}
        vars.kick = {int(e) if e.isdigit() else e for e in kick_entry.get().split(', ')}
        vars.up = {int(e) if e.isdigit() else e for e in up_entry.get().split(', ')}
        vars.down = {int(e) if e.isdigit() else e for e in down_entry.get().split(', ')}
        vars.left = {int(e) if e.isdigit() else e for e in left_entry.get().split(', ')}
        vars.right = {int(e) if e.isdigit() else e for e in right_entry.get().split(', ')}
        vars.start = {int(e) if e.isdigit() else e for e in start_entry.get().split(', ')}
        vars.back = {int(e) if e.isdigit() else e for e in back_entry.get().split(', ')}
        print(vars.up)

    # Initialize
    mappings = tk.Toplevel()
    mappings.transient(root)
    mappings.title("Pad Mappings")
    mappings.resizable(False, False)
    mappings.iconbitmap('icon.ico')
    mappings.focus_set()
    root.wm_attributes('-disabled', True)
    mappings.columnconfigure(0, weight=1, uniform=1)
    mappings.columnconfigure(1, weight=1, uniform=1)

    pads_frame = ttk.Frame(mappings)
    direction_frame = ttk.Frame(mappings)
    nav_frame = ttk.Frame(mappings)
    buttons_frame = ttk.Frame(mappings)

    pads_frame.grid(row=0, column=0, columnspan=2)
    direction_frame.grid(row=1, column=0)
    nav_frame.grid(row=1, column=1)
    buttons_frame.grid(row=2, column=0, columnspan=2, sticky='e', padx=4, pady=4)

    red_frame = ttk.Frame(pads_frame)
    yellow_frame = ttk.Frame(pads_frame)
    blue_frame = ttk.Frame(pads_frame)
    orange_frame = ttk.Frame(pads_frame)
    green_frame = ttk.Frame(pads_frame)
    kick_frame = ttk.Frame(pads_frame)
    up_frame = ttk.Frame(direction_frame)
    down_frame = ttk.Frame(direction_frame)
    left_frame = ttk.Frame(direction_frame)
    right_frame = ttk.Frame(direction_frame)
    start_frame = ttk.Frame(nav_frame)
    back_frame = ttk.Frame(nav_frame)

    ttk.Label(red_frame, text="Red").grid(row=0, column=0, sticky='s')
    ttk.Label(yellow_frame, text="Yellow").grid(row=0, column=0, sticky='s')
    ttk.Label(blue_frame, text="Blue").grid(row=0, column=0, sticky='s')
    ttk.Label(orange_frame, text="Orange").grid(row=0, column=0, sticky='s')
    ttk.Label(green_frame, text="Green").grid(row=0, column=0, sticky='s')
    ttk.Label(kick_frame, text="Kick").grid(row=0, column=0, sticky='s')
    ttk.Label(up_frame, text="Up").grid(row=0, column=0, sticky='s')
    ttk.Label(down_frame, text="Down").grid(row=0, column=0, sticky='s')
    ttk.Label(left_frame, text="Left").grid(row=0, column=0, sticky='s')
    ttk.Label(right_frame, text="Right").grid(row=0, column=0, sticky='s')
    ttk.Label(start_frame, text="Start").grid(row=0, column=0, sticky='s')
    ttk.Label(back_frame, text="Back").grid(row=0, column=0, sticky='s')

    red_entry = ttk.Entry(red_frame, width=10, justify='center')
    yellow_entry = ttk.Entry(yellow_frame, width=10, justify='center')
    blue_entry = ttk.Entry(blue_frame, width=10, justify='center')
    orange_entry = ttk.Entry(orange_frame, width=10, justify='center')
    green_entry = ttk.Entry(green_frame, width=10, justify='center')
    kick_entry = ttk.Entry(kick_frame, width=10, justify='center')
    up_entry = ttk.Entry(up_frame, width=5, justify='center')
    down_entry = ttk.Entry(down_frame, width=5, justify='center')
    left_entry = ttk.Entry(left_frame, width=5, justify='center')
    right_entry = ttk.Entry(right_frame, width=5, justify='center')
    start_entry = ttk.Entry(start_frame, width=5, justify='center')
    back_entry = ttk.Entry(back_frame, width=5, justify='center')

    apply_button = ttk.Button(buttons_frame, text="Apply", command=update_mappings)
    cancel_button = ttk.Button(buttons_frame, text="Cancel", command=close_mappings)
    ok_button = ttk.Button(buttons_frame, text="OK", command=lambda:[update_mappings(), close_mappings()])

    red_entry.grid(row=1, column=0, sticky='n')
    yellow_entry.grid(row=1, column=0, sticky='n')
    blue_entry.grid(row=1, column=0, sticky='n')
    orange_entry.grid(row=1, column=0, sticky='n')
    green_entry.grid(row=1, column=0, sticky='n')
    kick_entry.grid(row=1, column=0, sticky='n')
    up_entry.grid(row=1, column=0, sticky='n')
    down_entry.grid(row=1, column=0, sticky='n')
    left_entry.grid(row=1, column=0, sticky='n')
    right_entry.grid(row=1, column=0, sticky='n')
    start_entry.grid(row=1, column=0, sticky='n')
    back_entry.grid(row=1, column=0, sticky='n')

    red_entry.insert(0, ', '.join(str(i) for i in list(vars.red)))
    yellow_entry.insert(0, ', '.join(str(i) for i in list(vars.yellow)))
    blue_entry.insert(0, ', '.join(str(i) for i in list(vars.blue)))
    orange_entry.insert(0, ', '.join(str(i) for i in list(vars.orange)))
    green_entry.insert(0, ', '.join(str(i) for i in list(vars.green)))
    kick_entry.insert(0, ', '.join(str(i) for i in list(vars.kick)))
    up_entry.insert(0, ', '.join(str(i) for i in list(vars.up)))
    down_entry.insert(0, ', '.join(str(i) for i in list(vars.down)))
    left_entry.insert(0, ', '.join(str(i) for i in list(vars.left)))
    right_entry.insert(0, ', '.join(str(i) for i in list(vars.right)))
    start_entry.insert(0, ', '.join(str(i) for i in list(vars.start)))
    back_entry.insert(0, ', '.join(str(i) for i in list(vars.back)))

    red_frame.grid(row=0, column=0, padx=8, pady=4)
    yellow_frame.grid(row=0, column=1)
    blue_frame.grid(row=0, column=2, padx=8, pady=4)
    orange_frame.grid(row=0, column=3)
    green_frame.grid(row=0, column=4, padx=8, pady=4)
    kick_frame.grid(row=1, column=2)
    up_frame.grid(row=0, column=1, padx=4)
    down_frame.grid(row=2, column=1, padx=4)
    left_frame.grid(row=1, column=0, padx=4, pady=4)
    right_frame.grid(row=1, column=2, padx=4, pady=4)
    start_frame.grid(row=0, column=1, padx=8)
    back_frame.grid(row=0, column=0, padx=8)

    ok_button.grid(row=0, column=0, padx=4, pady=4)
    cancel_button.grid(row=0, column=1)
    apply_button.grid(row=0, column=2, padx=4, pady=4)
    
    mappings.protocol('WM_DELETE_WINDOW', close_mappings)

# Initialize
root = tk.Tk()
root.title("GHWT MIDI Drum Mapper")
root.resizable(False, False)
root.iconbitmap('icon.ico')
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
queue_inputs = tk.BooleanVar(value=vars.queue_inputs)

# Create Label
ttk.Label(root,text="Select MIDI Device").grid(row=0, column=0, columnspan=3, pady=(4, 0))

# Create the dropdown menu, postcommand is triggered whenever opening the dropdown menu
select_midi = ttk.Combobox(root, state='readonly', width=50, justify='center', postcommand=update_dropdown)
select_midi.bind('<<ComboboxSelected>>', update_midi)
select_midi.grid(row=1, column=0, columnspan=3, padx=8)

select_fps_frame = ttk.Frame(root)
select_fps_frame.grid(row=2, column=0, sticky='w', padx=8, pady=8)

ttk.Label(select_fps_frame, text="FPS: ").grid(row=0, column=0, sticky='w')

select_fps = ttk.Spinbox(select_fps_frame, from_=1, to=999, width=4, justify='left', command=update_fps)
select_fps.set(60)
select_fps.bind('write',update_fps)
select_fps.grid(row=0, column=1, sticky='w')

select_queue_inputs = ttk.Checkbutton(root, text="Queue Inputs", variable=queue_inputs, command=update_queue_inputs)
select_queue_inputs.grid(row=2, column=1)

mappings_button = ttk.Button(root, text="Mappings", command=open_mappings)
mappings_button.grid(row=2, column=2, sticky='e', padx=8, pady=8)

# Saves everything and closes program
def close_program():
    sys.exit()

# Intercept X button and run close_program (to shutdown everything properly)
root.protocol('WM_DELETE_WINDOW', close_program)

# Start the tkinter loop
root.mainloop()