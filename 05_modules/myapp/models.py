from dataclasses import dataclass
@dataclass

class ITAssetDC:
    
    asset_id: str
    kind: str
    dept: str
    owner: str = '仓库'      # 有默认值的字段必须放后面
    status: str = '在库'


    def __str__(self):
        return f"{self.asset_id} {self.kind} {self.dept} {self.owner} {self.status}"

    def checkout(self, new_owner):
        self.owner = new_owner
        self.status = '已借出'

    def back(self):
        self.owner = '仓库'
        self.status = '在库'

    

