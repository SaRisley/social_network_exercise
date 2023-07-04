from lib.post import Post

class PostRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM posts')
        posts = []
        for row in rows:
            item = Post(row["id"], row["title"], row["contents"], row["views"], row["account_id"])
            posts.append(item)
        return posts
    
    def find(self, title):
        rows = self._connection.execute('SELECT * FROM posts WHERE title = %s', [title])
        row = rows[0]
        return Post(row["id"], row["title"], row["contents"], row["views"], row["account_id"])
    
    def create(self, post):
        self._connection.execute('INSERT INTO posts (title, contents, views, account_id) VALUES (%s, %s, %s, %s)', [post.title, post.contents, post.views, post.account_id])

    def delete(self, title):
        self._connection.execute('DELETE FROM posts WHERE title = %s', [title])