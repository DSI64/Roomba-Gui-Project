from tkinter import *
from Robot import Robot
import keyboard

# Initialize the Robot instance
robot = Robot("COM5")

while True:

    def onPress(w):
        if w == keyboard.press_and_release(w):
            robot.driveDirect(b'\x05', b'\x05', b'\x06', b'\x06') # Moves Up
    
    def onRelease(w):
        if w == keyboard.release(w):
            robot.drive(b'\x00', b'\x00', b'\x00', b'\x00') # stops
    
     # Try this
    def move_robot(direction):
        #if not robot.serial_connection:
            #print("Robot not connected. Cannot move.")
            #return

        if direction == 'up':
            robot.driveDirect(b'\x05', b'\x05', b'\x06', b'\x06')  # Moves Up
        elif direction == 'down':
            robot.driveDirect(b'\x80', b'\x00', b'\x80', b'\x00')  # Moves Down
        elif direction == 'left':
            robot.driveDirect(b'\x00', b'\x80', b'\x80', b'\x00')  # Moves Left
        elif direction == 'right':
            robot.driveDirect(b'\x80', b'\x00', b'\x00', b'\x80')  # Moves Right        


    # Put on Song button

    # Bind keyboard commands using the keyboard module
    keyboard.on_press(lambda event: move_robot('up') if event.name in ['up', 'w'] else None)
    keyboard.on_press(lambda event: move_robot('down') if event.name in ['down', 's'] else None)
    keyboard.on_press(lambda event: move_robot('left') if event.name in ['left', 'a'] else None)
    keyboard.on_press(lambda event: move_robot('right') if event.name in ['right', 'd'] else None)
    keyboard.on_release(lambda event: stop_robot() if event.name in ['up', 'down', 'left', 'right',
                                                                  'w', 'a', 's', 'd'] else None)

    """
        if keyboard.press_and_release('s'):
        robot.drive(b'\x80', b'\x00', b'\x80', b'\x00') # Moves Down
    if keyboard.press_and_release('a'):
        robot.drive(b'\x00', b'\x80', b'\x80', b'\x00') # Moves Left
    if keyboard.press_and_release('d'):
        robot.drive(b'\x80', b'\x00', b'\x00', b'\x80') # Moves Right
    """  

    def set_led_color(color):
        if color == 'green':
            robot.leds(b'\x04', b'\x00', b'\xFF') # Green LED
        elif color == 'red':
            robot.leds(b'\x05', b'\xFF', b'\xFF') # Red LED
        elif color == 'yellow':
            robot.leds(b'\x06', b'\x15', b'\xFF') # Yellow LED
        elif color == 'orange':
            robot.leds(b'\x07', b'\x50', b'\xFF') # Orange LED


    # Starts the program and conncets to the iRobot
    def start_program():
        robot.start()

    # Quits the program and disconnects from the iRobot
    def quit_program():
        robot.onQuit()
        root.quit()

    def playing_song():
        robot.song()

    #def digit_led():
        #robot.digitLEDsASCII()


    # Body of program
    root = Tk()
    root.geometry("750x500")
    menu = Menu(root)
    menu.add_command(label="Start", command=start_program)
    menu.add_command(label="Quit", command=quit_program)
    root.config(menu=menu)

    # Remove everything from text to scroll.pack and see if it works
    text = Text(root, height=15, width=50, wrap=WORD)
    scroll = Scrollbar(root, command=text.yview)
    text.configure(yscrollcommand=scroll.set)
    text.pack(side=TOP, fill=BOTH, expand=True)
    scroll.pack(side=RIGHT, fill=Y)


    # Creates buttons used on GUI
    button_frame = Frame(root)
    button_frame.pack()

    # Button Definitons
    green_button = Button(button_frame, bg='lightgreen', text="         ", command=lambda: set_led_color('green'))
    green_button.grid(row=1, column=3)

    red_button = Button(button_frame, bg='red', text="         ", command=lambda: set_led_color('red'))
    red_button.grid(row=5, column=3)

    yellow_button = Button(button_frame, bg='yellow', text="         ", command=lambda: set_led_color('yellow'))
    yellow_button.grid(row=3, column=2)

    orange_button = Button(button_frame, bg='orange', text="         ", command=lambda: set_led_color('orange'))
    orange_button.grid(row=3, column=4, padx=10, pady=5)

    up_button = Button(button_frame, text="Move Up", command=lambda: move_robot('up'))
    up_button.grid(row=1, column=9)


    left_button = Button(button_frame, text="Move Left", command=lambda: move_robot('left'))
    left_button.grid(row=3, column=8)

    right_button = Button(button_frame, text="Move Right", command=lambda: move_robot('right'))
    right_button.grid(row=3, column=10)

    down_button = Button(button_frame, text="Move Down", command=lambda: move_robot('down'))
    down_button.grid(row=5, column=9)

    stop_button = Button(button_frame, text="Stop", command=robot.stop)
    stop_button.grid(row=1, column=13)

    boost_button = Button(button_frame, text="Boost")
    boost_button.grid(row=1, column=14)

    song_button = Button(button_frame, text="Play Song", command=playing_song)
    song_button.grid(row=1, column=15)

    # Bind keyboard commands
    #root.bind("<Key>", callbackKey)
    #root.bind("<KeyRelease>", callbackKey)

    # Execute main loop
    root.mainloop()




"""
While loop runs infinitely but will take in keyboard inputs
along with their combinations that are correct and on those inputs
it will pass that to the respective methods that direct the roomba
in that direction

"""

""""
def callbackKey(event):
        if event.type == "key":
            if event.keysym in ('Up', 'w', 'W'):
                robot.drive(b'\x00', b'\x80', b'\x00', b'\x80') # Moves Up
            elif event.keysym in ('Down', 's', 'S'):
                robot.drive(b'\x80', b'\x00', b'\x80', b'\x00') # Moves Down
            elif event.keysym in ('Left', 'a', 'A'):
                robot.drive(b'\x00', b'\x80', b'\x80', b'\x00') # Moves Left
            elif event.keysym in ('Right', 'd', 'D'):
                robot.drive(b'\x80', b'\x00', b'\x00', b'\x80') # Moves Right
        elif event.type == "keyrelease":
            robot.drive(b'\x00', b'\x00', b'\x00', b'\x00')
"""