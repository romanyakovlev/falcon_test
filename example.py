# things.py


import falcon
import json


class WorkersResource(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200
        resp.body = json.dumps({
            'worker_1':{1:40, 2:32},
            'worker_2':{1:42, 2:65},
        })

app = falcon.API()
workers = WorkersResource()
app.add_route('/workers', workers)
