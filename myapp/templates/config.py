from myapp import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'dunga3k46pbc2002'
app.config['MYSQL_DATABASE_DB'] = 'cskh'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)