from app import db, app
from app.models import *
with app.app_context():
    db.create_all()
    # a = db.session.
    # for i in a:
    #     print(i)
    # print(list(a))
    # auth = db.session.query(Cls_Stu).filter(Cls_Stu.cls == "1", Cls_Stu.name == "").all()
    # print(auth)
