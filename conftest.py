#管理请求头和请求会话
import pytest
import requests
import logging
from utils.logger import logger
from config import BASE_URL


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger=logging.getLogger("APILog")


#定义钩子函数，接收response对象
def log_response_hook(response,*args,**kwargs):
    #提取请求对象
    req=response.request

    #记录
    logger.info(f"===发送请求===")
    logger.info(f'请求方法：{req.method} |URL:{req.url}')
    if req.body:
        logger.info(f"请求参数：{str(req.body)[:200]}")

    #记录响应信息
    logger.info(f"===接收响应===")
    logger.info(f'响应状态码：{response.status_code} |接口耗时:{response.elapsed.total_seconds()}秒')
    logger.info(f"响应内容：{response.text[:200]}")
    logger.info(f"========================\n")




@pytest.fixture(scope='session')  # session级别
def api_session():
    session=requests.Session()
    session.headers.update({"content-type":"application/json"})

    session.hooks['response'].append(log_response_hook)
#yield区分前置操作和后置处理，返回session给测试用例使用
    yield session
    session.close()

