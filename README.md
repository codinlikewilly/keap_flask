Quick Setup:
    * There must be a logs directory under the root of your project. (Unless custom logger is passed)
    * There must be a cache directory under the root of your project. (Unless a custom cache class is passed)
    * Pip install keap-flask
    * from keap_flask.keapclient import KeapClient
    * Initialize with: keap = KeapClient(app=app)
    * Flask app must have three config variables set:
        - 1: KEAP_CLIENT_ID: The Client ID setup on keys.infusionsoft.com
        - 2: KEAP_CLIENT_SECRET: The Client Secret obtained when you setup your client on keys.infusionsoft.com
        - 3: AUTH_APP_BASE_URL: The Base URL of your application. Make sure to include trailing slash.
    
    * Notes:
        - https must be used. I use --cert=adhoc option when testing 
        - app is a required argument when initializing

    * Custom Auth Handler Class:
        * A custom Auth Handling class can be used by passing it as an arg upon initialization. 
        * Your Auth class must contain the following methods:
            - get_authorization: returns auth
            - update_authorization: updates stored auth

    * Authorizing
        - A blueprint is added to the flask app. It adds the following:
            - Authorization Route: '/authorize-keap'
                * ex: yoursite.com/authorize-keap
                * this is where you will authorize your application
        - A CLI command for refreshing auth should the autorefresh fail.: 
        - Command: 'flask keap refresh-auth'
        