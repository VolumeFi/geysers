# geysers
Liquidity Mining Tools for Token Projects

## Infura Key
```bash
export WEB3_INFURA_PROJECT_ID=${YOUR_INFURA_KEY}
```

## Add account
```bash
brownie accounts new deployer_account
```

input private key and password


## Test
Run ganache-cli mainnet fork

```bash
ganache-cli --fork https://mainnet.infura.io/v3/#{YOUR_INFURA_KEY} -p 7545 -e 10000
```

Run brownie test

```bash
brownie test -s
```

## Deployment
```bash
brownie run deploy_mainnet.py --network mainnet # UniswapExchangeAdd
```