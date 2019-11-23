from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main_route():
    return render_template('inex.html')


@app.route('/_stuff')
def upd_video():



@app.route('/settings', methods=['GET', 'POST'])
def settings_page():
    return render_template('loginpage.html')


if __name__ == "__main__":
    app.run()

