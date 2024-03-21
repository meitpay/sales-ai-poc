from flask import Flask, request, Response
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, Docker!'

def run_process_and_stream_output(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

    # Stream each line of the output
    for line in iter(process.stdout.readline, ''):
        print(line, end='')
        yield line

    process.stdout.close()
    return_code = process.wait()
    if return_code:
        raise subprocess.CalledProcessError(return_code, command)

@app.route('/job-listing', methods=['POST'])
def job_listing():
    try:
        data = request.get_json()
        company_description = data['company']
        company_domain = data['domain']
        hiring_needs = data['needs']
        specific_benefits = data['benefits']

        command = [
            'python', 'crews/job_posting/main.py',
            '--company_description', company_description,
            '--company_domain', company_domain,
            '--hiring_needs', hiring_needs,
            '--specific_benefits', specific_benefits
        ]

        return Response(run_process_and_stream_output(command), mimetype='text/markdown')

    except Exception as e:
        return f"An error occurred: {e}", 500

@app.route('/person-search', methods=['POST'])
def person_search():
    print('---------- Person Search ----------')
    try:
        data = request.get_json()
        person_name = data['person']
        websites = ', '.join(data['websites'])
        misc_information = data['miscInfo']
        social_media_profiles = ', '.join(data['soMeProfiles'])

        command = [
            'python', 'crews/person_search/main.py',
            '--person_name', person_name,
            '--websites', websites,
            '--misc_information', misc_information,
            '--social_media_profiles', social_media_profiles
        ]

        return Response(run_process_and_stream_output(command), mimetype='text/markdown')

    except Exception as e:
        return f"An error occurred: {e}", 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
