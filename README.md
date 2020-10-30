# Analyzing Flashloan Transaction Data

## Introduction
In light of MakerDAO's recent [forum post](https://forum.makerdao.com/t/urgent-flash-loans-and-securing-the-maker-protocol/4901) about flashloan's being an [attack vector](https://etherscan.io/tx/0x91cba77b2db3c1bdb726e160ba792d8d540adbc511e4f5c8b595545db9b61c3e) for governance contracts, we designed a python tool that allows users to examine the calldata of a transaction through the etherscan api. With this tool users can examine the function selectors and addresses passed into the calldata. It may be possible to determine if a flashloan inappropriately influenced a governance proposal. We make no warranties about the accuracy or interpretation of any data retrieved from this tool, and we don't endorse any claims made as a result of using this open source software, unless otherwise specified.

## Installation

#### Using git and python3-pip
```sh
git clone https://github.com/game-b-dev/tx_tools
cd tx_tools
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### Save `env` as `.env` with your ETHERSCAN_API_KEY:
#### (Warning! If you do not put the `.` in front of `env` then your API key may accidentally leak!)
```
# contents of .env
ETHERSCAN_API_KEY="your_etherscan_api_key"
```

## Usage
Modify `analyze_tx.py` with the transaction hash you want to analyze.
(more features coming asap)
```sh
(venv) ~/tx_tools $ python analyze_tx.py
```
