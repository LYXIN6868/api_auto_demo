import pytest
from config import BASE_URL

#正向用例，获取数据
@pytest.mark.parametrize("post_id",[1,2,3])
def test_gp_valid(api_session,post_id):
    response=api_session.get(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code==200
    data=response.json()

    #断言
    assert "userId" in data
    assert "title" in data
    assert data["id"]==post_id

#反向用例，获取不存在的id
def test_gb_not_found(api_session):
    response=api_session.get(f"{BASE_URL}/posts/999")
    assert response.status_code==404

#正向-创建文章
def test_craete_post(api_session):
    payload={
        "title":"My new post",
        "body":"This is my new post",
        "userId":1
    }
    response=api_session.post(f"{BASE_URL}/posts",json=payload)
    assert response.status_code==201
    data=response.json()
    assert data["title"]==payload["title"]
    assert data["userId"]==payload["userId"]

