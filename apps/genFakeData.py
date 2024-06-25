import random
import string

def generate_random_id(existing_ids, num_ids=10):
    """生成指定數量的隨機ID，並確保有重複"""
    while len(existing_ids) < num_ids:
        new_id = random.choice(string.ascii_uppercase) + ''.join(random.choices(string.digits, k=9))
        existing_ids.append(new_id)
    return existing_ids

def generate_random_value():
    """生成一個隨機的數值，範圍從 -20 到 20"""
    return random.randint(-20, 20)

def generate_random_entry(existing_ids):
    """生成一個隨機的條目，條目格式為 ID,值，條目數量隨機"""
    num_entries = random.randint(1, 5)
    entries = []
    for _ in range(num_entries):
        entry_id = random.choice(existing_ids)
        entry_value = generate_random_value()
        entries.append(f"{entry_id},{entry_value}")
    return '|'.join(entries)

def generate_random_data(num_lines, num_ids):
    """生成多行隨機資料"""
    data = []
    existing_ids = generate_random_id([], num_ids)
    for _ in range(num_lines):
        data.append(generate_random_entry(existing_ids))
    return data

# 接受用戶輸入的資料行數
file_name = input("請輸入要生成的文件名: ")
num_lines = int(input("請輸入要生成的資料行數: "))
num_ids = int(input("請輸入要生成的隨機ID數量: "))

# 生成對應行數的隨機資料
random_data = generate_random_data(num_lines, num_ids)

data_path = '../data/'
file_name = f'{file_name}.txt'
file_path = data_path + file_name
# 將生成的隨機資料寫入到 output.txt 文件中
with open(file_path, 'w') as file:
    for line in random_data:
        file.write(line + '\n')

print(f"隨機資料已寫入到 {file_name}.txt 文件中。")
