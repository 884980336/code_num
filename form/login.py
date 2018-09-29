from wtforms import Form
from wtforms.fields import simple,core,html5 # 字段来自于这里
from wtforms import validators # 验证规则来自于这里
from wtforms import widgets # 工具是在这里

# from flask import app
from flask import session
class Login(Form):
    email = simple.StringField(
                          label="邮箱",
                          validators=[validators.DataRequired(message='用户名不能为空.'),validators.Email(message='请输入正确格式')],
                          widget=widgets.TextInput(),
                          render_kw={"class": "form-control",'placeholder':"请输入邮箱"}
                          )
    pwd = simple.StringField(label="密码",
                             validators=[validators.DataRequired(message='密码不能为空.')],
                          widget=widgets.PasswordInput(),
                          render_kw = {"class": "form-control",'placeholder':"请输入密码"}
                          )

    valid_code = simple.StringField(
                          label="验证码",
                          validators=[validators.DataRequired(message='不能为空.')],
                          widget=widgets.TextInput(),
                          render_kw={"class": "form-control",'placeholder':"请输入验证码"}
                          )

    def validate_valid_code(self, field):
        # print(app)
        valid_code = session.get('random_code_str')
        if field.data.upper() != valid_code.upper():
            raise validators.StopValidation("验证码错误")