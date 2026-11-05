from config import BASE_URL


class PostsAPI:
    def __init__(self, session):
        self.session = session
        self.url = f'{BASE_URL}/posts'

    def get_post(self, post_id):
        return self.session.get(f"{self.url}/{post_id}")

    def create_post(self, payload):
        return self.session.post(self.url, json=payload)

    def delete_post(self, post_id):
        return self.session.delete(f"{self.url}/{post_id}")