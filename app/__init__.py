from flask import  Flask

app = Flask(__name__)

print('等会谁在使用我',__name__)

#从app包中导入模块routes
from app import routes