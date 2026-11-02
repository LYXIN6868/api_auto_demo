#管理请求头和请求会话
import pytest
import requests
from config import BASE_URL

@pytest.fixture(scope='session')  # session级别
def api_session():
    session=requests.Session()
    session.headers.update({"content-type":"application/json"})

#yield区分前置操作和后置处理，返回session给测试用例使用
    yield session
    session.close()

