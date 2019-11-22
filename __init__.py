from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main_route():
    return "It works!"


@app.route('/settings', methods=['GET', 'POST'])
def settings_page():
    return render_template("template/login_page.html")


if __name__ == "__main__":
    app.run()

