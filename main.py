from flask import Flask, render_template, request
from Newsletter_sub import *
from Learning_method_ML import *

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/test')
def test_data():
    return render_template("index.html")


@app.route('/newsletter_success', methods=["POST"])
def subscribe_success():
    user_email = request.form["email"]
    sending_newsletter(user_email)
    # activate_newsletter(user_email)
    return render_template("subscribe_success.html", user_email=user_email)


@app.route("/result", methods=["POST"])
def receive_data():
    q1, q2, q3, q4, q5, q6, q7, q8, q9, q10 = " ", " ", " ", " ", " ", " ", " ", " ", " ", " "
    k_v, a_v, v_v = 0, 0, 0
    your_method = " "
    answers = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]

    for index in range(1, 10):
        answers[index - 1] = user_input(request.form[f"q{index}"])[0]
        if answers[index - 1] == "Visual":
            v_v += 1
        elif answers[index - 1] == "Auditory":
            a_v += 1
        elif answers[index - 1] == "Kinesthetic":
            k_v += 1

    if k_v > a_v and k_v > v_v:
        your_method = "Kinesthetic"
    elif a_v > k_v and a_v > v_v:
        your_method = "Visual"
    else:
        your_method = "Auditory"
    return render_template(f"{your_method}.html", your_method=your_method)


if __name__ == "__main__":
    app.run(debug=True)
