from flask import Flask, request, redirect, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return open('index.html').read()

@app.route('/styles.css')  # Serve CSS explicitly
def serve_css():
    return send_from_directory('.', 'styles.css')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    budget = request.form['budget']
    goals = request.form['goals']
    with open('leads.txt', 'a') as f:
        f.write(f"{name}, {email}, {budget}, {goals}\n")
    return redirect('/thanks')

@app.route('/thanks')
def thanks():
    return "<h1>Thanks! We’ll reach out soon.</h1><p><a href='/'>Back</a></p>"

if __name__ == "__main__":
    app.run(debug=True)