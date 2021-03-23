from web3.auto import w3
import asyncio

#w3 = Web3(HTTPProvider("http://127.0.0.1:8545"))

async def log_loop(event_filter, poll_interval, callback_func):
    while True:
        print("trying")
        for event in event_filter.get_new_entries():
            callback_func(event)
            #handle_event(event)
        await asyncio.sleep(poll_interval)

def main(callback_func):
    block_filter = w3.eth.filter('latest')
    tx_filter = w3.eth.filter('pending')
    loop = asyncio.get_event_loop()
    try:
        
        loop.run_until_complete(
            asyncio.gather(
                #log_loop(block_filter, 2, callback_func),
                log_loop(tx_filter, 2, callback_func)))
    finally:
        loop.close()

if __name__ == '__main__':
    main(func1)