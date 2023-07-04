from lib.post import *

def test_post_construct():
    post = Post(1, "fake title", "fake content", 10, 3)
    assert post.id == 1
    assert post.title == "fake title"
    assert post.contents == "fake content"
    assert post.views == 10
    assert post.account_id == 3