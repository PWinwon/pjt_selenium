from gcd import GCDHelper

products = ['RTX 3090', 'RTX 3080 Ti', 'RTX 3080 -Ti', 'RTX 3070 Ti',
            'RTX 3070 -Ti', 'RTX 3060 Ti', 'RTX 3060 -Ti',
            'RTX 2060 super', 'RTX 2060 -super',
        ]

gcd = GCDHelper()
data_avg = []
for product in products:
    data = gcd.get_data_today(product)
    gcd.update_data_csv(data, product)
    val_avg = int(round(sum(data) / len(data)))
    data_avg.append(val_avg)
gcd.update_data_csv(data_avg)