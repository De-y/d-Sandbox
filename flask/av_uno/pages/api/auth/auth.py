from flask import Blueprint, request, redirect, session
import requests
import uuid
from flask_login import login_user, current_user
from prisma.models import User
import json
from libraries.db.models import UserModel

auth_blueprint = Blueprint('auth', __name__, url_prefix='/auth')

@auth_blueprint.route('/')
def avpass_home():
    return {'Notice': 'You have reached the authentication API route.'}

@auth_blueprint.route('/avpass', methods=['GET'])
def avpass_login():
    # Generate a unique state and save it to the session for later validation
    state = str(uuid.uuid4())
    session['state'] = state

    # Generate a unique nonce and save it to the session for later validation
    nonce = str(uuid.uuid4())
    session['nonce'] = nonce

    # Generate the authorization request URL with the appropriate parameters
    auth_endpoint = 'http://localhost:3000/oauth/authorize'
    client_id = '64008b39-9a69-4a65-b54d-bff3081cb626'
    redirect_uri = 'http://localhost/auth/avpass/callback'
    scope = 'openid email'
    response_type = 'code'
    prompt = 'login'
    auth_request_url = (f'{auth_endpoint}?client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}'
                        f'&response_type={response_type}&prompt={prompt}&state={state}&nonce={nonce}')

    # Redirect the user to the authorization request URL
    return redirect(auth_request_url)

@auth_blueprint.route('/avpass/callback', methods=['GET'])
def avpass_callback():
    # Verify the state parameter to prevent CSRF attacks
    if request.args.get('state') != '':
        return 'Invalid state parameter'

    # Exchange the authorization code for an access token and ID token
    token_endpoint = 'http://localhost:3000/oauth/api/user_info'
    client_id = '64008b39-9a69-4a65-b54d-bff3081cb626'
    client_secret = '271367673dc870f17dd253a8792b9d9b3ff76d252608d0906ac917e53ccfbaf3'
    redirect_uri = 'http://localhost/auth/avpass/callback'
    delete_uri = 'http://localhost:3000/oauth/delete'
    grant_type = 'authorization_code'
    code = request.args.get('code')
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {'client_id': client_id, 'client_secret': client_secret, 'auth_code': code}
    response = requests.post(token_endpoint, json = data)

    # Parse the access token and ID token from the response
    print(response.text)
    response_json = json.loads(response.text)
    username = response_json['username']
    email = response_json['email']
    email_verified = response_json['email_verified']

    # requests.delete(url = delete_uri, json={'auth_code': code})
    # Validate the ID token to ensure it came from AvPass and is not tampered with
    # You can use libraries like PyJWT or Authlib to help with this
    # Be sure to validate the nonce parameter to prevent replay attacks
    # You can use the nonce value saved in the session earlier to do this

    # Once the user is authenticated, you can redirect them to the appropriate page or return a response with the access token and ID token

    if current_user.is_authenticated:
        return {'status': 'You are already logged in!'}

    register_check = User.prisma().find_first(where={'email': email, 'emailVerified': email_verified, 'username': username})

    if register_check is not None:
        user = register_check
        login_user(UserModel(user))
        session.permanent = True
        return {'status': 'Login success!'}
    
    else:
        newdata = User.prisma().create(data={'email': email, 'emailVerified': email_verified, 'username': username})
        login_user(UserModel(newdata))
        session.permanent = True
        return {'status': 'Login success!'}
        return {'Username': f'{username}', 'Email': f'{email}', 'Email Verification Status': email_verified}