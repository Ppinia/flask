from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/pletemsi", methods=["GET", "POST"])
def pletemsi():
    return render_template("pletemsi.html")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/contact", methods=["POST"])
def contact():
    contact_name = request.form.get("contact-name")
    contact_email = request.form.get("contact-email")
    contact_message = request.form.get("contact-message")

    print(contact_name)
    print(contact_email)
    print(contact_message)

    return render_template("success.html")

if __name__ == '__main__':
    app.run(use_reloader=True)