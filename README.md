# Mock Contracts

Various mock contract deployments that anyone can use on public networks.

## Deployments

Public deployments, open to all.

### Goerli

| Name      | Address                                    | Description  |
| --------- | ------------------------------------------ | ------------ |
| MockToken | 0xeB6e6DC9a4A19A3d78A753c788E9dc84802bA844 | ERC20 token  |
| MockNFT   | 0xCaAf44843Ce103FC8fdD9d19a96612D020705208 | ERC721 token |

## Usage

This is an Ape project and you can interact with the deployments via the Ape
console. You may need to alter `ape-config.yaml` for your preferred network
connection.

    ape console --network ethereum:goerli
    In [1]: token = project.MockToken.deployments[0]

    In [2]: token.totalSupply()
    Out [2]: 1000000000000000000000000

    In [3]: token.mint('0x9283099A29556fCF8fFF5b2Cea2D4F67CB7A7A8b', 16777216, sender=accounts[0])
    [...]
    Out[3]: <Receipt 0x4f8e1ed021203f2a6cfb8581845005f073cd9a61ea7e4604f29f4b604775b797>

### MockToken (ERC20)

Everything is standard. Minting is offered up via an unpermissioned, public
`mint()` method.

#### Minting

Minting is available to anyone at any amount.

    token.mint(accounts[0].address, 123, sender=accounts[0])

### MockNFT (ERC721)

Everything is standard. Minting is offered up via two unpermissioned, public
`mint()` methods.

#### Minting

Minting is available to anyone a single token at a time. You can use the
default base URI (for token metadata):

    nft.mint(recipient, 123, sender=accounts[0])

Or mint a token with a specific URI:

    nft.mint(recipient, 123, 'https://example.com/token/123', sender=accounts[0])
