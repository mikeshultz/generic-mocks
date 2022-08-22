from ape import accounts, project


def main():
    deployer = accounts.load("deployer")
    deployer.deploy(project.MockNFT, "https://www.mikeshultz.com/nft/mock/")
    deployer.deploy(project.MockToken, int(1000000e18))
