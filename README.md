### Usage
Run the code and it will ask you what cryptocurrency you would like to know current market information for.

It will respond with ticker price, market cap, price change percentages etc.

Input:
```bash
python cmc-with-words.py
```
Output:
```
What coin would you like info for?: 
```
You type
Input:
```bash
Ethereum
```
Output:
```
Getting ticker data for coin with id: 1027
Name: Ethereum
Symbol: ETH
Rank: two
Price: five hundred and twenty-two
Market Cap: fifty-two billion, three hundred and seven million, seven hundred and forty thousand, nine hundred and six
24h Volume: one billion, seven hundred and ninety-four million, nine hundred and eighty thousand
Price Change 1h: -0.07
Price Change 24h: 0.84
Price Change 7d: 5.29
Total Supply: one hundred million, one hundred and eighty-four thousand, one hundred and thirty-seven
Circulating Supply: one hundred million, one hundred and eighty-four thousand, one hundred and thirty-seven
Max Supply: None
```

You will have two attempts to enter a correct name. 
Input format is case-sensitve (i.e. Ethereum will work, but ethereum and ETH will not)

### Dependencies
urllib and json libraries should be native to python 2.7.15 however inflect will most likely neeed to be installed

```python
import urllib, json
import inflect
```

if you do not have inflect installed enter the following in your command prompt or terminal
```bash
pip install inflect
```

### Number to Words with Inflect Library
Create our number to word engine
```python
p = inflect.engine()
```

### Coin Market Cap API
Set up coin market cap api call:
```python
url = "https://api.coinmarketcap.com/v2/ticker/"
response = urllib.urlopen(url)
data = json.loads(response.read())
```

Read ticker information from loaded json data and print a specific coin's current data to screen
```python
def getticker(n):
    n = str(n)
    print("\nGetting ticker data for coin with id: " + n)

    # Save information from loaded json
    tickername = data['data'][n]['name']
    tickersymbol = data['data'][n]['symbol']
    tickerrank = data['data'][n]['rank']
    tickerUSDprice = data['data'][n]['quotes']['USD']['price']
    tickerUSDmarketcap = data['data'][n]['quotes']['USD']['market_cap']
    tickerUSDpercentchange1h = data['data'][n]['quotes']['USD']['percent_change_1h']
    tickerUSDpercentchange24h = data['data'][n]['quotes']['USD']['percent_change_24h']
    tickerUSDvolume24h = data['data'][n]['quotes']['USD']['volume_24h']
    tickerUSDpercentchange7d = data['data'][n]['quotes']['USD']['percent_change_7d']
    tickertotalsupply = data['data'][n]['total_supply']
    tickercirculatingsupply = data['data'][n]['circulating_supply']
    tickermaxsupply =  data['data'][n]['max_supply']

    print("Name: " + tickername)
    print("Symbol: " + tickersymbol)
    print("Rank: " + p.number_to_words(tickerrank))
    print("Price: " + p.number_to_words( int(tickerUSDprice) ) )
    print("Market Cap: " + p.number_to_words(int(round(tickerUSDmarketcap,4))))
    print("24h Volume: " + p.number_to_words(int(round(tickerUSDvolume24h,4))))
    print("Price Change 1h: " + str(tickerUSDpercentchange1h) )
    print("Price Change 24h: " + str(tickerUSDpercentchange24h) )
    print("Price Change 7d: " + str(tickerUSDpercentchange7d) )
    print("Total Supply: " + p.number_to_words(int(round(tickertotalsupply,4))) )
    print("Circulating Supply: " + p.number_to_words(int(tickercirculatingsupply) ))
    if tickermaxsupply is None:
        print("Max Supply: " + "None")
    else:
        print("Max Supply: " + p.number_to_words(int(tickermaxsupply)) )
```
### Setting Up User Input
Set up coin interface index json functionality for interpreting user input as Name instead of coinmarketcap id.
```python
json_coin_index_data = open("coin_ids.json").read()
coin_index_data = json.loads(json_coin_index_data)
```

Prompt user for which coin ticker data he or she is interested in
```python
user_coin_choice = raw_input("What coin would you like info for?: ")
coinkeys = coin_index_data.keys()
```

If user enters correct coin name that matches a key in list coinkeys
    get the data
else prompt user again 
    if user correct choice
    get the data
    else say "Sorry that is still not a correct option"
    
```python
if user_coin_choice in coinkeys:
    getticker(coin_index_data[user_coin_choice])
else:
    print("That is not a valid choice. Please use full name with caps. (i.e. Ethereum)\nPlease Try again.\n")
    user_coin_choice = raw_input("What coin would you like info for?: ")
    if user_coin_choice in coinkeys:
        getticker(coin_index_data[user_coin_choice])
    else:
        print("I'm sorry that is still not an accepable coin name")
```

### coin_ids.json

User input cross-checked with manually added coin market cap coin name keys with to id values stored in json format with simple structured list as shown below and in file "coinmarketcap-info/data/coin_ids.json":

Initially as of Tuesday, June 19th, 2018 I have only written 24 entries.
Therefore, only 24 coins names are possible input strings for user choice of coin

coin_ids.json:
```javascript
{
  "Bitcoin": 1,
  "Ethereum": 1027,
  "Ripple": 52,
  "Bitcoin Cash": 1831,
  "EOS": 1765,
  "Litecoin": 2,
  "Stellar": 512,
  "Cardano": 2010,
  "IOTA": 1720,
  "TRON": 1958,
  "Tether": 825,
  "NEO": 1376,
  "DASH": 131,
  "Monero": 328,
  "Binance Coin": 1829,
  "NEM" : 873,
  "VeChain": 1904,
  "Ethereum Classic": 1321,
  "Ontology": 2566,
  "OmiseGo": 1808,
  "Qtum": 1684,
  "Zcash": 1437,
  "ICON": 2099,
  "Bytecoin": 372,
  "Verge": 693
}
```
