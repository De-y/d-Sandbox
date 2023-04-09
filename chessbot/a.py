# Import necessary modules
import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery
import os, flask, json

# Set up OAuth flow
CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'

# Set up Flask web app
from flask import Flask, render_template, request
app = Flask(__name__)
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
# Define index route
@app.route('/', methods=['GET', 'POST'])
def index():
    # If user has not authorized app to access their Google account, send them to authorization URL
    if 'credentials' not in flask.session:
        return flask.redirect('authorize')

    # Load credentials from session
    credentials_info = json.loads(flask.session['credentials'])
    credentials = google.oauth2.credentials.Credentials.from_authorized_user_info(credentials_info)    
    # Create YouTube API client
    youtube = googleapiclient.discovery.build(API_NAME, API_VERSION, credentials=credentials)

    # If form is submitted, report video
    if request.method == 'POST':
        video_url = request.form['video_url']
        reason = request.form['reason']

        # Get video ID from URL
        video_id = video_url.split('=')[1]

        # Report video with reason
        youtube.videos().report(id=video_id, body={'reason': reason}).execute()

        # Redirect to success page
        return flask.redirect('/success')

    # Render index template
    return render_template('index.html')

# Define authorize route
@app.route('/authorize')
def authorize():
    # Set up OAuth flow
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(CLIENT_SECRET_FILE, scopes=SCOPES,     redirect_uri="http://localhost:3000/callback/google")

    # Generate authorization URL and redirect user to it
    authorization_url, state = flow.authorization_url(access_type='offline', include_granted_scopes='true')
    flask.session['state'] = state
    return flask.redirect(authorization_url)

# Define callback route
@app.route('/callback/google')
def oauth2callback():
    # Verify authorization code and exchange for credentials
    state = flask.session['state']
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(CLIENT_SECRET_FILE, scopes=SCOPES, state=state,     redirect_uri='http://localhost:3000/callback/google')
    flow.redirect_uri = flask.url_for('oauth2callback', _external=True)
    authorization_response = request.url
    flow.fetch_token(authorization_response=authorization_response)

    # Store credentials in session
    credentials = flow.credentials
    flask.session['credentials'] = credentials.to_json()

    # Redirect back to index
    return flask.redirect('/')

# Define success route
@app.route('/success')
def success():
    return 'Video successfully reported!'

if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.run(debug=True, port=3000)
