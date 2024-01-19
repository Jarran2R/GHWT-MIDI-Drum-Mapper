from threading import Thread
import sys
import midi
import notes
import controller
import vars
import tkinter as tk
from tkinter import ttk
import mido
import vgamepad as vg

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
        print(vars.green)

    # Initialize
    mappings = tk.Toplevel()
    mappings.transient(root)
    mappings.title("Pad Mappings")
    mappings.geometry('480x360')
    mappings.resizable(False, False)
    mappings.iconbitmap('icon.ico')
    mappings.focus_set()
    root.wm_attributes('-disabled', True)

    red_entry = ttk.Entry(mappings, width=10)
    yellow_entry = ttk.Entry(mappings)
    blue_entry = ttk.Entry(mappings)
    orange_entry = ttk.Entry(mappings)
    green_entry = ttk.Entry(mappings)
    kick_entry = ttk.Entry(mappings)
    apply_button = ttk.Button(mappings, text="Apply", command=update_mappings)
    cancel_button = ttk.Button(mappings, text="Cancel", command=close_mappings)
    ok_button = ttk.Button(mappings, text="OK", command=lambda:[update_mappings(), close_mappings()])

    red_entry.insert(0, ', '.join(str(i) for i in list(vars.red)))
    yellow_entry.insert(0, ', '.join(str(i) for i in list(vars.yellow)))
    blue_entry.insert(0, ', '.join(str(i) for i in list(vars.blue)))
    orange_entry.insert(0, ', '.join(str(i) for i in list(vars.orange)))
    green_entry.insert(0, ', '.join(str(i) for i in list(vars.green)))
    kick_entry.insert(0, ', '.join(str(i) for i in list(vars.kick)))

    red_entry.grid(row=0, column=0, sticky='w')
    yellow_entry.grid(row=0, column=1, sticky='w')
    blue_entry.grid(row=1, column=0, sticky='w')
    orange_entry.grid(row=1, column=1, sticky='w')
    green_entry.grid(row=2, column=0, sticky='w')
    kick_entry.grid(row=2, column=1, sticky='w')
    apply_button.grid(row=3, column=0, sticky='e')
    cancel_button.grid(row=3, column=1, sticky='e')
    ok_button.grid(row=3, column=2, sticky='e')
    
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
ttk.Label(root,text="Select MIDI Device").grid(row=0, column=0, columnspan=3, sticky='s', pady=8)

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

# Resets everything and closes program
def close_program():
    sys.exit()

# Intercept X button and run close_program (to shutdown everything properly)
root.protocol('WM_DELETE_WINDOW', close_program)

# Start the tkinter loop
root.mainloop()