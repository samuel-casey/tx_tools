from . import etherscan_api_key
from .py_etherscan_api import (
    Proxies,
    rate_limiter,
    )


@rate_limiter
def get_calldata(tx_hash):
    '''
    Get only the calldata of a transactionthat occurred on the Ethereum mainnet.

    Returns calldata as a 0x-prepended hex string
    '''
    proxies = Proxies(etherscan_api_key)
    return proxies.get_transaction_by_hash(tx_hash)['input']
