
# This script creates an interactive Bokeh visualization with dropdowns and a button.
# Dropdowns allow users to select Attributes, and a callback function is expected
# to handle interactions and plot updates.
from writer import *

# Importing necessary components from Bokeh for creating interactive plots and UI elements.
# - `figure`: Used to render the main visualization.
# - `Dropdown`: Used to create dropdown menus for attribute selection.
# - `CustomJS`: Handles JavaScript events for interactive components.
from bokeh.layouts import column,row
from bokeh.models import Button,CustomJS, Dropdown
from bokeh.palettes import RdYlBu3
from bokeh.plotting import figure, curdoc,show

# Purpose: Creates a Bokeh dropdown menu using provided Attributes.
# Inputs:
# - att (list): List of Attributes for the dropdown.
# - label (str): Dropdown label.
# Outputs:
# - Dropdown menu with configured JavaScript interaction.
def create_dropdown(att,label = "Dropdown"):
    menu = [(l.capitalize(),l.lower()) for l in att]
    dropdown = Dropdown(label=label, menu=menu)
    dropdown.on_change("value", callback)
    return(dropdown)

# Placeholder for future development.
# Will handle dropdown interactions, extract data, and update the plot dynamically.
def callback(attr, old, new):
    selected_ranges = ranges_ddm.value
    selected_levels = levels_ddm.value
    selected_area_types = area_types_ddm.value
    selected_dtypes = dtypes_ddm.value
    selected_schools = schools_ddm.value
    x_new, y_new = base_fn(n)
    if selected_ranges:
        p.scatter(x_new, y_new, size=10, fill_color="red", line_color="pink")
    elif selected_levels:
        p.scatter(x_new, y_new, size=10, fill_color="blue", line_color="cyan")
    elif selected_area_types:
        p.scatter(x_new, y_new, size=10, fill_color="green", line_color="lime")
    elif selected_dtypes:
        p.scatter(x_new, y_new, size=10, fill_color="purple", line_color="magenta")
    elif selected_schools:
        p.scatter(x_new, y_new, size=10, fill_color="orange", line_color="yellow")
    curdoc().add_root(p)

#define base function
# Using the polygon base function from the `bases` module to generate coordinates.
# Number of points (`n`) determines the polygon structure.
base_fn = bases.polygon
#define number of points
n = 11
n = 11
#get base
x,y = base_fn(n)

# Loading Attributes from the specified files in the `Attributes` folder.
# These Attributes populate the dropdown menus for user selection.
#load Attributes
ranges = load_attribute("Attributes/range.txt")
levels = load_attribute("Attributes/levels.txt")
area_types = load_attribute("Attributes/area_types.txt")
dtypes = load_attribute("Attributes/damage_types.txt")
schools = load_attribute("Attributes/school.txt")

#initialise figure
# Initializing the Bokeh figure with configured dimensions, ranges, and styles.
# Adding a polygon scatter plot and hiding unnecessary visual elements like gridlines and axes.
#initialise figure
fig_size = 750
p = figure(width = fig_size ,height = fig_size ,x_range = (-1.5,1.5), y_range = (-1.5,1.5),toolbar_location = None)
p.outline_line_color = None
p.grid.grid_line_color = None
p.scatter(x,y,size = 10,fill_color = "black",line_color = "navy")
p.axis.visible = False

# Creating dropdown menus for different attribute groups like ranges, levels, and types.
# Grouping dropdowns into rows to organize UI layout.
#setup dropdowns
ranges_ddm = create_dropdown(ranges,"Range")
levels_ddm = create_dropdown(levels,"Level")
area_types_ddm = create_dropdown(area_types,"Area_type")
dtypes_ddm = create_dropdown(dtypes,"damage_type")
schools_ddm = create_dropdown(schools,"Schools")

# Adding a button labeled "Press Me" to trigger actions for the callback function.
# The button is linked to the `callback` function for handling click events.
button = Button(label="Press Me")
button.on_click(lambda: print(f"Button clicked! Current dropdowns: Range: {ranges_ddm.value}, Level: {levels_ddm.value}, Area Type: {area_types_ddm.value}, Damage Type: {dtypes_ddm.value}, Schools: {schools_ddm.value}"))

# Note: Ensure proper Attributes and running environment, such as the use of the `bokeh serve` command.
if __name__ == "__main__":
# Adding rows of dropdowns, the button, and the visualized figure into the Bokeh document structure.
# The layout is organized in a vertical column.
    row1 = row(ranges_ddm,levels_ddm,area_types_ddm)
    row2 = row(dtypes_ddm,schools_ddm)

curdoc().add_root(column(row(row1, row2), button, p))
