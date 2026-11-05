# 🚀 JSONPlaceholder API 自动化测试框架

[![API Automated Test](https://github.com/LYXIN6868/api_auto_demo/actions/workflows/api-test.yml/badge.svg)](https://github.com/LYXIN6868/api_auto_demo/actions/workflows/api-test.yml)
基于 Python + Pytest + Requests + Allure 搭建的接口自动化测试框架。采用分层设计思想，实现了接口请求封装、全局日志收集与 CI/CD 持续集成。

# 核心特性与优化点

- API Object 设计模式：将接口定义与测试逻辑彻底解耦。在 `api/` 层统一管理接口请求，测试用例只关注业务参数与断言，极大提升了代码的可维护性。
- 全局日志监控 (Hook)：利用 `requests.Session` 的 Hook 机制结合 `logging` 模块，自动拦截并记录每次请求的 Method、URL、状态码、耗时与响应体，方便报错时快速定位问题。
- 精细化 Allure 报告：集成 Allure 装饰器（Epic/Feature/Story）与 `step` 步骤管理，实现测试用例的可视化呈现与失败节点的精准追踪。
- CI/CD 自动化：配置 GitHub Actions，代码 Push 到 `main` 分支即自动触发云端回归测试，并支持生成并上传 Allure 测试制品（Artifacts）。

# 技术栈

- 语言：Python 3.x
- 测试框架：Pytest
- 请求库：Requests
- 报告：Allure-pytest
- CI/CD：GitHub Actions

# 项目结构

```text
api-auto-demo/
├── api/                  # API Object 层（接口封装）
│   └── post_api.py       
├── data/                 # 数据驱动层
│   └── post_data.yaml    # YAML 测试数据
├── tests/                # 测试用例层
│   ├── test_posts.py     
│   └── test_smoke.py     
├── utils/                # 工具层
│   └── logger.py         # 全局日志封装
├── config.py             # 环境配置（BASE_URL）
├── conftest.py           # 全局 Fixture 与 Session 钩子
├── pytest.ini            # Pytest 运行配置
└── requirements.txt      # 依赖清单

# 如何运行
    安装依赖：pip install -r requirements.txt
    运行测试并生成报告数据：pytest --alluredir=./allure-results
    查看可视化测试报告：allure serve ./allure-results

