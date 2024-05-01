if __name__ == "__main__":
  # Introduction to Python dictionary comprehension

  """
  { key: value for (key, value) in dict.items() if condition }
  """

  # Using Python dictionary comprehension to transform a dictionary

  stocks = {
    "AAPL": 121,
    "AMZN": 3380,
    "MSFT": 219,
    "BIIB": 280,
    "QDEL": 266,
    "LVGO": 144
  }
  print(stocks)

  new_stocks = {}
  for symbol, price in stocks.items():
    new_stocks[symbol] = price * 1.02
  print(new_stocks)

  stocks = {
    "AAPL": 121,
    "AMZN": 3380,
    "MSFT": 219,
    "BIIB": 280,
    "QDEL": 266,
    "LVGO": 144
  }
  print(stocks)

  new_stocks = { symbol: price * 1.02 for (symbol, price) in stocks.items() }
  print(new_stocks)
