from wtforms import Form
from wtforms.fields import simple, core
from wtforms import validators
from wtforms import widgets

from app import db, models
from flask import session
class Register(Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cls.choices = list(db.session.execute("select id, name from cls"))

    user = simple.StringField(label="姓名",
                              validators=[validators.DataRequired(message='用户名不能为空.'),validators.Length(min=2,max=4,message="长度错误")],
                              render_kw={"class": "form-control",'placeholder':"请输入用户名"}
                          )
    pwd = simple.StringField(label="密码",
                             validators=[validators.DataRequired(message='密码不能为空.')],
                          widget=widgets.PasswordInput(),
                          render_kw = {"class": "form-control",'placeholder':"请输入密码"}
                          )
    pwd1 = simple.StringField(label="确认密码",
                             validators=[validators.DataRequired(message='密码不能为空.')],
                          widget=widgets.PasswordInput(),
                          render_kw = {"class": "form-control",'placeholder':"请输入密码"}
                          )
    email = simple.StringField(
                          label="邮箱",
                          validators=[validators.DataRequired(message='不能为空.'),validators.Email(message='请输入正确格式')],
                          widget=widgets.TextInput(),
                          render_kw={"class": "form-control",'placeholder':"请输入邮箱"}
                          )


    valid_code = simple.StringField(
                          label="验证码",
                          validators=[validators.DataRequired(message='不能为空.')],
                          widget=widgets.TextInput(),
                          render_kw={"class": "form-control",'placeholder':"请输入验证码"}
                          )

    phone_num = simple.StringField(label="手机号",
                              validators=[validators.DataRequired(message='不能为空.'),
                                          validators.Length(min=11, max=11, message="长度错误")],
                              render_kw={"class": "form-control", 'placeholder': "请输入用户名"}
                              )

    cls = core.SelectField(
        label='班级',
        choices=[],
        coerce=int,
        render_kw = {"class": "form-control",}
    )


    def validate_pwd1(self, field):
        pwd = self.data.get("pwd")
        pwd1 = field.data
        if pwd != pwd1:
            raise validators.StopValidation("两次密码不一致")


    def validate_valid_code(self, field):
        valid_code = self.data.get("valid_code")
        if session.get("mail") != valid_code:
            raise validators.StopValidation("验证码错误")

