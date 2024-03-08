from flask import Flask
from flask import Flask, request, jsonify
import subprocess
import json


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker!'

@app.route('/process-data', methods=['POST'])
def process_data():
    # Extract form data
    form_data = request.form.to_dict()

    # Convert form data to JSON string
    form_data_json = json.dumps(form_data)

    # Call the crewai/main.py script with the form data
    result = subprocess.run(['python', 'crewai/main.py', form_data_json], capture_output=True, text=True)

    # Check if the script executed successfully
    if result.returncode == 0:
        # Return the output from the script
        return jsonify({"result": result.stdout.strip()})
    else:
        # In case of an error, return the error message
        return jsonify({"error": result.stderr.strip()}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
