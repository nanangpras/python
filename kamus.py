import time;

kamus_ind_jawa = {'utara':'lor','selatan':'kidul','barat':'kulon','timur':'wetan'}


print('kamus arah jawa')
print(f"utara = {kamus_ind_jawa['utara']}")
print(f"timur = {kamus_ind_jawa['timur']}")

print("-----------------------------------------")
date = time.asctime( time.localtime(time.time()) )
print(date)
print("----------------------------------------")

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print ("Nama :", dict['Name'])
print ("Umur: ", dict['Age'])
print("-----------------------------------------")
print('\nData ini dikirim oleh server Gojek, untuk memberikan informasi driver disekitramu')
data_dari_server_gojek={
    'tanggal':'2020-06-13',
    'driver_list':[
        {'nama':'Zara','jarak':100},
        {'nama':'Putra','jarak':20},
        {'nama':'Wahyu','jarak':200},
        {'nama':'Anto','jarak':3200},
    ]
}
print(data_dari_server_gojek)
print(f"\nDriver disekitar sini {data_dari_server_gojek['driver_list']}")
print("Data driver sekitarmu",data_dari_server_gojek['driver_list'])
print('-------------------------------------------------------')
print(f"Driver 1 {data_dari_server_gojek['driver_list'][0]}")
print("Driver 2",data_dari_server_gojek['driver_list'][1])
print('-------------------------------------------------------')
print(f"Driver terdekat berjarak {data_dari_server_gojek['driver_list'][1]['jarak']} meter")
print("Driver terjauh berjarak", data_dari_server_gojek['driver_list'][3]['jarak'], "meter")