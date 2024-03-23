from flask import render_template
from myapp import app
from API.controller import nhan_vien

app.register_blueprint(nhan_vien)
if __name__ == "__main__":
    app.run(debug=True)