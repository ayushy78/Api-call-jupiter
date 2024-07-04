import requests
import time

def send_msg_on_telegram(msg):
    telegram_api_url = f"https://api.telegram.org/bot5285438866:AAFrVHC_ZSAMReeUcgqWvCZGDDS8KgUU438/sendMessage?chat_id=-693640584&text={msg}"
    el_resp = requests.get(telegram_api_url)

while True:
    try:
        binance_response = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=JUPUSDT')
        binance_data = binance_response.json()
        Binance_price = float(binance_data['price'])

        quote_response_buyJUP = requests.get('https://quote-api.jup.ag/v6/quote',
            params={
                'inputMint': 'Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB',
                'outputMint': 'JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN',
                'amount': '10000000000',
                'slippageBps': '10'
            }
        )

        quote_data_buyJUP = quote_response_buyJUP.json()
        BuyingJUP = float(quote_data_buyJUP['outAmount']) / 10**6
        BuyJUP = round(10000 / BuyingJUP, 4)

        quote_response_sellJUP = requests.get('https://quote-api.jup.ag/v6/quote',
            params={
                'inputMint': 'JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN',
                'outputMint': 'Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB',
                'amount': '10000000000',
                'slippageBps': '10'
            }
        )

        quote_data_sellJUP = quote_response_sellJUP.json()
        SellingJUP = float(quote_data_sellJUP['outAmount']) / 10**6
        SellJUP = round(SellingJUP / 10000, 4)

        if (Binance_price - BuyJUP) / Binance_price > 0.008:
            text_buy = f"Buy JUP at Price (USDT-JUP): {BuyJUP}\n Sell on Binance at Price {Binance_price}"
            send_msg_on_telegram(text_buy)
            print("Buy message sent.")

        if (SellJUP - Binance_price) / Binance_price > 0.008:
            text_sell = f"Sell JUP at Price (JUP-USDT): {SellJUP} \n Buy on Binance at Price {Binance_price}"
            send_msg_on_telegram(text_sell)
            print("Sell message sent.")
        print(f"Binance Price:{Binance_price} \n USDT-JUP {BuyJUP} \n JUP-USDT {SellJUP}")
    except Exception as e:
        print(f"An error occurred: {e}")

    time.sleep(5)  # Wait for 5 seconds before checking again
