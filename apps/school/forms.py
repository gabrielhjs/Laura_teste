from wtforms import Form, IntegerField, StringField, validators, DateTimeField


class FormUserCreate(Form):
    """
    Form de validação dos dados de cadastro de novo usuário
    """

    name = StringField("name", [validators.DataRequired()])
    age = IntegerField("age", [validators.DataRequired()])
    ra = IntegerField("ra", [validators.DataRequired()])
    campus = StringField("campus", [validators.DataRequired(), validators.Length(min=2, max=2)])
    county = StringField("county", [validators.DataRequired()])
    course = StringField("course", [validators.DataRequired()])
    modality = StringField("modality", [validators.DataRequired()])
    level = StringField("level", [validators.DataRequired()])
    start_date = DateTimeField("start_date", [validators.DataRequired()], format="%Y-%m-%d")


class FormUserDelete(Form):
    """
    Form de validação dos dados de exclusão de usuário com curso
    """

    ra = IntegerField("ra", [validators.DataRequired()])
    campus = StringField("campus", [validators.DataRequired(), validators.Length(min=2, max=2)])
