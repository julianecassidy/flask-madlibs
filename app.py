from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get('/questions')
def create_question_form():
    """use prompts from a story instance and create a form with a text input for
    each prompt; return the form"""

    return render_template(
        "questions.html",
        prompts = silly_story.prompts
    )
