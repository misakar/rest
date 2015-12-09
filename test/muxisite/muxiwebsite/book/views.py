# coding: utf-8

"""
    views.py
    ~~~~~~~~

        木犀图书视图函数
        url                                        func
        /book                             主页 ; 显示:1.最近录入(6条)， 2.最近借阅
        /book/logout                      登出
        /bookin                           录入新书(只有管理员可见)
        /search                           站内搜索（支持两种模式）
        /search_results                   搜索结果页(提供借阅表单) 关于借阅状态
        /admin                            后台管理（只有管理员可见)
        /rter                             注册接口 (只有管理员可见)
        /<current_user>                   个人信息页(最近借阅)(快要到期 3天)
                      已过期的图书会flash消息提示
                           有情怀的flash提示
"""

from . import books
from .. import db
# from ..auth._decorate import auth_login
from werkzeug import secure_filename
from muxiwebsite.models import User, Book
from forms import BookForm, GetForm, LoginForm, RterForm
from flask import render_template, redirect, url_for, flash, request, session
from flask.ext.login import login_user, logout_user, login_required, current_user
from urllib2 import urlopen
import json
import datetime
import os

"""
                           ｜
              /------------/\-------------\
            /                              \
           |          木犀团队棒棒嗒         |
"""
# ------------------------------------------------------
#         """  我们在路上    前方不会太远 """
# ------------------------------------------------------


# 允许上传的文件扩展名
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    """检查文件扩展名函数"""
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


# 对所有访客可见
@books.route('/', methods=["POST", "GET"])
# @auth_login(redirect_url='user')
def home():
    """
    首页视图函数

        1. 最近录入
        2. 最近借阅

        new_book_list: 最近录入新书列表(默认为6本, 依据时间[id]排序)
    """
    form = LoginForm()
    new_book_list = Book.query.order_by('-id').all()[:9]
    get_book_list = Book.query.filter_by(status=True).order_by('start desc').all()[:2]

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
           login_user(user)
           return redirect(url_for('user', id=current_user.id))
        flash('用户名或密码错误!')

    range_book_count = range(len(new_book_list)/6 + 1)

    return render_template('home.html', new_book_list=new_book_list,
                           get_book_list=get_book_list, form=form,
                           range_book_count=range_book_count)


# 对所有访客可见
@books.route('/search', methods=["POST", "GET"])
def search():
    """
    搜索视图函数

        1. 搜索表单
        2. 显示搜索结果列表(最多加载5条搜索结果)

        搜索模式：
            1. 书名搜索（书名必须正确）
            2. 类别搜索（返回类别的图书：后台、前端、设计、互联网、其他）
    """
    if request.methos == 'POST':
        """前端 input 标签 action 实现重定向
           递交 search_results 处理"""
        pass


# 对所有访客可见
@books.route('/search_results/')
def search_results():
    """
    搜索结果页

        提供书籍借阅表单
    """
    get_book_list = []
    search = request.args.get('search')
    results = Book.query.whoosh_search(search, app.config['MAX_SEARCH_RESULTS'])

    for book in results[:]:
        """
        # 默认搜索结果全部为可借阅图书
        if request.args.get('range') == 'can':
            if book.status != True:
            # 跳过不可借阅图书
                get_book_list.append(book)
        if request.args.get('range') == 'all':
            get_book_list.append(book)
        """
        get_book_list.append(book)

    return render_template('search_results.html',
                           get_book_list=get_book_list,
                           search=search)


# 对所有访客可见，但只有登录用户可以借阅(html改动)
@books.route('/info/<name>', methods=["POST", "GET"])
def info(name):
    form = GetForm()
    book = Book.query.filter_by(name=name).first()
    if form.validate_on_submit():
        day = form.day.data
        if int(day) >= 0:
            start = datetime.datetime.now()
            book.start = start
            book.user_id = current_user.id
            book.status = True  # 已被借
            book.end = (start + datetime.timedelta(day)).strftime("%Y-%m-%d %H:%M:%S")
            return redirect(url_for('user', id=current_user.id))
        else:
            flash('光阴似箭、岁月如梭,时间－你不能篡改她，更不能逆转她!')
    return render_template('info.html', book=book, form=form)


# 只对管理员可见
@books.route('/rter', methods=["POST", "GET"])
@login_required
def rter():
    """用户注册接口"""
    if current_user.username == 'neo1218':
        form = RterForm()
        if form.validate_on_submit():
            u = User(username=form.username.data, password=form.password.data)
            db.session.add(u)
            db.session.commit()
        return render_template('r.html', form=form)
    else:
        return redirect(url_for('home'))


# 只对管理员可见
@books.route('/bookin', methods=["POST", "GET"])
@login_required
def bookin():
    """
    书籍录入

        输入书籍的名字，将书籍的

            书名， 封面， 简介 录入数据库
    """
    if current_user.username == 'neo1218':
        form = BookForm()

        if form.validate_on_submit():
            bookname = form.bookname.data
            get_url = "https://api.douban.com/v2/book/search?q=%s" % bookname
            resp_1 = json.loads(urlopen(get_url).read().decode('utf-8'))
            book_id = resp_1['books'][0]['id']
            url = "https://api.douban.com/v2/book/%s" % book_id
            resp_2 = json.loads(urlopen(url).read().decode('utf-8'))
            book = Book(url=url, name=resp_2['title'], author=resp_2['author'][0], \
                        tag=form.tag.data, summary=resp_2['summary'], \
                        image=resp_2['images'].get('large'), user_id=None, end=None, \
                        status=False)
            db.session.add(book)
            db.session.commit()
            flash('书籍已录入！')
            return redirect(url_for('bookin'))
        return render_template('bookin.html', form=form)
    else:
        return redirect(url_for('home'))


# 对所有登录用户可见
@books.route('/logout')
@login_required
def logout():
    """退出视图函数"""
    logout_user()
    return redirect(url_for('home'))


# 对登录用户可见
@books.route('/user/<int:id>', methods=["POST", "GET"])
def user(id):
    """
    用户个人信息页
        显示该用户历史借阅
        显示该用户快要过期的书（3天为界）

        提供用户还书按钮

        借阅图书默认按归还时间顺序排序
    """
    book_list = Book.query.filter_by(user_id=current_user.id).order_by('end').all()
    time_done_book = []
    time_dead_book = []

    for book in book_list:
        delta = (datetime.datetime.strptime(book.end, "%Y-%m-%d %H:%M:%S") - \
            datetime.datetime.now()).total_seconds()
        if delta <= 3*24*60*60 and delta > 0:
            time_done_book.append(book)
        if delta <= 0:
            time_dead_book.append(book)

    if request.method == "POST":
        """在前端input标签的重定向页面进行处理"""
        return redirect(url_for('book.user', id=current_user.id))

    books = Book.query.filter_by(name=request.args.get('back'), user_id=current_user.id).all()
    for book in books:
        book.status = False
        book.start = None
        book.end = None
        book.user_id = None
        flash('%s 已归还!' % book.name)
        return redirect(url_for('book.user', id=current_user.id))

    range_book_count = range(len(book_list)/3 + 1)
    range_timedonebook_count = range(len(time_done_book)/3 + 1)

    return render_template('user.html',
                           time_done_book=time_done_book[:2],
                           book_list=book_list,
                           range_book_count=range_book_count,
                           range_timedonebook_count=range_timedonebook_count,
                           session=session)


@books.route('/upload', methods=["POST", "GET"])
@login_required
def upload_file():
    """上传文件函数"""
    session['fileurl'] = 'http://127.0.0.1:5000/static/image/logo.png'
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            session['fileurl'] = 'http://121.0.0.1:5000/static/image/%s' % filename
            return redirect(url_for('user', username=current_user.username))
    return render_template('upload.html')
