from cod import CODHelper

# coin_list = ['bitcoin', 'ethereum']
coin_list = ['cardano'] # 테스트용

for coin in coin_list:
    codata = CODHelper(coin)
    # result = codata.get_data('2015/01/01')
    # codata.create_data_csv(result)
    result = codata.get_data_yesterday()
    codata.add_data_yesterday(result)
    del codata


