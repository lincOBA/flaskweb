from app import db
ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), unique = True)
    email = db.Column(db.String(120), unique = True)
    role = db.Column(db.SmallInteger, default = ROLE_USER)
    posts = db.relationship('Post', backref = 'author', lazy = 'dynamic')   
    def __repr__(self):
        return '<User %r>' % (self.nickname)
    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return unicode(self.id)
    @classmethod
    def login_check(cls, user_name,user_pwd = '123'):
        user = cls.query.filter(db.or_(User.nickname == user_name,User.email == user_pwd)).first()
        if not user:
            return None
        return user
    

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)
class uUser(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), unique = True)
    password = db.Column(db.String(20))
    role = db.Column(db.SmallInteger, default = ROLE_USER)
    def __repr__(self):                                                     
        return '<User %r>' % (self.nickname)
    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return unicode(self.id)
    @classmethod
    def login_check(cls, user_name,user_pwd = '123'):
        user = cls.query.filter(db.and_(uUser.nickname == user_name,uUser.password== user_pwd)).first()
        return user


class Testt(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    times = db.Column(db.String(120))

class lv(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(140), unique = True)
    department = db.Column(db.String(140))
    job = db.Column(db.String(140))
    time1 = db.Column(db.String(140))
    time2 = db.Column(db.String(140))
    genre = db.Column(db.String(140))
    reason = db.Column(db.String(600))

class Msg(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(140),unique = True)
    msg = db.Column(db.String(300))
    time = db.Column(db.String(150))

class Message(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(140))
    msg = db.Column(db.String(300))
    time = db.Column(db.String(150))
