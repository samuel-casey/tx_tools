import hashlib

__all__ = [
    'keccak_to_hex',
    'keccak_sig_to_selector',
    ]


def keccak_to_hex(text):
    keccak = hashlib.sha256()
    keccak.update(text.encode('utf-8'))
    return keccak.hexdigest()

def keccak_sig_to_selector(text):
    keccak = hashlib.sha256()
    keccak.update(text.encode('utf-8'))
    return keccak.hexdigest()[:8]
