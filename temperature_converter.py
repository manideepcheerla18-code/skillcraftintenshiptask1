import tkinter as tk
from tkinter import ttk


# =========================================================
# COLORS
# =========================================================

BG = "#F3F6FC"
WHITE = "#FFFFFF"
PRIMARY = "#4F46E5"
PRIMARY_DARK = "#3730A3"
BLUE = "#06B6D4"
GREEN = "#10B981"
RED = "#EF4444"
TEXT = "#1F2937"
GRAY = "#6B7280"
LIGHT_BLUE = "#E0E7FF"
LIGHT_RED = "#FEE2E2"


# =========================================================
# MAIN WINDOW
# =========================================================

root = tk.Tk()

root.title("TempX - Temperature Converter")

# Open maximized
try:
    root.state("zoomed")
except:
    root.geometry("900x750")

# Minimum size
root.minsize(650, 650)

root.configure(bg=BG)


# =========================================================
# COMBOBOX STYLE
# =========================================================

style = ttk.Style()

try:
    style.theme_use("clam")
except:
    pass

style.configure(
    "TCombobox",
    padding=7,
    font=("Arial", 11)
)


# =========================================================
# HEADER
# =========================================================

header = tk.Frame(
    root,
    bg=PRIMARY,
    height=115
)

header.pack(fill="x")

header.pack_propagate(False)


# Colored temperature icon

icon_circle = tk.Label(
    header,
    text="🌡️",
    font=("Arial", 28),
    bg="#FBBF24",
    fg=WHITE,
    width=3,
    height=1
)

icon_circle.pack(pady=(12, 2))


# App name

tk.Label(
    header,
    text="TempX",
    font=("Arial", 21, "bold"),
    bg=PRIMARY,
    fg=WHITE
).pack()


# Subtitle

tk.Label(
    header,
    text="Temperature Converter",
    font=("Arial", 10),
    bg=PRIMARY,
    fg="#E0E7FF"
).pack()


# =========================================================
# MAIN AREA
# =========================================================

main = tk.Frame(
    root,
    bg=BG
)

main.pack(
    fill="both",
    expand=True
)


center = tk.Frame(
    main,
    bg=BG
)

center.pack(
    fill="both",
    expand=True,
    padx=30,
    pady=18
)


# =========================================================
# INPUT CARD
# =========================================================

input_card = tk.Frame(
    center,
    bg=WHITE
)

input_card.pack(
    fill="x",
    pady=7
)


tk.Label(
    input_card,
    text="ENTER TEMPERATURE",
    font=("Arial", 10, "bold"),
    bg=WHITE,
    fg=GRAY
).pack(
    anchor="w",
    padx=22,
    pady=(15, 4)
)


display = tk.Entry(
    input_card,
    font=("Arial", 24, "bold"),
    justify="center",
    bg="#F8FAFC",
    fg=TEXT,
    insertbackground=PRIMARY,
    relief="flat"
)

display.pack(
    fill="x",
    padx=22,
    pady=(4, 15),
    ipady=7
)

# Automatically put cursor in input box
display.focus_set()


# =========================================================
# UNIT SELECTION CARD
# =========================================================

unit_card = tk.Frame(
    center,
    bg=WHITE
)

unit_card.pack(
    fill="x",
    pady=7
)


unit_inner = tk.Frame(
    unit_card,
    bg=WHITE
)

unit_inner.pack(
    pady=14
)


# FROM

tk.Label(
    unit_inner,
    text="FROM",
    font=("Arial", 8, "bold"),
    bg=WHITE,
    fg=GRAY
).grid(
    row=0,
    column=0,
    padx=8,
    pady=(0, 4)
)


from_unit = ttk.Combobox(
    unit_inner,
    values=[
        "Celsius",
        "Fahrenheit",
        "Kelvin"
    ],
    state="readonly",
    width=14
)

from_unit.grid(
    row=1,
    column=0,
    padx=8
)

from_unit.set("Celsius")


# SWAP BUTTON

swap_button = tk.Button(
    unit_inner,
    text="⇄",
    command=lambda: swap_units(),
    font=("Arial", 17, "bold"),
    bg=BLUE,
    fg=WHITE,
    activebackground="#0891B2",
    activeforeground=WHITE,
    relief="flat",
    bd=0,
    width=3,
    cursor="hand2"
)

swap_button.grid(
    row=1,
    column=1,
    padx=10
)


# TO

tk.Label(
    unit_inner,
    text="TO",
    font=("Arial", 8, "bold"),
    bg=WHITE,
    fg=GRAY
).grid(
    row=0,
    column=2,
    padx=8,
    pady=(0, 4)
)


to_unit = ttk.Combobox(
    unit_inner,
    values=[
        "Celsius",
        "Fahrenheit",
        "Kelvin"
    ],
    state="readonly",
    width=14
)

to_unit.grid(
    row=1,
    column=2,
    padx=8
)

to_unit.set("Fahrenheit")


# =========================================================
# RESULT CARD
# =========================================================

result_card = tk.Frame(
    center,
    bg=PRIMARY
)

result_card.pack(
    fill="x",
    pady=7
)


tk.Label(
    result_card,
    text="CONVERTED RESULT",
    font=("Arial", 9, "bold"),
    bg=PRIMARY,
    fg="#C7D2FE"
).pack(
    pady=(14, 2)
)


result_label = tk.Label(
    result_card,
    text="Enter a value",
    font=("Arial", 23, "bold"),
    bg=PRIMARY,
    fg=WHITE
)

result_label.pack(
    pady=(0, 14)
)


# =========================================================
# CONVERSION FUNCTIONS
# =========================================================

def get_symbol(unit):

    if unit == "Celsius":
        return "°C"

    elif unit == "Fahrenheit":
        return "°F"

    else:
        return "K"


def convert_temperature():

    value_text = display.get().strip()

    if value_text == "":
        result_label.config(
            text="Enter a temperature"
        )
        return

    try:

        value = float(value_text)

    except ValueError:

        result_label.config(
            text="Invalid number"
        )

        return


    source = from_unit.get()
    target = to_unit.get()


    # Convert source to Celsius

    if source == "Celsius":

        celsius = value

    elif source == "Fahrenheit":

        celsius = (value - 32) * 5 / 9

    else:

        celsius = value - 273.15


    # Convert Celsius to target

    if target == "Celsius":

        result = celsius

    elif target == "Fahrenheit":

        result = (celsius * 9 / 5) + 32

    else:

        result = celsius + 273.15


    # Show result

    result_label.config(
        text=(
            f"{value:g} {get_symbol(source)}"
            f"  =  "
            f"{result:.2f} {get_symbol(target)}"
        )
    )


# =========================================================
# SWAP UNITS
# =========================================================

def swap_units():

    source = from_unit.get()

    target = to_unit.get()

    from_unit.set(target)

    to_unit.set(source)

    if display.get().strip():

        convert_temperature()


# =========================================================
# CLEAR
# =========================================================

def clear_input():

    display.delete(
        0,
        tk.END
    )

    result_label.config(
        text="Enter a value"
    )

    display.focus_set()


# =========================================================
# BACKSPACE
# =========================================================

def backspace():

    current = display.get()

    if current:

        display.delete(
            len(current) - 1,
            tk.END
        )

    display.focus_set()


# =========================================================
# ACTION BUTTONS
# =========================================================

button_area = tk.Frame(
    center,
    bg=BG
)

button_area.pack(
    pady=12
)


# CLEAR BUTTON

clear_button = tk.Button(
    button_area,
    text="🧹  CLEAR",
    command=clear_input,
    font=("Arial", 11, "bold"),
    bg=LIGHT_RED,
    fg=RED,
    activebackground="#FECACA",
    relief="flat",
    bd=0,
    width=12,
    height=2,
    cursor="hand2"
)

clear_button.grid(
    row=0,
    column=0,
    padx=6
)


# BACKSPACE BUTTON

back_button = tk.Button(
    button_area,
    text="⌫  DELETE",
    command=backspace,
    font=("Arial", 11, "bold"),
    bg=LIGHT_BLUE,
    fg=PRIMARY,
    activebackground="#C7D2FE",
    relief="flat",
    bd=0,
    width=12,
    height=2,
    cursor="hand2"
)

back_button.grid(
    row=0,
    column=1,
    padx=6
)


# CONVERT BUTTON

convert_button = tk.Button(
    button_area,
    text="✨  CONVERT",
    command=convert_temperature,
    font=("Arial", 11, "bold"),
    bg=GREEN,
    fg=WHITE,
    activebackground="#059669",
    activeforeground=WHITE,
    relief="flat",
    bd=0,
    width=14,
    height=2,
    cursor="hand2"
)

convert_button.grid(
    row=0,
    column=2,
    padx=6
)


# =========================================================
# KEYBOARD ENTER ONLY
# =========================================================

def enter_pressed(event):

    convert_temperature()

    return "break"


# Only capture ENTER.
# Numbers are handled naturally by the Entry widget.
display.bind(
    "<Return>",
    enter_pressed
)


# =========================================================
# FOOTER
# =========================================================

tk.Label(
    root,
    text="Celsius   •   Fahrenheit   •   Kelvin",
    font=("Arial", 8),
    bg=BG,
    fg=GRAY
).pack(
    pady=(0, 8)
)


# =========================================================
# START APPLICATION
# =========================================================

root.mainloop()