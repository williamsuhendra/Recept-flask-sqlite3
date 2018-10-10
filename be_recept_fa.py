import json, falcon, datetime
from functions import directorylist, lookforfileurl, lookforafile
from utils import JSONTranslator

switcher = {
    'get-recept': sel_recept,
    'get-ingridient': sel_ingridient,
    'get-kookgerei': sel_kookgerei,
    'get-bereiding': sel_bereiding,
    'post-recept': mod_recept,
    'post-ingridient' : mod_ingridient,
    'post-kookgerei' : mod_kookgerei,
    'post-bereiding' : mod_bereiding,
}


def runcommand(argument, param):
    # Get the function from switcher dictionary
    func = switcher.get(argument, "nothing")
    # Execute the function
    return func(param)


class ObjRequestClass:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        data = req.context['request']
        output = runcommand(data['method'], data['param'])
        message = {}
        message['result'] = output
        resp.context['response'] = message

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200
        data = req.context['request']
        output = runcommand(data['method'], data['param'])
        message = {}
        message['result'] = output
        resp.context['response'] = message


api = falcon.API(middleware=[JSONTranslator(), ])
api.add_route("/api_run", ObjRequestClass())