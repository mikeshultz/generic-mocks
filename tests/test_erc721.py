import pytest
from ._utils import tx_params

BASE_URI = "http://example.eth/metadata/"


@pytest.fixture
def mock_nft(deployer, project):
    print("project:", project)
    return project.MockNFT.deploy(BASE_URI, sender=deployer)


def test_deployment(deployer, mock_nft):
    """Make sure the deployment parameters are correct"""
    assert mock_nft.symbol() == "MOCK"
    assert mock_nft.name() == "Mock NFT"
    assert mock_nft.balanceOf(deployer) == 0


def test_mint(named_accounts, mock_nft):
    mock_nft.mint(named_accounts.alice, 1, **tx_params(named_accounts.alice))
    assert mock_nft.balanceOf(named_accounts.alice) == 1


def test_mint_with_base_uri(named_accounts, mock_nft):
    token_id = 1024
    token_uri = "http://other.eth/metadata/2.json"
    mock_nft.mint(
        named_accounts.bob, token_id, token_uri, **tx_params(named_accounts.bob)
    )
    assert mock_nft.balanceOf(named_accounts.bob) == 1
    assert mock_nft.tokenURI(token_id) == token_uri
