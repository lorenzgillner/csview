#!/usr/bin/env python3

import tkinter as tk
import csv
import sys

from tkinter.filedialog import askopenfilename
from tksheet import Sheet
from themes import theme_light_orange

# Get the file name from the command line arguments
if len(sys.argv) == 1:
    filename = askopenfilename(
        defaultextension="*.csv",
        filetypes=[
            ("CSV files", "*.csv"),
            ("TSV Files", "*.tsv"),
            ("Data Files", "*.dat"),
            ("All Files", "*.*"),
        ],
    )
elif len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    print("Usage: csview <filename>")
    sys.exit()

# Create a Tkinter window
window = tk.Tk()
window.title("CSView: {0}".format(filename))

# Open the CSV file and read its contents
with open(filename, "r") as f:
    reader = csv.reader(f)
    data = list(reader)

# Create Tk Sheet for data display
sheet = Sheet(window, width=640, height=480)
sheet.set_options(**theme_light_orange, rounded_boxes=False)
sheet.yscroll.grid(row=0, column=2, rowspan=2, sticky="nswe")
sheet.enable_bindings(
    "single_select",
    "drag_select",
    "select_all",
    "column_select",
    "row_select",
    "move_columns",
    "move_rows",
    "column_width_resize",
    "column_height_resize",
    "row_width_resize",
    "row_height_resize",
    "arrowkeys",
    "right_click_popup_menu",
    "copy",
)
sheet.pack(expand=tk.YES, fill=tk.BOTH)

# Add headers to the table
headers = data[0]
sheet.headers(headers)

# Populate the table with data from the CSV file
sheet.data = data[1:]
sheet.readonly()

# Add key binding to exit
window.bind("<q>", lambda _: window.destroy())

# Start the main loop
window.mainloop()
