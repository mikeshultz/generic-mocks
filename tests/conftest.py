import pytest
from collections import namedtuple

NamedAccounts = namedtuple("NamedAccounts", ["alice", "bob", "carol"])


@pytest.fixture
def deployer(accounts):
    return accounts[0]


@pytest.fixture
def named_accounts(accounts) -> NamedAccounts:
    return NamedAccounts(accounts[1], accounts[2], accounts[3])
