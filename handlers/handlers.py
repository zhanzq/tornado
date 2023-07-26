# encoding=utf-8
# created @2023/07/26
# created by zhanzq
#

import json
from abc import ABC

import tornado
from log.logger import logger


class ChatHandler(tornado.web.RequestHandler, ABC):
    def post(self):
        self.set_header("Content-type", "application/json")
        post_data = self.request.body
        data = json.loads(post_data)
        logger.info(f"post data: {data}")
        res = {
            "id": "ChatHandler",
            "res": "ChatHandler result"
        }

        self.write(json.dumps(res, ensure_ascii=False))
        return


class ClsHandler(tornado.web.RequestHandler, ABC):
    def post(self):
        self.set_header("Content-type", "application/json")
        post_data = self.request.body
        data = json.loads(post_data)
        logger.info(data)
        res = {
            "id": "ClsHandler",
            "res": "ClsHandler result"
        }

        self.write(json.dumps(res, ensure_ascii=False))
        return


class ModelHandler(tornado.web.RequestHandler, ABC):
    def get(self):
        logger.info("get method")

        res = {
            "id": "ModelHandler",
            "res": "ModelHandler result"
        }

        self.write(json.dumps(res, ensure_ascii=False))
        return
