# Binance Futures Testnet Trading Bot

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Create `.env` file:

```env
API_KEY=your_api_key
API_SECRET=your_secret
```

## Run Commands

Market Order:

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

Limit Order:

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 70000
```

## Features

* Place Market Orders
* Place Limit Orders
* BUY / SELL support
* CLI validation
* Logging
* Error handling

## Assumptions

* Binance Futures Testnet account is active
* API keys are valid
* User has testnet balance
