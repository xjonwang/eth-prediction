from pybundlr import pybundlr

# test_pred = [1274.65, 1274.65, 1274.65, 1274.65, 1274.65, 1274.65, 1274.65, 1274.65, 1274.65, 1274.65, 1274.65, 1274.65]
ocean = create_ocean_instance()

file = "../ETH_DATA/test_pred.csv"
url = pybundlr.fund_and_upload(file, "matic", )