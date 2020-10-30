# from web3 import Web3
import hashlib

__all__ = [
    'keccak_to_hex',
    'keccak_sig_to_selector',
    ]

# def keccak_to_hex(text):
#     return Web3.toHex(Web3.keccak(text=text))
#
# def keccak_sig_to_selector(text):
#     return Web3.toHex(Web3.keccak(text=text))[:8]

def keccak_to_hex(text):
    keccak = hashlib.sha256()
    keccak.update(text.encode('utf-8'))
    return keccak.hexdigest()

def keccak_sig_to_selector(text):
    keccak = hashlib.sha256()
    keccak.update(text.encode('utf-8'))
    return keccak.hexdigest()[:8]
