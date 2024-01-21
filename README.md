# GHWT MIDI Drum Mapper

GHWT MIDI Drum Mapper is a tool that allows you to use your midi edrums on Guitar Hero World Tour without using a drum brain.

__Has only been tested on GHWT:DE__

> [!IMPORTANT] 
> You **MUST** download ViGEmBus driver or else the program will **NOT WORK**
> 
> https://github.com/nefarius/ViGEmBus

## Settings
|Setting|Description|
|-|-|
|Select MIDI Device|Selects which MIDI device will be read|
|Queue Inputs|Queues the inputs so that they're guaranteed to go through|
|FPS|The rate at which the virtual gamepad updates, the initial hit is always instant|
|Mappings|Bring up the mappings page, where you can assign MIDI numbers to each pad. Multiple MIDI numbers can be set by seperating each one with a comma and a space. Only Red/Yellow/Blue/Orange/Green/Kick take MIDI numbers, Up/Down/Left/Right/Start/Back take keyboard keys.|

## Features
- GUI with customizable options and mappings
- Map keyboard keys to navigation buttons (Up/Down/Left/Right, Start/Back)
- Multiple midi notes on one pad
- Velocity support

## TODO
- Implement Quick Setup for mappings
- Allow for mapping controller to navigation
- Persistent mappings/settings
