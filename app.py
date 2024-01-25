from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if a file was uploaded
        if 'file' not in request.files:
            return render_template('index.html', error='No file part')

        file = request.files['file']

        # Check if the file has a CSV extension
        if file.filename == '' or not file.filename.endswith('.csv'):
            return render_template('index.html', error='Invalid file type. Please upload a CSV file.')

        # Read the CSV file into a DataFrame
        df = pd.read_csv(file)

        # Get the column names of the first row
        columns = df.columns.tolist()

        # Pass the column names to the HTML template
        return render_template('index.html', columns=columns)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
