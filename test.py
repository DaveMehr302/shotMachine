import tkinter as tk
import gpiod
import time

VALVE_1_GPIO_PIN = 16
VALVE_2_GPIO_PIN = 20
VALVE_3_GPIO_PIN = 21

chip = gpiod.Chip('gpiochip4')

valve1 = chip.get_line(VALVE_1_GPIO_PIN)
valve2 = chip.get_line(VALVE_2_GPIO_PIN)
valve3 = chip.get_line(VALVE_3_GPIO_PIN)

valve1.request(consumer="VALVE_1", type=gpiod.LINE_REQ_DIR_OUT)
valve2.request(consumer="VALVE_2", type=gpiod.LINE_REQ_DIR_OUT)
valve3.request(consumer="VALVE_3", type=gpiod.LINE_REQ_DIR_OUT)

window = tk.Tk()
window.title("SPATENT shotMachine")

window.columnconfigure(3, weight=1, minsize=75)
window.rowconfigure(1, weight=1, minsize=50)

btn_v1_pressed = False
btn_v2_pressed = False
btn_v3_pressed = False

def btn_v1_handle_left_click(event):
    global btn_v1_pressed
    if(btn_v1_pressed):
        btn_v1_pressed = False
        btn_v1.configure(bg="black")
        valve1.set_value(0)
    else:
        btn_v1_pressed = True
        btn_v1.configure(bg="green")
        valve1.set_value(1)
        
def btn_v2_handle_left_click(event):
    global btn_v2_pressed
    if(btn_v2_pressed):
        btn_v2_pressed = False
        btn_v2.configure(bg="black")
        valve2.set_value(0)
    else:
        btn_v2_pressed = True
        btn_v2.configure(bg="green")
        valve2.set_value(1)
        
def btn_v3_handle_left_click(event):
    global btn_v3_pressed
    if(btn_v3_pressed):
        btn_v3_pressed = False
        btn_v3.configure(bg="black")
        valve3.set_value(0)
    else:
        btn_v3_pressed = True
        btn_v3.configure(bg="green")
        valve3.set_value(1)
    


frame = tk.Frame(
    bg="grey",
    master=window,
    relief=tk.RAISED,
    borderwidth=1
)
frame.grid(row=1, column=3, padx=5, pady=5)

btn_v1 = tk.Button(master=frame, text="Ventil 1", fg="white", bg="black", width=10, height=5)
btn_v1.pack(padx=5, pady=5, side=tk.LEFT)
btn_v1.bind('<Button-1>', btn_v1_handle_left_click)    
btn_v2 = tk.Button(master=frame, text="Ventil 2", fg="white", bg="black", width=10, height=5)
btn_v2.pack(padx=5, pady=5, side=tk.LEFT)
btn_v2.bind('<Button-1>', btn_v2_handle_left_click)    
btn_v3 = tk.Button(master=frame, text="Ventil 3", fg="white", bg="black", width=10, height=5)
btn_v3.pack(padx=5, pady=5, side=tk.LEFT)
btn_v3.bind('<Button-1>', btn_v3_handle_left_click)    
    

    


window.mainloop()

