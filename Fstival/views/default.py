from pyramid.response import Response
from pyramid.view import view_config
from pyramid.renderers import render_to_response

from sqlalchemy.exc import DBAPIError

from ..models import MyModel
from ..models import User
from ..models import Comment

import hashlib
import datetime
import time

uname = "admin"
@view_config(route_name='home', renderer='../templates/homepage.jinja2')
def my_view(request):
    try:
        query = request.dbsession.query(MyModel)
        one = query.filter(MyModel.name == 'one').first()
    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    return {'one': one, 'project': 'foss-blog'}

@view_config(route_name='log', renderer='../templates/login.jinja2')
def my_login(request):
    return {}

@view_config(route_name='user', renderer='../templates/userpage.jinja2')
def my_user(request):
    global uname
    uname = request.params['username']
    pwd = request.params['pswd']
    hash_obj = hashlib.md5(pwd.encode())
    m = hash_obj.hexdigest()
    query = request.dbsession.query(User)
    one = query.filter(User.username == uname, User.password == m).first()
    if one:
        return {'one': one}
    else:
        return Response("<h3>Check user name and password&nbsp;&nbsp;&nbsp;&nbsp;<a href='/login'>Login</a></h3>")

@view_config(route_name='post', renderer='../templates/post.jinja2')
def my_post(request):
    global user
    query = request.dbsession.query(User)
    one=query.filter(User.username == uname).first()
    return {'one':one}

@view_config(route_name='view', renderer='../templates/view.jinja2')
def my_comment(request):
    global user
    query = request.dbsession.query(User)
    one=query.filter(User.username == uname).first()
    return {'one':one}

@view_config(route_name='signup', renderer='../templates/signup.jinja2')
def my_signup(request):
    return {}

@view_config(route_name='account', renderer='../templates/userpage.jinja2')
def my_account(request):
    global user
    query = request.dbsession.query(User)
    one=query.filter(User.username == uname).first()
    return {'one':one}



@view_config(route_name='register', renderer='../templates/login.jinja2')
def signup1(request):
    global uname
    uname = request.params['username']
    pwd = request.params['pswd']
    query = request.dbsession.query(User)
    one = query.filter(User.username == uname).all()
    hash_obj = hashlib.md5(pwd.encode())
    m = hash_obj.hexdigest()
    length=len(one)
    if one:
        return Response("<h3>'Username '+user+' already exists . Try another name.'&nbsp;&nbsp;&nbsp;&nbsp;<a href='/signup'>Signup</a></h3>")
    else:
        model = User(username = uname, password = m)
        request.dbsession.add(model)
        return {'one': one}

@view_config(route_name='postcomment', renderer='../templates/post.jinja2')
def postdb(request):
    global uname
    email = request.params['email']
    topic = request.params['topic']
    cmt = request.params['comment']
    tdy = datetime.date.today()
    query = request.dbsession.query(User)
    one = query.filter(User.username == uname).all()
    model = Comment(email = email, topic = topic,comment = cmt,datetime = tdy)
    request.dbsession.add(model)
    return render_to_response('../templates/post.jinja2',{'message':'Updated succesfully!!','one':one},request=request)


@view_config(route_name='viewcomment', renderer='../templates/view.jinja2')
def viewcomment(request):
	obj=request.dbsession.query(Comment).filter().order_by(desc(Comment.datetime)).all()
	return {'length':len(obj),'obj':obj}

db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:
1.  You may need to run the "initialize_foss_db" script
    to initialize your database tales.  Check your virtual
    environment's "bin" directory for this script and try to run it.
2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.
After you fix the problem, please restart the Pyramid application to
try it again.
"""
