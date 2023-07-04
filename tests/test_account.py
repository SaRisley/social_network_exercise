from lib.account import *

def test_account_construct():
    account = Account(1, "fakeemail@email.com", "fakeusername")
    assert account.id == 1
    assert account.email == "fakeemail@email.com"
    assert account.username == "fakeusername"
