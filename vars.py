import vgamepad as vg
selected_midi = ""
midi_list = []
inport = ()
fps = 60
queue_inputs = False
gamepad = vg.VX360Gamepad()

# MIDI numbers for each lane.
green = {}
red = {}
yellow = {}
blue = {}
orange = {}
kick = {}
up = {}
down = {}
left = {}
right = {}
start = {}
back = {}

# MIDI messages
green_messages = []
red_messages = []
yellow_messages = []
blue_messages = []
orange_messages = []
kick_messages = []

green_velocity = 0
red_velocity = 0
yellow_velocity = 0
blue_velocity = 0
orange_velocity = 0
kick_velocity = 0

green_active = False
red_active = False
yellow_active = False
blue_active = False
orange_active = False
kick_active = False