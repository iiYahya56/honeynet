from honeynet import web_server, ssh_emulator, logger, config
from threading import Thread

if __name__ == '__main__':
    logger.init_db()
    
    # Run Flask app in a thread
    t1 = Thread(target=web_server.app.run, kwargs={
        'host': config.HOST,
        'port': config.PORT
    })
    t1.start()

    # Run SSH emulator
    ssh_emulator.run_ssh_emulator()
