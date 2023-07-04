As a social network user,
So I can have my information registered,
I'd like to have a user account with my email address.

As a social network user,
So I can have my information registered,
I'd like to have a user account with my username.

As a social network user,
So I can write on my timeline,
I'd like to create posts associated with my user account.

As a social network user,
So I can write on my timeline,
I'd like each of my posts to have a title and a content.

As a social network user,
So I can know who reads my posts,
I'd like each of my posts to have a number of views.


Nouns:
user_account, email, username, posts, title, content, views

Records  | Properties
user_acc | email, username
post     | title, contents, views


Table: accounts
id: SERIAL
email: text
username: text

Table: posts
id: SERIAL
title: text
contents: text
views: int

Can one account have many posts? (Yes)
Can one post have many accounts? (No)
You'll then be able to say that:

Accounts have many posts
And on the other side, posts belongs to an account
In that case, the foreign key is in the table posts


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

MODEL CLASS
class Account:
    #id: int
    #email: string
    #username: string


class Post:
    #id: int
    #title: string
    #contents: string
    #views: int
    #account_id: int

REPOSITORY CLASS
class AccountRepository:
    def all():
        #List all accounts

    def find():
        #Find specific account based on username

    def create():
        #Create new record in accounts table

    def delete():
        #Delete specific record from accounts table based on username

class PostRepository:
    def all():
        #List all posts

    def find():
        #Find specific post based on title

    def create():
        #Create new record in posts table

    def delete():
        #Delete specific record from posts table based on title

TESTS
    Account
    #When I create an account object the properties are correctly created as expected

    Post
    #When I create a post object the properties are correctly created as expected

    AccountRepository
    #When I call the all method I get a list of account objects that represent all records on the accounts table
    #When I call the find method with a username I get a account object that represents the matching record on the accounts table
    #When I call the create method with a account object a new record with the data from the account object is written to the accounts table
    #When I call the delete method with a username the corresponding record on the accounts table is deleted 

    PostRepository
    #When I call the all method I get a list of post objects that represent all records on the posts table
    #When I call the find method with a title I get a posts object that represents the matching record on the posts table
    #When I call the create method with a post object a new record with the data from the post object is written to the posts table
    #When I call the delete method with a title the corresponding record on the posts table is deleted 

    

