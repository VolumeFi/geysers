from brownie import StakeRewards, StakeRewardsFactory, accounts

def main():
    acct = accounts.load("deployer_account")
    StakeRewardsContract = StakeRewards.deploy("0x0000000000000000000000000000000000000000", "0x0000000000000000000000000000000000000000", "0x0000000000000000000000000000000000000000", "0x0000000000000000000000000000000000000000", 0, "0x0000000000000000000000000000000000000000", {'from':accounts[0]})
    StakeRewardsFactory.deploy(StakeRewardsContract, {'from':accounts[0]})