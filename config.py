import os
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

CSRF_ENABLED = True
SECRET_KEY = 'shi-yan-lou'

if __name__ == '__main__':
	print SQLALCHEMY_DATABASE_URI
	print SQLALCHEMY_MIGRATE_REPO
