from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get('/questions')
def create_question_form():
    #TODO: returns html to include the blank madlib form

    """use prompts from a story instance and create a form with a text input for
    each prompt; return the form"""

    return render_template(
        "questions.html",
        prompts = silly_story.prompts
    )

@app.get('/results')
def take_responses_from_form(): #TODO: generate_story_from_form
    """ takes input values from form answers and creates a story from those
    answers on the results page; return the rendered story """

    generated_story = silly_story.generate(request.args)

    return render_template(
        "results.html",
        story = generated_story
    )