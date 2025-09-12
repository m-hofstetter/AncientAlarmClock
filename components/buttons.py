from gpiozero import Button

BUTTONS = [
    Button(9, pull_up=False),
    Button(11, pull_up=False),
    Button(10, pull_up=False),
    Button(5, pull_up=False)
]

TOGGLE_SWITCHES = [
    Button(26, pull_up=False),
    Button(19, pull_up=False),
    Button(13, pull_up=False),
    Button(20, pull_up=False)
]
