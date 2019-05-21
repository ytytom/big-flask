# -*- coding:utf-8 -*-
from flask_restful import Resource, reqparse, request
from common.log import loggers
import json

logger = loggers()

# parser = reqparse.RequestParser()
# parser.add_argument("id", type=str, required=True, trim=True)
# parser.add_argument("action", type=str, required=True, trim=True)

class test(Resource):
    def get(self):
#        db = DB()
#        status , result = db.select("period_xingneng","")
#        logger("period_xingneng")
        logger.info("info message")
        return {"status": True, "message": "start task success !" ,"data": "result"}
