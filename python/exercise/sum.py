
"""
小明买一个西瓜还差5元，小花买这个西瓜还差10元，两人的钱加在一起还差3元。请问西瓜多少钱？
"""

def qian(a, b, c):
    x = a - c
    y = x + b
    return y


z = qian(5, 10, 3)
print(z)
