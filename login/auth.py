from flask import request, session, redirect
from app import  models

class Auth(object):

    def __init__(self, app=None):
        self.app = app
        if app:
            # 实例化时完成注册
            self.init_app(app)

    def init_app(self, app):
        # 也可手动完成注册过程
        app.auth_manager = self  # 将自身添加进app中

        self.app = app
        app.before_request(self.check_login)  # 添加一个before_request
        app.context_processor(self.context_processor)  # 向模板中添加新的变量

    def check_login(self):
        """
        检查用户是否已经登录
        :return:
        """
        withe_list = ['/login', '/getimg', '/get_email', '/register']
        if request.path in withe_list:
            return

        user = session.get('user')
        if not user:
            return redirect('/login')

        else:
            user = models.db.session.query(models.User).filter_by(id = user.get("id")).first()
            # print(user)
            request.user = user

    def context_processor(self):
        user = session.get('user')
        return dict(current_user=user)

    def login(self, data):
        """
        将用户登录信息，放入session
        :param data:
        :return:
        """
        session['user'] = data


    def logout(self):
        """
        将用户登录信息，放入session
        :param data:
        :return:
        """
        del session['user']