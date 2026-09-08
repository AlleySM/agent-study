# 题1 列表推导：nums=range(1,21)，一行取出所有偶数
nums = [x for x in range(1, 21) if x % 2 == 0]
# 题2 在题1基础上：生成这些偶数的平方列表（过滤+变换一起做）
squares = [x**2 for x in range(1, 21) if x % 2 == 0]
# 题3 words=['IT','rpa','Python','fastapi','db']：一行转成大写，且只保留长度>=3 的
words=['IT','rpa','Python','fastapi','db']
words=[word.upper() for word in words if len(word) >= 3]
# 题4 字典推导：生成 {1:1, 2:4, 3:9, 4:16, 5:25}
nums = {x: x**2 for x in range(1,6)}
# 题5 给定 d={'a':1,'b':2,'c':3}：一行筛出 值>1 的键值对，组成新字典
d = d={'a':1,'b':2,'c':3}
d = {k: v for k,v in d.items() if v >1}
# 题6 集合推导：[1,1,2,2,3,4,4,5] 一行去重；再用集合推导求这些词各自的长度 {'it','rpa',...}
lens = {len(x) for x in [1,1,2,2,3,4,4,5]} 
# 题7 嵌套推导：把二维 [[1,2],[3,4],[5,6]] 拍平成一维 [1,2,3,4,5,6]
nums = [x for y in [[1,2],[3,4],[5,6]] for x in y]
# 题8 生成器表达式：g=(x*x for x in range(1_000_000))
#     打印 type(g)；用 next(g) 连取3次；再 sum(g)；对比 [x*x for ...] 列表版的内存差别
g = (x * x for x in range(1_000_000))   # 圆括号 -> 生成器
print(type(g))        # <class 'generator'>，此刻并没有真的算一百万个值
print(next(g), next(g), next(g))        # 取一个算一个：0 1 4
print(sum(g))         # 惰性把剩下的累加完
