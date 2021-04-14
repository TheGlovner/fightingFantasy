"""
This file is used to conrtol the GUI for output/input control with the user
"""

import tkinter as tk
from PIL import Image, ImageTk


def renderWindow(window_data):

    # Create the window
    window = tk.Tk()

    # Create the text frame to house the scenario text
    text_frame = tk.Frame(
                         master=window,
                         relief=tk.RAISED,
                         borderwidth=5
                         )
    scenario_text = tk.Label(
                            master=text_frame,
                            text=window_data["ScenarioText"]
                            )
    scenario_text.pack(
                      side=tk.LEFT
                      )


    # Create the image frame to house the scenario image
    picture = ImageTk.PhotoImage(Image.open(window_data["ScenarioImage"]))
    image_frame = tk.Label(
      master=window,
      image=picture,
      relief=tk.RAISED,
      borderwidth=5
    )

    # Create the button frame to house the option buttons
    button_frame = tk.Frame(
                           master=window,
                           relief=tk.RAISED,
                           borderwidth=5
                           )

    if len(window_data["Button1"]) > 0:
        button1  = tk.Button(
                            master=button_frame,
                            text=window_data["Button1"],
                            width=10,
                            height=10,
                            )
        button1.pack(
                    side=tk.LEFT
                    )

    if len(window_data["Button2"]) > 0:
        button2 = tk.Button(
                           master=button_frame,
                           command=buttonClick2,
                           text=window_data["Button2"],
                           width=10,
                           height=10,
                           )
        button2.pack(
                    side=tk.LEFT
                    )


    text_frame.pack(side=tk.LEFT)
    image_frame.pack(side=tk.RIGHT)
    button_frame.pack(side=tk.BOTTOM)


    window.mainloop()


def buttonClick1():
    print('hello you clicked button 1')  # do here whatever you want


def buttonClick2():
  print('hello you clicked button 2')  # do here whatever you want
