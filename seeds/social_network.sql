DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;
DROP TABLE IF EXISTS accounts;
DROP SEQUENCE IF EXISTS accounts_id_seq;


CREATE TABLE accounts(
    id SERIAL PRIMARY KEY,
    email text,
    username text
);

CREATE TABLE posts(
    id SERIAL PRIMARY KEY,
    title text,
    contents text,
    views int,
    account_id int,
    constraint fk_account foreign key(account_id)
    references accounts(id)
    on delete cascade
);

INSERT INTO accounts (email, username) VALUES ('fakeemail@email.com', 'fakeusername');
INSERT INTO accounts (email, username) VALUES ('fakeemail2@email.com', 'fakeusername2');
INSERT INTO accounts (email, username) VALUES ('fakeemail3@email.com', 'fakeusername3');

INSERT INTO posts (title, contents, views, account_id) VALUES ('title1', 'contents1', 100, 1);
INSERT INTO posts (title, contents, views, account_id) VALUES ('title2', 'contents2', 200, 2);
INSERT INTO posts (title, contents, views, account_id) VALUES ('title3', 'contents3', 500, 1);
