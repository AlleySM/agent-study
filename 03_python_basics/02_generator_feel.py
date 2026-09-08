import time, sys

N = 1_000_000

# 感受1: 建立瞬间一生成器"秒建"， 列表要真算一百万个(会顿一下)
t = time.perf_counter()
g = (x * x for x in range(N))
print("生成器建立耗时:", time.perf_counter() - t, "秒")


t = time.perf_counter()
lst = [x * x for x in range(N)]
print("列表建立耗时：", time.perf_counter() - t, "秒")

# 感受2: 内存占用 （也可以同时打开任务管理器看python内存）
print("生成器字节:", sys.getsizeof(g))
print("列表字节:", sys.getsizeof(lst), '差约', sys.getsizeof(lst) / sys.getsizeof(g), '倍')

# 感受3: 一次性一next 取走就没了， 列表反复能用
g2 = (x * x for x in range(N))
next(g2); next(g2)
print('取走2个后剩下:', list(g2))
print('再遍历一遍: ', list(g2))  # 再遍历一遍:  []
print('列表反复能用: ', lst[0], lst[0])

# 感受4: 生成求不能索引、不能 len （取消下面两行注释，亲手看报错）
# print("生成器索引:", g[0])
print('列表可以: 索引',  lst[0], 'len', len(lst))