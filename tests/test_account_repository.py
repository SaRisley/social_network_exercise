from lib.account import *
from lib.account_repository import *

def test_get_all_records(db_connection):
    db_connection.seed('seeds/social_network.sql')
    repository = AccountRepository(db_connection)
    accounts = repository.all()
    assert accounts == [
        Account(1, "fakeemail@email.com", "fakeusername"),
        Account(2, "fakeemail2@email.com", "fakeusername2"),
        Account(3, "fakeemail3@email.com", "fakeusername3")
    ]

def test_find_record(db_connection):
    db_connection.seed('seeds/social_network.sql')
    repository = AccountRepository(db_connection)
    accounts = repository.find("fakeusername2")
    assert accounts == Account(2, "fakeemail2@email.com", "fakeusername2")

def test_create_record(db_connection):
    db_connection.seed('seeds/social_network.sql')
    repository = AccountRepository(db_connection)
    repository.create(Account(4, "fakeemail4@email.com", "fakeusername4"))
    result = repository.find("fakeusername4")
    assert result == Account(4, "fakeemail4@email.com", "fakeusername4")

def test_delete_record(db_connection):
    db_connection.seed('seeds/social_network.sql')
    repository = AccountRepository(db_connection)
    repository.delete("fakeusername2")
    accounts = repository.all()
    assert accounts == [
        Account(1, "fakeemail@email.com", "fakeusername"),
        Account(3, "fakeemail3@email.com", "fakeusername3")
    ]