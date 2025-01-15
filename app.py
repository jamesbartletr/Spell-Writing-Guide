from flask import Flask, render_template, request, send_from_directory
import os
from writer import generate_image  # Assuming writer.py has a function generate_image to create images

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/generated'

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/generate', methods=['POST'])
def generate():
    # Get the form data
    prompt = request.form.get('prompt')

    if not prompt:
        return "Invalid prompt, please enter some text!", 400

    # Call the generate_image function from writer.py
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{prompt.replace(' ', '_')}.png")
    generate_image(prompt, image_path)  # Assumes generate_image saves a file to the given path

    return render_template("index.html", generated_image=image_path)


@app.route('/static/generated/<filename>')
def serve_image(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':
    app.run(debug=True)
