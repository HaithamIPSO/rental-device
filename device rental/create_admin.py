from application import db
from application.models import Users
from werkzeug.security import generate_password_hash,check_password_hash

user = Users.query.filter_by(is_admin=1).first()
hash_pw = generate_password_hash('Admin.66')

if user:
    pass
else:
    admin = Users(email='admin@ipso.com',password=hash_pw,is_admin=1,firstname="Admin",lastname="admin",phone_number="+222222",gender="Male",age=23)
    db.session.add(admin)
    db.session.commit()




    