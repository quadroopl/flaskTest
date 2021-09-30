
def get_price(coin, currency):
    try:
        response = requests.get(URL.format(coin, currency)).json()
        return response
    except:
        return False


def StartCollection():
    while True:
        date_time = datetime.now()
        date_time = date_time.strftime("%d/%m/%y %H:%M:%S")
        currentPrice = get_price("BTC", "USD")
        if currentPrice:
            return (date_time, "$", currentPrice["USD"])