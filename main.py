# encoding=utf-8
# created @2023/07/26
# created by zhanzq
#

import logging
import tornado
from handlers.handlers import ClsHandler, ChatHandler, ModelHandler

from log.logger import logger


def make_app():
    return tornado.web.Application([
        ("/cls", ClsHandler),
        ("/chat", ChatHandler),
        ("/model", ModelHandler),
    ])


if __name__ == "__main__":
    ip = "127.0.0.1"
    port = 9000
    num_processes = 1
    app = make_app()
    httpserver = tornado.httpserver.HTTPServer(app)
    httpserver.listen(port)
    httpserver.start(num_processes=num_processes)
    logger.info("server start success")
    logger.info(f"address {ip}:{port}")
    tornado.ioloop.IOLoop.instance().start()
