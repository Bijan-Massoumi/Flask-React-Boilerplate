from flask import Flask, send_from_directory

def create_app(config_filename):
    app = Flask(__name__, static_folder="./build/")
    app.config.from_object(config_filename)
    
    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    from Model import db
    db.init_app(app)

    return app


app = create_app("config")

@app.route('/')
def serve_react():
    return send_from_directory(app.static_folder, 'index.html')
 

if __name__ == "__main__":
    app.run(debug=True)
