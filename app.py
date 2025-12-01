from flask import Flask, render_template, request
from flask_cors import CORS
import smtplib
from email.message import EmailMessage
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("form.html")

@app.route("/enviar", methods=["POST"])
def enviar():
    destinatario = request.form["email"]   # e-mail da pessoa

    # Configurações do e-mail
    EMAIL_REMETENTE = "grouphopex@gmail.com"
    SENHA = os.getenv("EMAIL_SENHA")

    msg = EmailMessage()
    msg["Subject"] = "Olá, Somos a Hope-X!"
    msg["From"] = EMAIL_REMETENTE
    msg["To"] = destinatario
    # Mensagem enviada
    msg.add_alternative("""
    <html>
    <body>
        <p><b>Olá!</b></p>
        <p>Agradecemos o seu contato.</p>
        <p>Para facilitar, clique no link abaixo para agendar sua entrevista:</p>
        <p><a href="https://docs.google.com/forms/d/e/1FAIpQLSfnJlMbbmrddCwx5Elb3dZph7wJflndGuE0Cqjku2LXmgU3pQ/viewform?usp=dialog">Formulário de Agendamento</a></p>

        <h3><strong>Como funciona o processo?</strong></h3>

        <p><strong>1️⃣ Agendamento da entrevista:</strong>  
        Você escolhe data, horário e nos informa o objetivo do projeto.</p>

        <p><strong>2️⃣ Alinhamento do projeto:</strong>  
        Nossa equipe entrará em contato para iniciar o desenvolvimento do seu site.</p>

        <p><strong>Retorno em até 48 horas.</strong></p>

        <p>Atenciosamente,<br>
        <strong>Equipe Group Hope-X</strong></p>
    </body>
    </html>
    """, subtype="html")

    # Enviar
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_REMETENTE, SENHA)
            smtp.send_message(msg)

        return "<h2>E-mail enviado com sucesso!</h2>"

    except Exception as e:
        return f"<h2>Erro ao enviar: {e}</h2>"

if __name__ == "__main__":
    app.run(debug=True)

