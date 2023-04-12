# Import necessary modules
import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery
import os, flask, json

CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'

from flask import Flask, render_template, request
app = Flask(__name__, template_folder='templates', static_folder='assets')
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

@app.route('/', methods=['GET', 'POST'])
def index():

    if 'credentials' not in flask.session:
        return flask.redirect('authorize')

    credentials_info = json.loads(flask.session['credentials'])
    credentials = google.oauth2.credentials.Credentials.from_authorized_user_info(credentials_info)    

    youtube = googleapiclient.discovery.build(API_NAME, API_VERSION, credentials=credentials)

    if request.method == 'POST':

        video_id = 'MbppYBjbPBo'
        
        report = {
            'reasonId': '5',
            'comments': 'This video is inappropriate',
            'videoId': video_id,
            'language': 'en'
        }


        youtube.videos().reportAbuse(body=report).execute()

        return flask.redirect('/success')

    return render_template('index.html')

@app.route('/authorize')
def authorize():
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(CLIENT_SECRET_FILE, scopes=SCOPES, redirect_uri="http://localhost:3000/callback/google")

    authorization_url, state = flow.authorization_url(access_type='offline', include_granted_scopes='true')
    flask.session['state'] = state
    return flask.redirect(authorization_url)

@app.route('/callback/google')
def oauth2callback():
    state = flask.session['state']
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(CLIENT_SECRET_FILE, scopes=SCOPES, state=state, redirect_uri='http://localhost:3000/callback/google')
    flow.redirect_uri = flask.url_for('oauth2callback', _external=True)
    authorization_response = request.url
    flow.fetch_token(authorization_response=authorization_response)

    credentials = flow.credentials
    flask.session['credentials'] = credentials.to_json()

    return flask.redirect('/')

@app.route('/success')
def success():
    return 'Video successfully reported!'

if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.run(debug=True, port=3000)
