from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,SelectField,TextAreaField,FileField,IntegerField,DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
import phonenumbers

class AddDeviceForm(FlaskForm):
    DeviceName = StringField('Device Name',
                        validators=[DataRequired()])
                        
    Manufacture = StringField('Manufacture',
                        validators=[DataRequired()])

    ProductType = StringField('Product Type',
                        validators=[DataRequired()])
    OS = StringField('OS',
                        validators=[DataRequired()])
    
    submit = SubmitField('Add')



