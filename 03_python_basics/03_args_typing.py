# 题1 序列解包：把三元组直接拆给三个变量，打印验证
t = ('FastAPI', 0.141, True)
first, second, third = t
print(first, second, third)   # 预期：FastAPI 0.141 True

# 题2 *rest 收集：先口答 first/middle/last 分别是什么，再跑
first, *middle, last = [1, 2, 3, 4, 5]
print(f"first: {first} ; middle: {middle}; last: {last}")
print(first, middle, last)   # 预期：1 [2, 3, 4] 5

# 题3 解包调用：星号把列表"抖开"传给函数
def total(*nums):
    return sum(nums)
print(total(1, 2, 3, 4, 5))  # 预期 15
nums = [1, 2, 3]
print(total(*nums))          # 预期 6 ← 这行的 *nums 就是解包调用

# 题4 **kwargs 收集关键字参数
def show(**kw):
    for k, v in kw.items():
        print(k, '=', v)
show(name='张三', dept='IT')          # 预期两行
d = {'name': '李四', 'dept': '行政'}
show(**d)                            # 双星号把字典"抖开"传进去

# 题5 组合（就是你 FastAPI 的雏形）：位置参数 + 不定参数
def create_user(name: str, age: int, **extra):
    print(name, age, extra)
create_user('王五', 28, dept='IT', phone='139****')
# 预期：王五 28 {'dept': 'IT', 'phone': '139****'}

# 题6 给函数加类型注解（注解不影响运行，但 IDE 会提示你）
def filter_evens(nums: list[int]) -> list[int]:
    return [x for x in nums if x % 2 == 0]
print(filter_evens([1, 2, 3, 4]))    # 预期 [2, 4]

# 题7 str | None 的含义：返回值"可能是字符串，可能没有"
def find_user(user_id: int, data: dict[str, str]) -> str | None:
    return data.get(str(user_id))
print(find_user(1, {'1': 'Alice'}))  # 预期 Alice
print(find_user(2, {'1': 'Alice'}))  # 预期 None ← 没有这个用户

    
