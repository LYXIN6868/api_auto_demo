# JSONPlaceholder API 自动化测试框架

基于 Python + Pytest + Requests 搭建的接口自动化项目。

## 技术栈
- Python 3.x
- Pytest
- Requests
- Allure 

## 项目结构
- `config.py`: 存放环境基础配置
- `conftest.py`: 存放全局 Fixture (如 Session 管理)
- `tests/`: 存放测试用例
- `测试用例表格.xlsx`: 测试用例设计清单

## 如何运行
1. 安装依赖：`pip install -r requirements.txt`
2. 执行测试：`pytest`