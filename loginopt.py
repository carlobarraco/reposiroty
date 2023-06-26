from flask import Flask, render_template, request, session, redirect, url_for
import random
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'email@gmail.com'
app.config['MAIL_PASSWORD'] = 'password'
app.secret_key = 'ABCDE'

mail = Mail(app)

# Pagina di login
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'email@gmail.com' and password == '1234':
            otp_code = generate_otp()
            send_otp_email(username, otp_code)
            session['otp_code'] = otp_code
            session['username'] = username
            return render_template('login2.html', username=username)
        else:
            return render_template('index4.html', error="Credenziali non valide")

    return render_template('index4.html')

# Genera un codice OTP casuale
def generate_otp():
    otp = random.randint(100000, 999999)
    return str(otp)

# Invia il codice OTP all'indirizzo email
def send_otp_email(email, otp):
    subject = 'Codice OTP'
    body = f"Il tuo codice OTP è: {otp}"
    msg = Message(subject, sender=app.config['MAIL_USERNAME'], recipients=[email])
    msg.body = body
    mail.send(msg)
    print("Email inviata con successo")

# Verifica il codice OTP inserito dall'utente
@app.route('/verify', methods=['POST'])
def verify_otp():
    username = session.get('username')
    otp = request.form['otp']
    saved_otp = session.get('otp_code')

    # Verifica il codice OTP
    if otp == saved_otp:
        return redirect(url_for('success'))
    else:
        return render_template('login2.html', username=username, error="Codice OTP non valido")

# Pagina di accesso riuscito
@app.route('/success')
def success():
    username = session.get('username')
    return render_template('success.html', username=username)

if __name__ == '__main__':
    app.run()