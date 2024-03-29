# GHWT MIDI Drum Mapper

GHWT MIDI Drum Mapper is a tool that allows you to use your midi edrums on Guitar Hero World Tour: Definitive Edition without using a drum brain.

__Only works on GHWT:DE with input hack__

> [!IMPORTANT] 
> You **MUST** download ViGEmBus driver or else the program will **NOT WORK**
> 
> https://github.com/nefarius/ViGEmBus

## Features
- GUI with customizable settings and mappings
- Automatic saving/loading of settings and mappings
- Seperate settings/mappings for each MIDI device
- Unlimited MIDI notes on one pad
- Velocity support

## Settings
|Setting|Description|
|-|-|
|Select MIDI Device|Selects which MIDI device will be read|
|Queue Inputs|Queues the inputs so that they're guaranteed to go through|
|FPS|The rate at which the virtual gamepad updates, the initial hit is always instant|

*FPS should be set at or under the game's FPS, if the game's FPS drops below this value then the game WILL drop inputs*

## Mappings
The **Mappings** button brings up the mappings page where you can assign MIDI numbers to each pad

Multiple MIDI numbers can be inputted by seperating each one with a comma and a space

*Red/Yellow/Blue/Orange/Green/Kick* take MIDI numbers

*Up/Down/Left/Right/Start/Back* take keyboard keys

## Axis bindings (for velocity)
**L Thumb X** - None

**L Thumb Y** - Axis 1 (Inverted)

**R Thumb X** - Axis 2

**R Thumb Y** - Axis 3 (Inverted)
