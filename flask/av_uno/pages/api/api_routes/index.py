from flask import Blueprint, request

home_route = Blueprint('api_home', __name__,
                        template_folder='templates')

@home_route.route('/')
def index():
    return {'Message': f'Welcome to the aviance API. Your IP address is: {request.remote_addr}'}