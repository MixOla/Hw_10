import json
import functions
import visualize
from flask import Flask

app = Flask(__name__)

candidates = functions.get_all_candidates()


@app.route('/')
def page_index():
    candidates = functions.get_all_candidates()
    html_code = visualize.build_html_for_all_candidates(candidates)
    return html_code

@app.route('/skills/<skill>')
def page_skills(skill):
    candidates = functions.get_skills_of_cand(skill)
    html_code = visualize.build_html_for_all_candidates(candidates)
    return html_code

@app.route('/candidates/<int:id>')
def page_candidates(id):
    candidate = functions.get_id_cand(id)
    html_code = visualize.build_html_for_one_candidate(candidate)
    return html_code





app.run(debug=True)