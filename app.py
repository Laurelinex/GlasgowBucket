from flask import Flask, render_template

from controllers.zones_controller import zones_blueprint
from controllers.locations_controller import locations_blueprint

app = Flask(__name__)

app.register_blueprint(zones_blueprint)
app.register_blueprint(locations_blueprint)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

# @app.route("/bucket")
# def bucket():
#     return render_template('bucket.html')

if __name__ == '__main__':
    app.run()