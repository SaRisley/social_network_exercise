from lib.post_repository import *
from lib.post import *

def test_get_all_records(db_connection):
    db_connection.seed('seeds/social_network.sql')
    repository = PostRepository(db_connection)
    posts = repository.all()
    assert posts == [
        Post(1, "title1", "contents1", 100, 1),
        Post(2, "title2", "contents2", 200, 2),
        Post(3, "title3", "contents3", 500, 1)
    ]

def test_find_record(db_connection):
    db_connection.seed('seeds/social_network.sql')
    repository = PostRepository(db_connection)
    post = repository.find("title2")
    assert post == Post(2, "title2", "contents2", 200, 2)

def test_create_record(db_connection):
    db_connection.seed('seeds/social_network.sql')
    repository = PostRepository(db_connection)
    repository.create(Post(4, "title4", "contents4", 500, 3))
    result = repository.find("title4")
    assert result == Post(4, "title4", "contents4", 500, 3)

def test_delete_record(db_connection):
    db_connection.seed('seeds/social_network.sql')
    repository = PostRepository(db_connection)
    repository.delete("title2")
    posts = repository.all()
    assert posts == [
        Post(1, "title1", "contents1", 100, 1),
        Post(3, "title3", "contents3", 500, 1)
    ]