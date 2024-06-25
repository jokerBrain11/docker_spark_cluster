import random
import datetime

# 生成假資料的數量
num_rows = 10000000
num_urls = 200

# 生成唯一的 url_id 和 url
unique_url_ids = random.sample(range(1000, 14000), num_urls)
urls = [f"{random.choice('abcdefghijklmnopqrstuvwxyz')}{random.choice('abcdefghijklmnopqrstuvwxyz')}{random.choice('abcdefghijklmnopqrstuvwxyz')}.example.com" for _ in range(num_urls)]

# 生成範例2數據
data2 = list(zip(unique_url_ids, urls))

# 確保範例1數據中的url_id對應範例2數據中的url_id
data1 = []
used_url_ids = random.sample(unique_url_ids, 2)  # 選擇兩個 url_id 來重複使用
for i in range(num_rows):
    id = random.randint(10000000, 99999999)
    type = random.choice(['G', 'H', 'I'])
    date = (datetime.date(2020, 2, 29) + datetime.timedelta(days=random.randint(0, 365))).isoformat()
    if i < 2:
        url_id = used_url_ids[i]
    else:
        url_id = random.choice(unique_url_ids)
    count = random.randint(1, 20)
    count2hr = random.randint(1, 10)
    data1.append([id, type, date, url_id, count, count2hr])

data_path = '../data/'
file_path1 = data_path + 'data1.txt'
file_path2 = data_path + 'data2.txt'

# 將範例1數據寫入TXT
with open(file_path1, 'w') as file:
    file.write('id, type, date, url_id, count, count2hr\n')
    for row in data1:
        file.write(','.join(map(str, row)) + '\n')

# 將範例2數據寫入TXT
with open(file_path2, 'w') as file:
    file.write('url_id, url\n')
    for row in data2:
        file.write(f"{row[0]},{row[1]}\n")

print("假資料生成完畢，已寫入 data1.txt 和 data2.txt")

