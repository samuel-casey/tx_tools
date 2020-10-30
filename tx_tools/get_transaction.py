from . import etherscan_api_key
from .py_etherscan_api import (
    Proxies,
    rate_limiter,
    )


@rate_limiter
def get_transaction(tx_hash):
    '''
    Get transaction data that occurred on the Ethereum mainnet.

    Returns JSON as a python dict with these keys:
        {
            'blockHash', 'blockNumber', 'hash', 'transactionIndex',
            'to', 'from', 'value', 'input', 'nonce', 'gas', 'gasPrice'
            'v', 'r', 's'
        }
    '''
    proxies = Proxies(etherscan_api_key)
    return proxies.get_transaction_by_hash(tx_hash)
