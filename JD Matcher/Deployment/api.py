# Library Imports
from flask import Flask, render_template, request
import spacy
import warnings, re
warnings.filterwarnings("ignore")

app = Flask(__name__)
nlp = spacy.load('saved_model')
		
@app.route('/')
def home():
	return render_template('index.html')

@app.route('/extract', methods=['POST'])
def extract():
	raw_text = request.form.get('job_description')
	jd = re.sub('\n', ' ', raw_text).strip()
	doc = nlp(jd)
	skills = {ent.text for ent in doc.ents if ent.label_ == 'SKILL'}
	return render_template('index.html', OUTPUT=str(', '.join(skills)), RAW_TEXT=raw_text)

if __name__ == "__main__":
    app.run(debug=True)