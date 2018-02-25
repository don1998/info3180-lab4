from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed



class UploadForms(FlaskForm):
     File = FileField(validators=[FileRequired(),FileAllowed(['jpg', 'png', 'Images only!'])])