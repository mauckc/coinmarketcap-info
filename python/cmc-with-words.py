import urllib, json
import inflect

# Read ticker information from coinmarketcap and function for parsing
# information by specific coins using their coin index (i.e. Ethereum = 1027)

# Create number to word engine
p = inflect.engine()

url = "https://api.coinmarketcap.com/v2/ticker/"
response = urllib.urlopen(url)
data = json.loads(response.read())

#print(coinkeys)
#print(enumerate(coinkeys))
# Read ticker information from loaded json data and print specific coins'
#  current information to screen
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


# Set up coin interface index json functionality
json_coin_index_data = open("../data/coin_ids.json").read()
coin_index_data = json.loads(json_coin_index_data)

user_coin_choice = raw_input("What coin would you like info for?: ")
coinkeys = coin_index_data.keys()

if user_coin_choice in coinkeys:
    getticker(coin_index_data[user_coin_choice])
else:
    print("That is not a valid choice. Please use full name with caps. (i.e. Ethereum)\nPlease Try again.\n")
    user_coin_choice = raw_input("What coin would you like info for?: ")
    if user_coin_choice in coinkeys:
        getticker(coin_index_data[user_coin_choice])
    else:
        print("I'm sorry that is still not an accepable coin name")
