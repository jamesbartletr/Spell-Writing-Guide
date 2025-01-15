# Spell Writing Guide

This repository contains the updated and improved version of the code used in the [Spell Writing Guide](https://www.drivethrurpg.com/product/429711/The-Spell-Writing-Guide?manufacturers_id=22808). The system provides a simple method for generating and visualizing spells, making it particularly convenient for Dungeons & Dragons (D&D) 5e or other tabletop RPGs. The modular nature makes it easy to adapt for any system or personal customization.

## Features Overview

The codebase revolves around a creative representation of spells, utilizing math, geometry, and visualization tools to generate unique graphical and audible attributes for spells. Here is a breakdown of the various functionality offered by the key files:

### 1. `bard_spells.py`  
*Utility for Generating Musical Notes*

This script maps D&D spell attributes (e.g., range, damage type, school, etc.) to musical notes or chords. The concept is to audibly represent spells as a creative way to enhance role-playing experiences.

---

### 2. `bases.py`  
*Mathematical Bases for Geometry and Visualization*

Provides functions for generating geometric shapes and patterns as x, y coordinate data. These bases are essential for constructing the visual components of spells.

**Key Features:**
- Polygon generator for custom n-sided shapes.
- Line and curve generators (linear, quadratic, cubic, and golden spiral patterns).
- Supports flexible customization like radius, start angle, and shape parameters.

---

### 3. `line_shapes.py`  
*Utility for Connecting Points with Line Shapes*

Includes functions for creating geometric shapes and curves (circles, arcs, straight lines) between two specified points in a Cartesian coordinate system. Useful for connecting spell-related elements such as levels and ranges.

**Key Features:**
- Centered and off-center circles/arcs.
- Straight lines for point-to-point connections.
- Versatile and optimized for mathematical and graphical applications.

---

### 4. `writer.py`  
*Spell Visualization Platform*

This script generates detailed visual representations of spell attributes, such as range, level, school, and more, through plot diagrams. It is highly customizable and allows users to add personalized touch through configurable files.

**Key Features:**
- Visualizes spell details (e.g., schools, levels, etc.) in graphical format.
- Provides command-line support for generating visuals dynamically.
- Modular approach allows the addition of new attributes via text files in the `Attributes/` directory.
- Ideal for DMs and players seeking visual aids for their campaigns.

---

### 5. `writer_live.py`  
*Interactive Visualization via Bokeh*

`writer_live.py` is an interactive tool for displaying spell visualizations dynamically. Users can select attributes through dropdown menus, directly affecting the visualization in real-time. Ideal for exploring and experimenting with spell designs.

**Key Features:**
1. Interactive dropdown menus populate from external files, allowing customizable spell attributes.
2. Dynamic scatter plot generation based on user-selected attributes.
3. Integrates with Bokeh for interactive web visualization.
4. Customizable geometric bases (`bases.polygon`) for plot computations.
5. Real-time updates triggered by dropdowns or user inputs.

---

## Folder Structure
- **Uniques/**: Directory auto-generated during runtime, containing unique binary files for rotational patterns.
- **Attributes/**: Houses text files defining valid inputs for spell attributes (e.g., levels, ranges, schools).

---

## Setup

To start using this project, clone the repository:

```bash
git clone https://github.com/GorillaOfDestiny/SpellWritingGuide
```

Upon initial execution, the code will automatically generate a folder called `Uniques` containing files like `11.npy`. These are used to store rotationally unique binary numbers that the method relies on.

---

## Dependencies

The project is developed using **Python 3.10.4**. Below are the required Python modules:

- `numpy`
- `matplotlib`
- `argparse`
- `math`
- `os`
- `tqdm`
- `bokeh`

To install them, use:

```bash
pip install numpy matplotlib argparse tqdm bokeh
```

---

## Running the Code

To generate visualizations, execute:

```bash
python writer.py
```

For detailed information about optional commands, type:

```bash
python writer.py --help
```

### Example Usage
A standard input for generating a spell is:

```bash
python writer.py -level <level> -range <range> -area <area> -dtype <dtype> -school <school>
```

Replace `<level>`, `<range>`, etc. with appropriate lowercase strings (e.g., `fireball`, `cone`, etc.). Defaults will generate a "Fireball" spell visualization.

To see all available inputs and their formats:

```bash
python writer.py --arg_help
```

Options are read from corresponding `.txt` files in the `Attributes/` directory.

---

## Modifying the System

To add your own spell attributes:
1. Open the relevant `.txt` files in the `Attributes/` directory.
2. Add your entries into a new line (e.g., school names, ranges, etc.).

Example:
- Adding a new damage type to `damage_types.txt`.

---

## Conclusion

The **Spell Writing Guide** system combines creativity with robust mechanics to give players, Dungeon Masters, and enthusiasts an intuitive way to visualize (and even hear) their spells. Whether used for personal campaigns or public projects, this repository offers a modular, extendable framework for spell representation.
