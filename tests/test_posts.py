import pytest
import allure
from api.post_api import PostsAPI  # 导入你封装的接口类

#可通过UI界面看到具体是在哪一步挂掉了(Behaviors)
#正向用例
@allure.epic("文章模块")
@allure.feature("获取文章")
@allure.story("获取单篇文章详情")
@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_get_valid(api_session, post_id):
    # 1. 实例化接口类
    post_api = PostsAPI(api_session)

    with allure.step(f"发送 GET 请求获取 ID 为 {post_id} 的文章"):
        response = post_api.get_post(post_id)

    with allure.step("断言状态码为 200 且数据结构正确"):
        assert response.status_code == 200
        data = response.json()
        assert "userId" in data
        assert "title" in data
        assert data["id"] == post_id


@allure.epic("文章模块")
@allure.feature("创建文章")
@allure.story("正常创建新文章")
def test_create_post(api_session):
    post_api = PostsAPI(api_session)
    payload = {
        "title": "My new post",
        "body": "This is my new post",
        "userId": 1
    }

    with allure.step("发送 POST 请求创建文章"):
        response = post_api.create_post(payload)

    with allure.step("断言状态码为 201 且返回内容与请求一致"):
        assert response.status_code == 201
        data = response.json()
        assert data["title"] == payload["title"]
        assert data["userId"] == payload["userId"]


# 异常用例

@allure.epic("文章模块")
@allure.feature("获取文章")
@allure.story("获取不存在的文章返回404")
@allure.severity(allure.severity_level.NORMAL)
def test_get_not_found(api_session):
    post_api = PostsAPI(api_session)

    with allure.step("发送 GET 请求获取不存在的 ID (999)"):
        response = post_api.get_post(999)

    with allure.step("断言状态码为 404"):
        assert response.status_code == 404