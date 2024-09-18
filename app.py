from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# Route for serving CSS files directly from the root directory
@app.route('/<path:filename>')
def serve_static(filename):
    if filename.endswith('.css'):
        return send_from_directory('.', filename)
    return send_from_directory('.', filename)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
