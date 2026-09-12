from myapp.models import ITAssetDC
from myapp.services import show_all, checkout, back, stats
from myapp.config import settings


if __name__ == "__main__":
    print(f"连接{settings.db_host}:{settings.db_port}, DEBUG={settings.debug}")
    assets = [
        ITAssetDC('A001', '笔记本', 'IT部', '张三'),
        ITAssetDC('A002', '台式机', 'IT部', '仓库'),
        ITAssetDC('A003', '打印机', 'IT部', '仓库'),
    ]
    print(show_all(assets))
    print(checkout(assets, 'A001', '李四'))
    print(back(assets, 'A001'))
    print(stats(assets))

    assert assets[0].asset_id == 'A001'
    assert assets[0].status == '在库'      # 借出后又归还
    assert assets[0].owner == '仓库'
    assert assets[1].owner == '仓库'
    print("断言全过：数据一致 ✅")