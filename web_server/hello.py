"""
============================
Author:古一
Time:2020/8/14
E-mail:369799130@qq.com
============================
"""

from flask import Flask, request, session
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://hogwarts_python:hogwarts_python@stuq.ceshiren.com/hogwarts_python'
db = SQLAlchemy(app)
app.config['JWT_SECRET_KEY'] = 'testing'
jwt = JWTManager(app)


class User(db.Model):
    __tablename__ = 'user_listen'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class Cases(db.Model):
    __tablename__ = 'cases_listen'
    case_id = db.Column(db.Integer, primary_key=True)
    case_title = db.Column(db.String(80), unique=True, nullable=False)
    case_precondition = db.Column(db.String(80), unique=False, nullable=False)
    case_steps = db.Column(db.String(120), unique=False, nullable=False)
    case_expected = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return '<Cases %r>' % self.case_title


class Projects(db.Model):
    __tablename__ = 'user_listen'
    p_id = db.Column(db.Integer, primary_key=True)
    p_name = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<Project %r>' % self.p_name



class Login(Resource):

    @jwt_required
    def get(self):
        """查询登录信息"""
        return {'data': 'this is a get request'}

    def post(self):
        """登录"""
        user = User.query.filter_by(username=request.form['username'], password=request.form['password']).first()
        if user is None:
            return {"data": "", "errcode": 0}
        else:
            access_token = create_access_token(identity=user.username)
            return {"data": {
                'username': user.username,
                'email': user.email,
                "token": access_token
            },
                "errcode": 1,
            }

    @jwt_required
    def logout(self):
        """注销"""
        session.clear()
        return '666'




class Case(Resource):
    def get(self, case_id):
        """查询某条用例"""
        case = Cases.query.filter_by(case_id=case_id).first()
        return {
            "data": {
                'case_title': case.case_title,
                'case_precondition': case.case_precondition,
                'case_steps': case.case_steps,
                'case_expected': case.case_expected
            }

        }

    def put(self, case_id):
        """更新用例"""
        case = Cases.query.filter_by(case_id=case_id).first()
        case.case_title = 'xiugai'
        return {'msg': '修改成功'}

    def delete(self, case_id):
        case = Cases.query.filter_by(case_id=case_id).delete()
        print(case.case_id, type(case.case_id))
        return {"msg": f"用例{case.case_id}删除成功"}


class CaseList(Resource):
    def get(self):
        """查询所有用例"""
        case_list = Cases.query.all()
        return {"data": f"{case_list}"}

    def post(self):
        """新增用例"""
        case = Cases(case_title=request.form.get('case_title'),
                     case_precondition=request.form.get('case_precondition'),
                     case_steps=request.form.get('case_steps'),
                     case_expected=request.form.get('case_expected'))
        db.session.add(case)
        db.session.commit()
        return {"msg": "用例添加成功"}

class Project(Resource):
    def get(self, p_id):
        """查询某个项目"""
        project = Projects.query.filter_by(p_id=p_id).first()
        return {
            "data": {
                'p_name': project.p_name
            }

        }

    def put(self, p_id):
        """更新项目"""
        project = Projects.query.filter_by(p_id=p_id).first()
        project.p_name = 'xiugai'
        return {'msg': '修改成功'}

    def delete(self, p_id):
        Projects.query.filter_by(p_id=p_id).delete()
        return {"msg": "删除成功"}


class ProjectList(Resource):
    def get(self):
        """查询所有项目"""
        project_list = Projects.query.all()
        return {"data": f"{project_list}"}

    def post(self):
        """新增项目"""
        project = Projects(p_name=request.form['p_name'])
        db.session.add(project)
        db.session.commit()
        return {"msg": "项目添加成功"}

api.add_resource(Login, '/login', '/logout')
api.add_resource(CaseList, '/cases')
api.add_resource(Case, '/cases/<case_id>')
api.add_resource(ProjectList,'/projects')
api.add_resource(Project, '/projects/<p_id>')


if __name__ == '__main__':
    app.run(debug=True)
