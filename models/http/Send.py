from models.http.base.BaseHttpModel import *


class Send(BaseHttpModel):
    url = 'https://qa3.helsi.me/api/healthy/send?debug=true'

    def __init__(self):
        BaseHttpModel.__init__(self)
        pass

    def send_request(self, payload):
        BaseHttpModel.send_request(self, payload, "post")