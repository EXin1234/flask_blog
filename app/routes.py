#app包里导入app对象
from app import app

#2个路由
@app.route('/')
@app.route('/index')

#1个视图函数
def index():
    return "Hello,World!"
