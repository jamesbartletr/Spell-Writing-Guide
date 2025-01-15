from flask import Flask, render_template, request, send_from_directory
import os
from writer import draw_spell  # Assuming writer.py has the draw_spell function for generating visuals

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/generated'

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Folder where the attributes text files are stored
ATTRIBUTES_FOLDER = os.path.join("Attributes")


# Function to load dropdown options from the attribute files
def load_attributes(attribute_name):
    file_path = os.path.join(ATTRIBUTES_FOLDER, f"{attribute_name}.txt")
    if not os.path.isfile(file_path):
        return []
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines()]


@app.route('/')
def index():
    # Load all dropdown options from the attribute files
    levels = load_attributes("levels")
    ranges = load_attributes("range")
    area_types = load_attributes("area_types")
    damage_types = load_attributes("damage_types")
    schools = load_attributes("school")

    return render_template(
        "index.html",
        levels=levels,
        ranges=ranges,
        area_types=area_types,
        damage_types=damage_types,
        schools=schools
    )


@app.route('/generate', methods=['POST'])
def generate():
    # Fetch the form data
    level = request.form.get('level')
    rang = request.form.get('range')
    area = request.form.get('area')
    dtype = request.form.get('dtype')
    school = request.form.get('school')

    if not all([level, rang, area, dtype, school]):
        return "Invalid input! Please fill all the fields.", 400

    # Use the writer.py function to generate an image with the selected attributes
    image_filename = f"spell_{level}_{rang}_{area}_{dtype}_{school}.png"
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_filename)

    # Generate the spell visualization using draw_spell from writer.py
    draw_spell(
        level=level,
        rang=rang,
        area=area,
        dtype=dtype,
        school=school,
        savename=image_path,
        legend=True
    )

    # Render the template with the generated image
    return render_template("index.html", generated_image=image_path)


@app.route('/static/generated/<filename>')
def serve_image(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':
    app.run(debug=True)
