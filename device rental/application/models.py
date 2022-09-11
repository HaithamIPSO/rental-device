
from application import db,login_manager,ma
from flask_login import UserMixin


@login_manager.user_loader
def load_user(id):
        
    return Users.query.get(int(id))


class Users(db.Model,UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(100),nullable=False)
    firstname = db.Column(db.String(100),nullable=False)
    lastname = db.Column(db.String(100),nullable=False)
    password= db.Column(db.String(200),nullable=False)
    gender= db.Column(db.String(100),nullable=False)
    age= db.Column(db.String(100),nullable=False)
    phone_number= db.Column(db.String(100),nullable=False)

    is_admin = db.Column(db.Integer,nullable=True)



class Devices(db.Model):
    device_id = db.Column(db.Integer(), primary_key=True)
    DeviceName = db.Column(db.String(300))
    Manufacture = db.Column(db.String(300))
    ProductType = db.Column(db.String(300))
    OS = db.Column(db.String(300))


class Reservation(db.Model):
    reserve_id = db.Column(db.Integer(), primary_key=True)
    client_id = db.Column(db.ForeignKey('users.id'))
    device_id = db.Column(db.ForeignKey('devices.device_id'))
    reserve_date = db.Column(db.Date(),nullable=True)
    pickup_date = db.Column(db.Date(),nullable=True)
    return_date = db.Column(db.Date(),nullable=True)
    reason = db.Column(db.String(1000),nullable=True)
    status = db.Column(db.String(100),nullable=True)

class ReservationSchema(ma.Schema):
    class Meta:
        fields = ("reserve_id",'client_id','device_id','reserve_date','pickup_date','return_date','reason','status','id','firstname','lastname','DeviceName')
