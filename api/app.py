from flask import Flask, request, redirect, send_from_directory
import os
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

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
    print(f"Lead: {name}, {email}, {budget}, {goals}")  # Log for Vercel
    # Email setup
    msg = MIMEText(f"New Lead:\nName: {name}\nEmail: {email}\nBudget: ${budget}\nGoals: {goals}")
    msg['Subject'] = 'New AdDirect Lead'
    msg['From'] = 'GTINKCO@gmail.com'  # Sender (your Gmail)
    msg['To'] = 'GTINKCO@gmail.com'    # Receiver (your Gmail)
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login('GTINKCO@gmail.com', 'sheevwyiqtzmjeti')  # Your App Password
            server.send_message(msg)
        print("Email sent successfully")
    except Exception as e:
        print(f"Email failed: {e}")
    return redirect('/thanks', code=302)

@app.route('/thanks')
def thanks():
    return "<h1>Thanks! We’ll reach out soon.</h1><p><a href='/'>Back</a></p>"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)