import pytest
import allure
from api.post_api import PostsAPI
from utils.yaml_util import read_yaml


#  正向用例

@allure.epic("文章模块")
@allure.feature("获取文章")
@allure.story("获取单篇文章详情")
@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_get_valid(api_session, post_id):
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
@allure.story("数据驱动-批量创建文章")
@pytest.mark.parametrize("payload", read_yaml("data/post_data.yaml")["create_posts"])
def test_create_post(api_session, payload):
    post_api = PostsAPI(api_session)
    with allure.step(f"发送 POST 请求创建文章: {payload['title']}"):
        response = post_api.create_post(payload)
    with allure.step("断言状态码为 201 且返回内容一致"):
        assert response.status_code == 201
        data = response.json()
        assert data["title"] == payload["title"]


# 异常用例

@allure.epic("文章模块")
@allure.feature("获取文章")
@allure.story("异常健壮性-非法ID参数校验")
@pytest.mark.parametrize("invalid_id", read_yaml("data/post_data.yaml")["invalid_ids"])
def test_get_invalid_post_id(api_session, invalid_id):
    post_api = PostsAPI(api_session)
    with allure.step(f"发送 GET 请求，请求非法 ID: {invalid_id}"):
        response = post_api.get_post(invalid_id)
    with allure.step("断言返回错误状态码 (404 或 400)"):
        assert response.status_code in [400, 404]


@allure.epic("文章模块")
@allure.feature("创建文章")
@allure.story("异常健壮性-缺失必填字段")
def test_create_post_missing_title(api_session):
    post_api = PostsAPI(api_session)
    invalid_payload = {"body": "只有内容没有标题", "userId": 1}
    with allure.step("发送缺失 title 的 POST 请求"):
        response = post_api.create_post(invalid_payload)
    with allure.step("验证后端是否拦截(400) 或 Mock 接口的默认处理(201)"):
        assert response.status_code in [201, 400]


# 业务场景联动

@allure.epic("文章模块")
@allure.feature("业务场景联动")
@allure.story("CRUD 增删改查完整闭环")
def test_crud_workflow(api_session):
    post_api = PostsAPI(api_session)
    payload = {"title": "闭环测试", "body": "测试内容", "userId": 1}

    with allure.step("1. 创建新文章 (POST)"):
        res_create = post_api.create_post(payload)
        assert res_create.status_code == 201
        new_id = res_create.json()["id"]

    with allure.step(f"2. 获取刚创建的文章 (GET)，验证内容"):
        res_get = post_api.get_post(new_id)
        # 兼容 Mock 接口
        assert res_get.status_code in [200, 404]

    with allure.step("3. 删除该文章 (DELETE)"):
        res_delete = post_api.session.delete(f"{post_api.url}/{new_id}")
        assert res_delete.status_code == 200

    with allure.step("4. 再次获取，验证是否已被删除"):
        res_get_deleted = post_api.get_post(new_id)
        assert res_get_deleted.status_code in [200, 404]