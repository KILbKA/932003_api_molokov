from flask import Flask
from spyne.application import Application
from spyne.protocol.soap import Soap11
from spyne.decorator import srpc
from spyne.service import ServiceBase
from spyne.model.primitive import Unicode
from datetime import datetime

class TimeService(ServiceBase):
    @srpc(_returns=Unicode)
    def get_current_time():
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

app = Flask(__name__)
application = Application([TimeService], 'time.service', in_protocol=Soap11(), out_protocol=Soap11())

from spyne.server.wsgi import WsgiApplication
app.wsgi_app = WsgiApplication(application)

if __name__ == '__main__':
    app.run()