import re
import json
import pandas as pd

from tx_tools import (
    get_abi,
    get_calldata,
    get_transaction,
    keccak_sig_to_selector,
    keccak_to_hex
    )


tx_hash = '0x91cba77b2db3c1bdb726e160ba792d8d540adbc511e4f5c8b595545db9b61c3e'

lift_selector = keccak_sig_to_selector("lift(address)")
tx_data = get_transaction(tx_hash)

tx_target = tx_data['to']
tx_sender = tx_data['from']
tx_calldata = tx_data['input']
tx_selector = tx_calldata[2:10]
tx_calldata = tx_calldata[10:]

print('------------------------------------------------------------------------------------')
print(f'Transaction Hash: {tx_hash}')
print(f'To: {tx_target}'.rjust(60))
print(f'From: {tx_sender}'.rjust(60))
print(f'selector: {tx_selector}'.rjust(26))
print('------------------------------------------------------------------------------------')
print('calldata'.rjust(17))
print('------------------------------------------------------------------------------------')

bytes32_arrays = []
for i in range(len(tx_calldata)//64):
    bytes32_arrays.append(tx_calldata[i*64:(i+1)*64])
    print('{}:'.format(i).rjust(10), '{}'.format(tx_calldata[10:][i*64:(i+1)*64]).ljust(1))

df = pd.DataFrame({f'selector: {tx_selector}': bytes32_arrays})


# print(web3.toHex(web3.eth.getCode("0x55e8BeF09624D60793181A125E07F040B4BCaCBC")))
