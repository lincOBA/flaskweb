#-*- coding:utf-8 -*-
from app import app

OPEN = False
if OPEN:
    app.run(port=9999,host='0.0.0.0')
else:
    app.run(debug = True, port=9999)
