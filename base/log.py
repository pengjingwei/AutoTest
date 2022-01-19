import logging

file = open(r'./logger', encoding='utf-8', mode='a')
logging.basicConfig(
    level=logging.INFO,
    stream=file,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filemode='a'
)


console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)


def log(func):
    def wrapper(*args, **kwargs):
        info = func.__doc__
        logging.info('testing at : %s' % info)
        return func(*args, **kwargs)

    return wrapper


def errorLog(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            logging.getLogger().exception('Exception')
            exit()

    return wrapper


def consoleLog(info, level='INFO'):
    if level == 'INFO':
        logging.info(info)
    elif level == 'WARNING':
        logging.warning(info)
    elif level == 'ERROR':
        logging.error(info)
