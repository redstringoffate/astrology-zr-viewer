# app.py (Flask version using pyswisseph)

from flask import Flask, render_template, request, send_file
import pandas as pd
import pyswisseph as swe
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Parse form data
            year = int(request.form['year'])
            month = int(request.form['month'])
            day = int(request.form['day'])
            hour = int(request.form['hour'])
            minute = int(request.form['minute'])
            lat = float(request.form['lat'])
            lon = float(request.form['lon'])
            tz = float(request.form['tz'])

            # Placeholder response file generation (simulate actual logic)
            data = {
                'Date': [f"{year}-{month:02}-{day:02}"],
                'Age': [0],
                'Fortune L1': ['Leo ♌'],
                'Spirit L1': ['Virgo ♍'],
                'Firdaria Major': ['☉ Sun'],
                'Firdaria Minor': ['☽ Moon'],
                'Profection Sign': ['Cancer ♋'],
                'Uranus': ['Capricorn ♑'],
                'Neptune': ['Capricorn ♑'],
                'Pluto': ['Scorpio ♏']
            }
            df = pd.DataFrame(data)
            file_path = "output.xlsx"
            df.to_excel(file_path, index=False)

            return send_file(file_path, as_attachment=True)

        except Exception as e:
            return f"An error occurred: {str(e)}"

    return render_template('index.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)
