from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,SelectField,TextAreaField,FileField,IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
import phonenumbers

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',validators=[DataRequired(),Length(min=5,max=30)])
    
    submit = SubmitField('Login')


class RegisterationForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    firstname = StringField('First Name',validators=[DataRequired(),Length(min=5,max=30)])
    lastname = StringField('Last Name',validators=[DataRequired(),Length(min=5,max=30)])
    phone = StringField('Phone Number', validators=[DataRequired()])

    password = PasswordField('Password',validators=[DataRequired(),Length(min=5,max=30)])
    gender_choices = ([('Male','Male'),('Female','Female')])

    gender = SelectField('Gender',
                        choices=gender_choices)
    age = StringField('Age',validators=[DataRequired()])

    submit = SubmitField('Register')

    def validate_phone(form, field):
        if len(field.data) > 16:
            raise ValidationError('Invalid phone number.')
        try:
            input_number = phonenumbers.parse(field.data)
            if not (phonenumbers.is_valid_number(input_number)):
                raise ValidationError('Invalid phone number.')
        except:
            input_number = phonenumbers.parse("+1"+field.data)
            if not (phonenumbers.is_valid_number(input_number)):
                raise ValidationError('Invalid phone number.')