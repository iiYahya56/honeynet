from honeynet import web_server, logger, config

if __name__ == '__main__':
    logger.init_db()
    web_server.app.run(host=config.HOST, port=config.PORT)
