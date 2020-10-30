from . import etherscan_api_key
from .py_etherscan_api import (
    Contract,
    rate_limiter,
    )


@rate_limiter
def get_abi(contract_address):
    '''
    We can only call this 5 times per second. The rate limiter overcompensates
    by delaying each call by 0.5 seconds.
    '''
    contract = Contract(contract_address, etherscan_api_key)
    return contract.get_abi()
