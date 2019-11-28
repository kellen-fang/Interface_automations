# coding: utf-8


import logging, os, time


# 定义日志级别
LEVELS = {
    "debug": logging.DEBUG,
    "info": logging.INFO,
    "warning": logging.WARNING,
    "errot": logging.ERROR,
    "critical": logging.CRITICAL
}

logger = logging.getLogger()
level = "default"

# 创建日志文件
def create_file(file_name):
    file_path = file_name[0:file_name.rfind("/")]
    # 判断文件路径是否存在
    if not os.path.isdir(file_path):
        os.makedirs(file_path)
    # 判断文件是否存在
    if not os.path.isfile(file_name):
        fp = open(file_name, mode="w", encoding="utf-8")
        fp.close()

# 定义日志集合
def set_handler(levels):
    # 判断levels是否等于error，是，添加集合
    if levels == "error":
        logger.addHandler(create_mylog.err_handler)
    logger.addHandler(create_mylog.handler)

# 移除日志集合
def remove_handler(levels):
    # 判断levels是否等于error，是，移除集合
    if levels == "error":
        logger.removeHandler(create_mylog.err_handler)
    logger.removeHandler(create_mylog.handler)

# 定义日志的时间格式
def get_current_time():
    date_time = time.strftime(create_mylog.date, time.localtime(time.time()))
    return date_time


# 封装log的方法
class create_mylog:
    log_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    log_file = log_path + "/log/log.log"
    err_file = log_path + "/log/err.log"
    # 设置日志等级格式
    logger.setLevel(LEVELS.get(level, logging.NOTSET))
    create_file(log_file)
    create_file(err_file)
    date = "%Y-%m-%d %H:%M:%S"
    # 定义日志文件目录及文件名称
    handler = logging.FileHandler(log_file, encoding="utf-8")
    err_handler = logging.FileHandler(err_file, encoding="utf-8")

    @staticmethod
    def debug(log_meg):
        set_handler("debug")
        logger.debug("[DEBUG:" + get_current_time() + "]:" + log_meg)
        remove_handler("debug")

    @staticmethod
    def info(log_meg):
        set_handler("info")
        logger.debug("[INFO:" + get_current_time() + "]:" + log_meg)
        remove_handler("info")

    @staticmethod
    def warning(log_meg):
        set_handler("warning")
        logger.debug("[WARNING:" + get_current_time() + "]:" + log_meg)
        remove_handler("warning")

    @staticmethod
    def error(log_meg):
        set_handler("error")
        logger.debug("[ERROR:" + get_current_time() + "]:" + log_meg)
        remove_handler("error")

    @staticmethod
    def critical(log_meg):
        set_handler("critical")
        logger.debug("[CRITICAL:" + get_current_time() + "]:" + log_meg)
        remove_handler("critical")


if __name__ == "__main__":
    create_mylog.debug("这是debug消息")
    create_mylog.info("这是info消息")
    create_mylog.warning("这是warning消息")
    create_mylog.error("这是error消息")
    create_mylog.critical("这是critical消息")