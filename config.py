
walletAddress = "Your_wallet"                     #Your Wall address From trustwallet or MetaMask or another wallet.
private_key = "Wallet_private_key" #Wallet private_key

spend = "0xB31f66AA3C1e785363F0875A1B74E27b85FD66c7"  # WAVAX  OR BUSD OR USDT OR OTHER (Default WAVAX ) contract for buy the token

AmountForSnipe = 1 # Amount how much you want buy the token in spend.
MinLiquidityAdded = 20  # Set how much minimum liquidity added in pair address that you want to buy. set in spend. (eg : 2, 4, 7). if spend is WAVAX , 2 mean 2 WAVAX  liquidity added.
MaxSlippage = 25  # Max Slippage or Prince Impact
SellToken = 1   # 0 = Not Sell after buy, 1 = Sell token after buy by take profit
Takeprofit = 250  # In percent

transactionRevertTime = 1000 #Limit for make transaction
gasAmount = 600000 #Minimul limit is 210000, more much more better.
gasPrice = 30 #Customize your GWEI (gas fee) here, cannot decimal. (eg : 5, 10, 25).

traderjoexyzRouter = "0x60aE616a2155Ee3d9A68541Ba4544862310933d4"
traderjoexyzFactory = "0x9Ad6C38BE94206cA50bb0d90783181662f0Cfa10"

avalanche_c = "https://avalanche.public-rpc.com"          #avalanche JSON-RPC