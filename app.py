from flask import Flask, render_template, request, redirect, url_for
from email.message import EmailMessage
import smtplib
import ssl  # Import the ssl module

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sendemail/", methods=["POST"])
def sendemail():
    if request.method == "POST":
        name = request.form["name"]
        subject = request.form["Subject"]
        email = request.form["_replyto"]
        message = request.form["message"]

        # Replace with your Gmail credentials
        your_email = "komikers09@gmail.com"
        your_password = "owvw thsf cezf kivs"  # Use an App Password if 2FA is enabled

        # Set up the SMTP server
        try:
            context = ssl.create_default_context()  # Create a secure context
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server: # Use SMTP_SSL
                server.ehlo()  # No need to call starttls() with SMTP_SSL
                server.login(your_email, your_password)

                # Compose the email
                msg = EmailMessage()
                msg.set_content(f"Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}")
                msg["To"] = your_email  # Send the email to yourself
                msg["From"] = your_email
                msg["Subject"] = subject

                # Send the email
                server.send_message(msg)
                print("Email sent successfully!")
        except Exception as e:
            print(f"Failed to send email: {e}")
            # Consider adding a flash message to display to the user on the website
            # For example:
            # flash(f"Failed to send email: {e}", "error") # Requires adding flash to imports
            # return redirect(url_for("index")) #  and adding flash message display to index.html

        return redirect(url_for("index")) # Fix: redirect to index

if __name__ == "__main__":
    app.run(debug=True)
