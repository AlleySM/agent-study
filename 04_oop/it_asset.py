class ITAsset:
    def __init__(self, asset_id, kind, dept, owner='仓库'):
        # 存下：编号、类型、所属部门、当前负责人
        self.asset_id = asset_id
        self.kind = kind
        self.dept = dept
        self.owner = owner
        # 再加 self.status = '在库'
        self.status = '在库'

    def checkout(self, person):
        # 借出：负责人改成 person，状态改成 '已借出'
        self.owner = person
        self.status = '已借出'

    def back(self):
        # 归还：负责人改回 '仓库'，状态改回 '在库'
        self.owner = '仓库'
        self.status = '在库'

    def __str__(self):
        # 返回可读字符串，例如：A001 笔记本 | IT部 | 张三 | 已借出
        return f"{self.asset_id} {self.kind} | {self.dept} | {self.owner} | {self.status}"


# 测试（自己写）：
# a = ITAsset('A001', '笔记本', 'IT部', '张三')
# print(a)              # 看 __str__ 生效没
a = ITAsset('A001', '笔记本', 'IT部', '张三')
print(a)
# a.checkout('李四')
# print(a)              # 状态应变 已借出、负责人变 李四
a.checkout('李四')
print(a)
# a.back()
# print(a)              # 应回到 在库/仓库
a.back()
print(a)


class Desktop(ITAsset):
    def __init__(self, asset_id, dept, owner, cpu):
        super().__init__(asset_id, '台式机', dept, owner)  # 复用父类初始化
        self.cpu = cpu                  # 子类自己的属性

    def describe(self):
        # 返回：台式机 A002（i7-13700），状态：在库
        return f"{self.kind} {self.asset_id} ({self.cpu}) ，状态：{self.status}"

class Printer(ITAsset):
    def __init__(self, asset_id, dept, owner, ip):
        super().__init__(asset_id, '打印机', dept, owner)           # 自己补全
        self.ip = ip

    def describe(self):
        # 返回：打印机 A003（IP: 192.168.1.20），状态：在库
        return f"{self.kind} {self.asset_id} ({self.ip}) ，状态：{self.status}"

# 多态体验：同一个函数，传不同子类，输出各自的描述
def show(asset):
    print(asset.describe())

# show(Desktop(...)); show(Printer(...))
b = Desktop('A008', 'IT部', '仓库', 'i7-13700')
c = Printer('A003', 'IT部', '仓库', '192.168.1.20')
show(b)
show(c)


from dataclasses import dataclass

@dataclass
class ITAssetDC:
    asset_id: str
    kind: str
    dept: str
    owner: str = '仓库'      # 有默认值的字段必须放后面
    status: str = '在库'

# d = ITAssetDC('B001', '投影仪', '行政部')
d = ITAssetDC('A009', '空气净化器', '市场部', '张三', '已借出')
# print(b)   # 注意：你没写 __init__ 也没写 __str__，但它自动有了
print(d)

from abc import ABC, abstractmethod

class AssetBase(ABC):
    @abstractmethod
    def describe(self):
        ...        # 只声明、不实现 —— 这是"契约"：子类必须实现

# 第一步：直接 AssetBase() 实例化 → 会报 TypeError，说明抽象类不能 new
# asset = AssetBase()  # 这行会报错
# 第二步：写个 class X(AssetBase): pass 然后 X() → 也报错，因为没实现 describe
class X(AssetBase):
    pass
# X()  # 这行也会报错
# 第三步：给 X 补上 describe 方法再实例化 → 成功
class X(AssetBase):
    def describe(self):
        return "X的描述"
x = X()  # 这行不会报错
print(x.describe())  # 输出 X的描述