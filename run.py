import requests
import csv

kyword = input('Masukkan keyword :')
write = csv.writer(open('hasil/{}.csv'.format(kyword), 'w', newline=''))
headers = ('Nama', 'Harga', 'Stok')
write.writerow(headers)

url = 'https://api.bukalapak.com/multistrategy-products'
count = 0
for page in range(1, 6):
    paramtr = {
    'prambanan_override': True,
    'keywords': kyword,
    'limit': 50,
    'offset': 50,
    'page': page,
    'facet': True,
    'access_token': '-dIzX_R2qaEKfoApCcpQsCqOFWBOOmkl7MvMzD6yRJuXkA'
    }

    respon = requests.get(url, params=paramtr).json()

    products = respon['data']
    for p in products:
        nama = p['name']
        harga = p['price']
        stok = p['stock']
        count+=1
        print('no:',count, 'nama:', nama, 'harga:', harga, 'stok:', stok)
        write = csv.writer(open('hasil/{}.csv'.format(kyword), 'a', newline=''))
        data = [nama,harga,stok]
        write.writerow(data)