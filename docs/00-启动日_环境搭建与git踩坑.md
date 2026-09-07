# 第0篇 - 启动日: 现代开发环境搭建 + Git 踩坑实录

> 日期: 2026-09-06 ~ 09-07 对应计划: 启动日 + W1 [现代开发环境]
> 学习时长: 3h 环境: Windows11 / Python 3.10 3.13 / uv 0.12 / VSCode

## 1. 今天要解决什么、最终完成什么
- 目标：搭好工程化开发环境、跑通第一个FastAPI、代码上GitHub
- 完成清单：逐条列：venv/uv、pyproject、FastAPI、VSCode调试、GitHub仓库

## 2. Python 虚拟环境隔离原理（用自己的话讲清）
- pyvenv.cfg 里有什么、home 和 include-system-site-packages=false 各管什么：home标明本地Python的路径,include-system-site-packages=false这句话是关键，运行时 sys.path 不加载全局 site-packages，所以 import 看不到全局包
- Activate.ps1 到底改了什么：只把 `.venv\Scripts` 顶到 PATH 最前 + 设提示符 `(.venv)`，敲 python/pip 命中 venv（命令选择隔离）
- 包装到哪里、为什么各项目互不影响：venv 自己的 pip 把包装进 venv 专属的 `Lib\site-packages`（不是全局的），每个 venv 各装各的
- 怎么验证自己在虚拟环境里: `where.exe python` 首行指向 `.venv`；且 `sys.prefix` 是 .venv、`sys.base_prefix` 是母体 Python，**两者路径不同**

## 3. 老式 venv+pip vs 现代 uv+pyproject（对比表）
| 维度 | venv + pip + requirements | uv + pyproject + uv.lock |
|---|---|---|
| 创建/激活/装包 | `python -m venv .venv` 建 → `Activate.ps1` 激活 → `pip install` 装 | `uv init` 建骨架、`uv add` 一条搞定建环境 + 装包，`uv run` 不用手动激活 |
| 直接依赖 vs 全量锁定 | freeze 把所有包平铺，不分直接 / 间接，还混无关包 | pyproject 只写直接依赖 + 版本范围，uv.lock 精确锁全量 (含间接) |
| 换机器复现 | `pip install -r requirements.txt`，版本可能漂移 | `uv sync` 按 lock 装出一模一样的环境 |
- 常用 uv 命令：init / add / add --dev / run / sync，各自作用：`init` 建骨架 / `add` 加直接依赖 / `add --dev` 加开发依赖 / `run` 免激活运行 / `sync` 按 lock 还原 
- 为什么 uv.lock 要提交、.venv 不提交：uv.lock精确锁定fastapi/uvicorn 及其所有间接依赖的确切版本和哈希，保证换机器装出一模一样的环境，要提交 Git，而.venv是uv 自动建的本项目专属虚拟环境，只需要本地安装即可

## 4. 第一个 FastAPI
- 路由函数是什么、@app.get("/") 和下面 def 的关系：被 `@app.get('路径')` 装饰器紧贴修饰的函数就是路由函数，装饰器把 URL 和函数绑定，访问该路径时执行它
- /docs 能干什么：它是 FastAPI **自动生成的交互式接口文档网页（Swagger UI）**，能在页面上直接点 Try it out → Execute 测每个接口，不是磁盘上的文件夹
- 怎么用 launch.json 给 FastAPI 打断点（注意别加 --reload）：①`Ctrl+Shift+P → Python: Select Interpreter` 选 `.venv`；②在**路由函数的 return 那一行**（main.py 里）行号左侧点红点；③F5 选「Python: FastAPI」启动；④浏览器访问 URL 才命中断点

## 5. Git 踩坑实录（重点，按「现象→原因→解决」三段式写）
### 坑1：.gitignore 没生效，1475 个 .venv 文件被暂存
现象（status 里 1475 个 .venv）→ 原因（.gitignore 是空文件且已 git add，进了**暂存区**，不是 "local"）→ 解决（补内容并保存 → `git rm -r --cached .` → `git add .`）+ 经验（.gitignore 只对未跟踪文件生效）；
### 坑2：PowerShell 里 activate 没激活成功
现象（提示符无 `(.venv)`、where 首行还是全局）→ 原因（PowerShell 跑了 bash 专用的无扩展名 activate）→ 解决（`.\.venv\Scripts\Activate.ps1`，三 shell 对应 Activate.ps1 /activate.bat/activate）；
### 坑3：winget 装完 uv 提示"无法识别"
现象（uv 无法识别）→ 原因（当前终端 PATH 是安装前旧快照）→ 解决（`$env:Path` 临时前置，或重开终端 / 重启 VSCode）；
### 补充坑：包名不能数字开头 / 冲突解决≠只删标记 / push 被 reset 怎么分层排查
包名不能数字开头（`02_dev_env`→`dev-env`，目录名可以、模块名不行）；解决冲突要连正文一起取舍、不是只删标记；push 被 reset 按 "git 配置→DNS→直连 IP:443→代理" 逐层排查；


## 6. 命令速查（今天敲过的，整理成自己的小抄）
### ① 虚拟环境 venv + pip
```powershell
python -m venv .venv                    # 创建虚拟环境（只创建，不激活）
.\.venv\Scripts\Activate.ps1           # PowerShell 激活（CMD用activate.bat，bash用activate）
where.exe python                        # 验证：首行指向 .venv 才算激活
python -m pip install 包名              # 在激活的 venv 里装包
python -m pip install -r requirements.txt   # 按文件批量装依赖
pip freeze > requirements.txt          # 导出当前环境依赖
deactivate                              # 退出虚拟环境
```
### ② uv 现代工具链
```powershell
uv init                 # 初始化项目骨架（生成 pyproject.toml）
uv add 包名              # 加直接依赖（自动建.venv+写pyproject+更新lock+安装）
uv add --dev 包名        # 加开发依赖
uv run 命令              # 用项目环境运行，无需手动激活
uv sync                 # 按 uv.lock 精确还原环境（换机器时用）
```
### ③ 运行 FastAPI 与调试
```powershell
uvicorn main:app --reload       # 命令行启动，改代码自动重载
# 启动后浏览器开 http://127.0.0.1:8000/docs 看交互式接口文档
# VSCode 调试：选解释器 → 路由函数 return 行打断点 → F5（调试别加 --reload）
```
### ④ Git 版本管理
```powershell
# —— 首次配置（只做一次）——
git init                            # 初始化本地仓库
git config --global user.name "名字"    # 配置用户名
git config --global user.email "邮箱"   # 配置邮箱
git config --global --list          # 查看全局配置
git branch -M main                  # 主分支改名 main
git remote add origin 仓库URL        # 关联 GitHub 远程
# —— 日常三板斧 ——
git status                          # 看工作区/暂存区状态
git add .                           # 改动加入暂存区
git commit -m "说明"                # 提交到本地仓库
git push origin main                # 推送到远程
git pull                            # 拉取并合并远程更新
git log --oneline                   # 查看提交历史
git checkout -b 分支名               # 新建并切换分支
git checkout 分支名                  # 切换分支
git rm -r --cached .                # 移出跟踪索引（不删硬盘），让.gitignore重新生效
```



## 7. 还没完全懂、待后面补的
SSH 默认 22 端口常被封，改走 443（HTTPS 端口，不封）


## 8. 明日计划
9/8：推导式（列表 / 字典 / 集合）、生成器与 yield、解包、match-case、类型注解 `list[str] / X | None`