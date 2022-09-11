from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,SelectField,TextAreaField,FileField,IntegerField,DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
import phonenumbers

class BookDeviceForm(FlaskForm):
    ReserveDate = DateField('Reserve Date',
                        validators=[DataRequired()])
                        
    ReturnDate = DateField('Return Date',
                        validators=[DataRequired()])

    PickupDate = DateField('Pickup Date',
                        validators=[DataRequired()])
    Reason = TextAreaField('Reason',
                        validators=[DataRequired()])
    
    submit = SubmitField('Submit')



