# currency price crawler
import http.client
import json
import matplotlib.pyplot as plt

coins = {
        'bitcoin': 'btc',
        'bitcoin cash': 'bch',
        'etherium': 'eth',
        'etherium classic': 'etc',
        'ripple': 'xrp',
        'quantum': 'qtum',
        'iota': 'iota',
        'litecoin': 'ltc',
        'bitcoin gold': 'btg'}

def getOrderbook(coin):
    conn = http.client.HTTPSConnection('api.coinone.co.kr')
    conn.request('GET', '/orderbook?' + coin)
    resp = conn.getresponse().read()
    resp = resp.decode('utf-8')
    resp = json.loads(resp)
    return resp

def getTrades(coin = 'btc', period = 'day', unit = 'minute'):
    conn = http.client.HTTPSConnection('api.coinone.co.kr')
    conn.request('GET', '/trades?currency=' + coin + '&period=' + period)
    resp = conn.getresponse().read()
    resp = resp.decode('utf-8')
    resp = json.loads(resp)

    if resp['errorCode'] != '0':
        print('crawling failed')
        return

    orders = resp['completeOrders']
    trades = []
    for o in orders:
        ts = int(o['timestamp'])
        price = float(o['price'])
        qty = float(o['qty'])

        # merge data if timestamp is same
        if len(trades) > 0 and \
                trades[-1]['timestamp'] == ts:
            if trades[-1]['price'] == price:
                trades[-1]['qty'] += qty
            else:
                trades[-1]['price'] = price
                trades[-1]['qty'] = qty
        else:
            if len(trades) > 0:
                ts_prev = trades[-1]['timestamp']
                price_prev = trades[-1]['price']
                for t in range(ts_prev + 1, ts):
                    tr = {
                            'timestamp': t,
                            'price': price_prev,
                            'qty': 0}
                    trades.append(tr)
                    
            tr = {
                    'timestamp': ts,
                    'price': price,
                    'qty': qty}
            trades.append(tr)

    if unit == 'minute':
        new_trades = []
        print('minute') 
        for i in range(0, int(len(trades) / 30)):
            new_trades.append(trades[i * 30])
        trades = new_trades

    return trades 

def onlyClosePrices(trades):
    new_trades = []
    for i in range(0, int(len(trades) / 30)):
        new_trades.append(trades[i * 30])
    return new_trades

def writeFile(trades, name, enableTimestamp = True, enableQuantity = False):
    fp = open(name + '.csv', 'w')
    for t in trades:
        ts = t['timestamp']
        pr = t['price']
        qt = t['qty']

        buf = ""
        if enableTimestamp:
            buf += str(ts) + "," 
        buf += str(pr)
        if enableQuantity:
            buf += "," + str(qt)
        buf += "\n"

        fp.write(buf)

    fp.close()

if __name__ == '__main__':
    trades = getTrades()
    ts = [tr['timestamp'] for tr in trades]
    pr = [tr['price'] for tr in trades]
    writeFile(trades, 'btc', enableTimestamp = False)
    plt.plot(ts, pr)
    plt.show()
