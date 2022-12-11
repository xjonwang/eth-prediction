from pybundlr import pybundlr
from utils import create_alice_wallet, create_ocean_instance

# test_pred = [1274.65, 1274.65, 1274.65, 1274.65, 1274.65, 1274.65, 1274.65, 1274.65, 1274.65, 1274.65, 1274.65, 1274.65]
ocean = create_ocean_instance()
wallet = create_alice_wallet(ocean) #you're Alice

file = "../ETH_DATA/test_pred.csv"
url = pybundlr.fund_and_upload(file, "matic", wallet.private_key)
print(f"Your csv url: {url}")