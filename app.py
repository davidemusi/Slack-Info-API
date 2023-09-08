from flask import Flask, request, jsonify
import datetime
import pytz

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_info():
    # Get query parameters from the request
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Get the current day of the week
    current_day = datetime.datetime.now(pytz.utc).strftime('%A')

    # Get the current UTC time with a +/-2 minute window and format it
    utc_time = datetime.datetime.now(pytz.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

    # GitHub URL of the file being run
    github_file_url = "https://github.com/davidemusi/Slack-Info-API/blob/main/app.py"

    # GitHub URL of the full source code
    github_repo_url = "https://github.com/davidemusi/Slack-Info-API.git"

    # Status Code of Success
    status_code = 200

    # Create the JSON response
    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": status_code
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
