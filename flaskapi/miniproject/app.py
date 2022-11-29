from flask import Flask, render_template, request,
jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

tasks = ["Make miniproject for Flask", "Finish all assignments", "Build a task app", "Have a good night sleep"]

#@app.route('/form-handler', methods=['POST'])
#def handle_data():
#   return jsonify(request.form)

class TaskForm(FlaskForm):
    task = StringField("Task")
    submit = SubmitField("Add Task")

@app.route('/', methods=["GET", "POST"])
def index():
    if 'task' in request.form:
        tasks.append(request.form['task'])

    return render_template('index.html', tasks=tasks, template_form=TaskForm()) 



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)

