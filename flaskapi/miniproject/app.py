from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

tasks = ["Make miniproject for Flask", "Finish all assignments", "Build a task app", "Have a good night sleep"]

class TaskForm(FlaskForm):
    task = StringField("Task")
    submit = SubmitField("Add Todo")

@app.route('/', methods=["GET", "POST"])
def index():
    if 'task' in request.form:
        tasks.append(request.form['task'])

    return render_template('index.html', tasks=tasks, template_form=TaskForm()) 




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)

