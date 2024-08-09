from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    try:
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        print(f"Received message from {name} ({email}): {message}")
        return "Thank you for contacting us!"
    except Exception as e:
        print(f"Error: {e}")
        return "An error occurred. Please try again later.", 500

if __name__ == '__main__':
    app.run(debug=True)

