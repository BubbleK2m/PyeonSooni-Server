import os


class Config:
    DEBUG = False
    REMOTE_HOST = 'pyeonsooni.herokuapp.com'

    HOST = 'localhost'
    PORT = int(os.getenv('PORT', 5000))

    SERVICE_NAME = 'pyeonsooni'
    SECRET = os.getenv('SECRET_KEY', '78OC34B1ABC11263A357R8FBM99Y7221D7DB')

    SWAGGER = {
        'title': SERVICE_NAME,
        'specs_route': os.getenv('SWAGGER_URI', '/docs/'),
        'uiversion': 3,

        'info': {
            'title': SERVICE_NAME + ' API',
            'version': '1.0',
            'description': '편순이 서버 API Spec'
        },

        'schemes': [
            'https'
        ],

        'host': '{}'.format(REMOTE_HOST) if REMOTE_HOST else None,
        'basepath': '/'
    }

    if REMOTE_HOST is None:
        SWAGGER['host'] = '{0}{1}'.format(HOST, PORT)

    MONGO = {
        'host': 'ds155699.mlab.com',
        'port': 55699,
        'db': '{}'.format(SERVICE_NAME),
        'username': 'gdh0608',
        'password': 'kim0608'
    }

    GOOGLE_MAPS = {
        'api_key': 'AIzaSyDeOFSfSpQkihFYYNRYh5MZr1U-qNysmBU'
    }

