username = input('请输入你的姓名：')
print(
    '您好，',
    username,
)
bornyear = input('接下来，请输入你的出生年份：')
bbyear = int(bornyear)
old = 2019 - bbyear
print(username, '，你的年龄是：', old, '岁')
if old >= 18:
    print("恭喜你，你已经是一个成年人了")
else:
    print('哎呀，你还是个宝宝呢')
