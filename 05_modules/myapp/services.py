from myapp.models import ITAssetDC

def show_all(assets: list[ITAssetDC]) -> list[str]:
    return [str(asset) for asset in assets]
def checkout(assets: list[ITAssetDC], asset_id: str, owner: str) -> str:
    for asset in assets:
        if asset.asset_id == asset_id:
            if asset.status == '已借出':
                raise ValueError(f"{asset_id}已被借出")
            asset.status = '已借出'
            asset.owner = owner
            return f"{asset.asset_id} {asset.kind}被借出给{owner}"

    raise ValueError(f"查不到Asset_id为{asset_id!r}的设备")

        

def back(assets: list[ITAssetDC], asset_id: str) -> str:
    for asset in assets:
        if asset.asset_id == asset_id:
            if asset.status == '在库':
                raise ValueError(f"{asset_id}已在库, 请检查Asset_id是否正确")
            asset.status = '在库'
            asset.owner = '仓库'
            return f"{asset.asset_id} {asset.kind}已归还到仓库"

    raise ValueError(f"查不到Asset_id为{asset_id!r}的设备")


def stats(assets: list[ITAssetDC]) -> dict[str, int]:
    checkoutCountKey, inStockCountKey = '已借出', '在库'
    checkoutCount, inStockCount = 0, 0
    stats = {checkoutCountKey: checkoutCount, inStockCountKey: inStockCount}
    for asset in assets:
            if asset.status == '已借出':
                stats[checkoutCountKey] = stats[checkoutCountKey] + 1
            elif asset.status == '在库':
                stats[inStockCountKey] = stats[inStockCountKey] + 1
    return stats


