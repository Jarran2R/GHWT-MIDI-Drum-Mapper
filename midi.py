import vars

# I FINALLY GOT IT WORKING
def midi_callback(message):
    # Green
    if message.type == "note_on" and message.velocity > 0 and message.note in vars.green:
        vars.green_messages.append(message)
        print(vars.green_messages)
    
    # Red
    if message.type == "note_on" and message.velocity > 0 and message.note in vars.red:
        vars.red_messages.append(message)
        print(vars.red_messages)
    
    # Yellow
    if message.type == "note_on" and message.velocity > 0 and message.note in vars.yellow:
        vars.yellow_messages.append(message)
        print(vars.yellow_messages)
    
    # Blue
    if message.type == "note_on" and message.velocity > 0 and message.note in vars.blue:
        vars.blue_messages.append(message)
        print(vars.blue_messages)
    
    # Orange
    if message.type == "note_on" and message.velocity > 0 and message.note in vars.orange:
        vars.orange_messages.append(message)
        print(vars.orange_messages)
    
    # Kick
    if message.type == "note_on" and message.velocity > 0 and message.note in vars.kick:
        vars.kick_messages.append(message)
        print(vars.kick_messages)