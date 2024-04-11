# io.UnsupportedOperation: not readable

with open('example.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    print(lines) # 👉️ ['bobby\n', 'hadz\n', 'com']