from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Simulated job data
job_database = {
    "76104": [
        {"company": "Starbucks", "title": "Barista", "type": "Part-Time"},
        {"company": "Fort Worth ISD", "title": "Library Assistant", "type": "Part-Time"},
        {"company": "Dutch Bros", "title": "Crew Member", "type": "Part-Time"}
    ],
    "76110": [
        {"company": "In-N-Out", "title": "Cashier", "type": "Part-Time"},
        {"company": "AAFES", "title": "Customer Service Rep", "type": "Part-Time"}
    ]
}

@app.route('/', methods=['GET', 'POST'])
def index():
    jobs = []
    if request.method == 'POST':
        zip_codes = request.form.get('zip_codes', '')
        zip_list = [z.strip() for z in zip_codes.split(',')]
        for zip_code in zip_list:
            jobs.extend(job_database.get(zip_code, []))
    return render_template('index.html', jobs=jobs)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
