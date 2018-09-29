from PIL import ImageDraw, ImageFont, Image # pillow
from io import BytesIO
import datetime
import random
import shutil
import os


from flask import Blueprint, render_template, request, session, redirect
from flask.ext.mail import Message
from form import login, register


from app import email, db, models, auth
import count_tools

RECV_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "recv_file")

us = Blueprint("app01", __name__)

@us.route("/")
def home():
    return render_template("home.html")

@us.route("/count", methods=["GET", "POST"])
def count():
    if request.method == "POST":
        file_obj = request.files.get("file")
        file_path = os.path.join(RECV_DIR, datetime.date.today().strftime("%Y_%m_%d"),
                                       session.get("user").get("name"))
        file_name = os.path.join(file_path, file_obj.filename)
        try:
            shutil.rmtree(file_path)
        except FileNotFoundError:
            pass
        if not os.path.isdir(file_path):
            os.makedirs(file_path)
        file_obj.save(file_name)
        file_type = file_obj.filename.split(".")[-1].capitalize()
        if hasattr(count_tools, file_type):
            count = getattr(count_tools, file_type)(file_name).line_count()
            info = db.session.query(models.Code_count).filter_by(user = request.user.id,
                                                       data = datetime.date.today()).first()
            if info:
                info.count = count
                db.session.commit()
            else:
                clsobj = models.Code_count(user=request.user.id,count=count)  # 实例化类
                db.session.add(clsobj)  # 通过session将clsobj添加进数据库中
                # 上面并不需要指定库,因为clsobj是Classes的实例,他们存在着对应关系
                db.session.commit()  # 提交
            return "ok"
        else:
            return "bu ok"

    my = db.session.query(models.Code_count).filter_by(user = request.user.id).all()[::-1]
    # my_cls = db.session.query(models.Code_count).filter(
    #     models.Code_count.user.cls.id == request.user.cls.id,
    #     models.Code_count.data == datetime.date.today()).all()
    # print(request.user.cls)
    my_cls = db.session.query(models.Code_count.user,
                              models.Code_count.count,
                              models.Code_count.data,
                              models.User.cls,
                              models.User.name
                              ).join(models.User,isouter=True).filter(
        models.Code_count.data == datetime.date.today(),
        models.User.cls == request.user.cls
    ).all()
    top10 = db.session.query(
                              models.Code_count.count,
                              models.Code_count.data,
                              models.User.name,
                                models.Cls.name.label('cname')
                              ).join(models.User,models.Cls,isouter=True).filter(
        models.Code_count.data == datetime.date.today(),
    ).order_by(models.Code_count.count.desc())[:9]
    print(top10[0].cname)
    return render_template("index.html", my=my, my_cls=my_cls, top10=top10)


@us.route("/login", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        form = login.Login()

        return render_template("login.html", form=form)
    else:
        form = login.Login(formdata=request.form)
        if form.validate():
            # 验证通过,打印数据
            mail = request.form.get("email")
            pwd = request.form.get("pwd")
            user = db.session.query(models.User).filter(models.User.email==mail, models.User.password==pwd).all()
            if user:
                name = user[0].name
                id = user[0].id
                auth.login({"name":name,"id":id})
                return redirect("/")
            form.pwd.errors.append("邮箱或密码错误")
            return render_template("login.html", form=form)
        return render_template("login.html", form=form)


@us.route("/register", methods=["GET", "POST"])
def register_func():
    if request.method == "GET":
        form = register.Register()
        return render_template("register.html", form=form)
    else:
        form = register.Register(formdata=request.form)
        if form.validate():
            # 验证通过,打印数据
            name = form.data.get("user")
            pwd = form.data.get("pwd")
            email = form.data.get("email")
            phone_num = form.data.get("phone_num")
            cls = form.data.get("cls")
            print(name, phone_num, cls)
            auth = db.session.query(models.Cls_Stu).filter(models.Cls_Stu.name == name,
                                                           models.Cls_Stu.phone_num == phone_num,
                                                           models.Cls_Stu.cls == cls).all()
            if auth:
                user_obj = models.User(name=name, password=pwd,
                                       email=email, cls=cls,
                                       phone_num=phone_num)
                db.session.add(user_obj)
                db.session.commit()

                return redirect("/login")

            form.cls.errors.append("用户验证失败, 请检查信息或联系管理员")
            return render_template("register.html", form=form)
        else:
            return render_template("register.html", form=form)

@us.route("/getimg")
def get_img():
    # 生成随机颜色
    def get_random_color():
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes
    f = BytesIO()
    # 创建新的图片,指定打下颜色
    image = Image.new(mode="RGB", size=(160, 35), color=get_random_color())
    # 创建一个可以在给定图像上绘图的对象。
    draw = ImageDraw.Draw(image)
    # 设置字体及大小
    font = ImageFont.truetype("fonts/kumo.ttf", size=36)

    temp = []
    for i in range(5):
        # 生成随机字符
        random_char = random.choice(
            [str(random.randint(0, 9)), chr(random.randint(65, 90)), chr(random.randint(97, 122))])
        # 将字符绘入图片
        draw.text((i * 30, 0), random_char, get_random_color(), font=font)
        # 将字符添加进列表中
        temp.append(random_char)

    width = 120
    height = 80
    for i in range(50):
        x = random.randint(0, width)
        y = random.randint(0, height)
        # 绘制弧
        draw.arc((x, y, x + 4, y + 4), 0, 90, fill=get_random_color())
    # 将图片数据写入f
    image.save(f, "png")
    # 读取f
    data = f.getvalue()
    # 设置session,保存为浏览器发送的随机字符
    session["random_code_str"] = "".join(temp)
    return data


@us.route("/get_email", methods=["GET", "POST"])
def get_email():
    auth = ''.join(random.sample(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'], 6))
    recv_email = request.form.get("email")
    msg = Message(subject="账号注册",
                  sender="884980336@qq.com",
                  recipients=[recv_email])
    msg.body = 'text body'
    msg.html = '您的验证码为%s'%auth
    email.send(msg)
    session["mail"] = auth
    return "已发送"

@us.route("/logout")
def logout():
    auth.logout()
    return redirect("/")