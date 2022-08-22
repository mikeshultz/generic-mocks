import pytest

from ._utils import tx_params

INITIAL_SUPPLY = int(1000000e18)


@pytest.fixture
def mock_erc20(deployer, project):
    return project.MockToken.deploy(INITIAL_SUPPLY, sender=deployer)


def test_deployment(deployer, mock_erc20):
    """Make sure the deployment parameters are correct"""
    assert mock_erc20.symbol() == "MOCK"
    assert mock_erc20.name() == "Mock Token"
    assert mock_erc20.balanceOf(deployer) == INITIAL_SUPPLY


def test_mint(named_accounts, deployer, mock_erc20):
    """Test simple minting"""
    amount = int(5e18)

    assert mock_erc20.balanceOf(named_accounts.alice) == 0

    mock_erc20.mint(named_accounts.alice, amount, **tx_params(deployer))

    assert mock_erc20.balanceOf(named_accounts.alice) == amount


def test_transfer(named_accounts, deployer, mock_erc20):
    """Make sure transfers work"""
    amount = int(1e18)

    mock_erc20.mint(named_accounts.alice, amount * 2, **tx_params(deployer))
    original_balance = mock_erc20.balanceOf(named_accounts.alice)
    mock_erc20.transfer(named_accounts.bob, amount, **tx_params(named_accounts.alice))

    assert mock_erc20.balanceOf(named_accounts.bob) == amount
    assert mock_erc20.balanceOf(named_accounts.alice) == original_balance - amount
