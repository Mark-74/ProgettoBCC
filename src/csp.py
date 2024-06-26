from flask import Flask, Response

def init_app(app: Flask):
    """
    Initializes the Flask app with a Content Security Policy (CSP) header.

    Args:
        app (Flask): The Flask app to initialize.

    Returns:
        None
    """
    @app.after_request
    def csp(response: Response):
        response.headers['Content-Security-Policy'] = '; '.join([
            "style-src 'self' 'unsafe-inline' cdnjs.cloudflare.com",
            "script-src 'self' cdn.jsdelivr.net"
        ])
        return response
    pass
