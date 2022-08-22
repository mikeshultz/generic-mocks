// SPDX-License-Identifier: MIT
pragma solidity ^0.8.12;

import {ERC721, ERC721URIStorage} from "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import {Strings} from "@openzeppelin/contracts/utils/Strings.sol";

contract MockNFT is ERC721URIStorage {
    string public defaultBaseURI;

    constructor(string memory _defaultBaseURI) ERC721("Mock NFT", "MOCK") {
        defaultBaseURI = _defaultBaseURI;
    }

    function mint(address to, uint256 tokenId) public returns (uint256) {
        return
            _mintToken(
                to,
                tokenId,
                string.concat(
                    defaultBaseURI,
                    Strings.toString(tokenId),
                    ".json"
                )
            );
    }

    function mint(
        address to,
        uint256 tokenId,
        string calldata tokenURI
    ) public returns (uint256) {
        return _mintToken(to, tokenId, tokenURI);
    }

    function _mintToken(
        address to,
        uint256 tokenId,
        string memory tokenURI
    ) private returns (uint256) {
        _mint(to, tokenId);
        _setTokenURI(tokenId, tokenURI);
        return tokenId;
    }
}
