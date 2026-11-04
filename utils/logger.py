import logging
import os


def get_logger(name="APITest"):
    #创建全局唯一日志对象
    logger=logging.getLogger(name)
    if not logger.handlers:
        #设置日志级别
        logger.setLevel(logging.INFO)

        #定义格式
        formatter=logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        #控制台输出
        console_handler=logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        #文件输出
        log_dir="logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        file_handler=logging.FileHandler(f"{log_dir}/test_run.log",encoding='utf-8')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger

#实例化一个logger
logger=get_logger()
