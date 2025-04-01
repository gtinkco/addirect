from flask import Flask, request, redirect, send_from_directory
import os

app = Flask(__name__)

# Set the path to the public directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUBLIC_DIR = os.path.join(BASE_DIR, 'public')

@app.route('/')
def home():
    return send_from_directory(PUBLIC_DIR, 'index.html')

@app.route('/styles.css')
def serve_css():
    return send_from_directory(PUBLIC_DIR, 'styles.css')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    budget = request.form['budget']
    goals = request.form['goals']
    print(f"Lead: {name}, {email}, {budget}, {goals}")
    try:
        with open('leads.txt', 'a') as f:
            f.write(f"{name}, {email}, {budget}, {goals}\n")
    except:
        pass  # Ignore file write errors on Vercel
    return redirect('/thanks', code=302)

@app.route('/thanks')
def thanks():
    return "<h1>Thanks! We’ll reach out soon.</h1><p><a href='/'>Back</a></p>"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)