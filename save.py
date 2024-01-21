import vars
from configparser import ConfigParser

def save_config():
    config = ConfigParser()
    selected_midi = vars.selected_midi[:-2]
    config.read('config.ini')
    if vars.selected_midi:
        if not selected_midi in config.sections():
            config.add_section(selected_midi)
        config[selected_midi]['fps'] = str(vars.fps)
        config[selected_midi]['queue_inputs'] = str(vars.queue_inputs)
        config[selected_midi]['red'] = ', '.join(str(i) for i in list(vars.red))
        config[selected_midi]['yellow'] = ', '.join(str(i) for i in list(vars.yellow))
        config[selected_midi]['blue'] = ', '.join(str(i) for i in list(vars.blue))
        config[selected_midi]['orange'] = ', '.join(str(i) for i in list(vars.orange))
        config[selected_midi]['green'] = ', '.join(str(i) for i in list(vars.green))
        config[selected_midi]['kick'] = ', '.join(str(i) for i in list(vars.kick))
        config[selected_midi]['up'] = ', '.join(str(i) for i in list(vars.up))
        config[selected_midi]['down'] = ', '.join(str(i) for i in list(vars.down))
        config[selected_midi]['left'] = ', '.join(str(i) for i in list(vars.left))
        config[selected_midi]['right'] = ', '.join(str(i) for i in list(vars.right))
        config[selected_midi]['start'] = ', '.join(str(i) for i in list(vars.start))
        config[selected_midi]['back'] = ', '.join(str(i) for i in list(vars.back))
        with open("config.ini", 'w') as cfgfile:
            config.write(cfgfile)

def load_config():
    config = ConfigParser()
    selected_midi = vars.selected_midi[:-2]
    config.read('config.ini')
    if selected_midi in config.sections():
        vars.fps = config[selected_midi].getint('fps') if config[selected_midi].getint('fps') else 60
        vars.queue_inputs = config[selected_midi].getboolean('queue_inputs') if config[selected_midi].getboolean('queue_inputs') else False
        vars.red = {int(e) if e.isdigit() else e for e in config[selected_midi]['red'].split(', ')} if config.has_option(selected_midi, 'red') else {}
        vars.yellow = {int(e) if e.isdigit() else e for e in config[selected_midi]['yellow'].split(', ')} if config.has_option(selected_midi, 'yellow') else {}
        vars.blue = {int(e) if e.isdigit() else e for e in config[selected_midi]['blue'].split(', ')} if config.has_option(selected_midi, 'blue') else {}
        vars.orange = {int(e) if e.isdigit() else e for e in config[selected_midi]['orange'].split(', ')} if config.has_option(selected_midi, 'orange') else {}
        vars.green = {int(e) if e.isdigit() else e for e in config[selected_midi]['green'].split(', ')} if config.has_option(selected_midi, 'green') else {}
        vars.kick = {int(e) if e.isdigit() else e for e in config[selected_midi]['kick'].split(', ')} if config.has_option(selected_midi, 'kick') else {}
        vars.up = {int(e) if e.isdigit() else e for e in config[selected_midi]['up'].split(', ')} if config.has_option(selected_midi, 'up') else {}
        vars.down = {int(e) if e.isdigit() else e for e in config[selected_midi]['down'].split(', ')} if config.has_option(selected_midi, 'down') else {}
        vars.left = {int(e) if e.isdigit() else e for e in config[selected_midi]['left'].split(', ')} if config.has_option(selected_midi, 'left') else {}
        vars.right = {int(e) if e.isdigit() else e for e in config[selected_midi]['right'].split(', ')} if config.has_option(selected_midi, 'right') else {}
        vars.start = {int(e) if e.isdigit() else e for e in config[selected_midi]['start'].split(', ')} if config.has_option(selected_midi, 'start') else {}
        vars.back = {int(e) if e.isdigit() else e for e in config[selected_midi]['back'].split(', ')} if config.has_option(selected_midi, 'back') else {}