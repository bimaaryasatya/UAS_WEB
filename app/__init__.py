from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Import routes setelah inisialisasi app untuk menghindari circular import
    from . import routes
    
    return app