## ☘️Introduction

此目录用于**存放 & 编辑** seldom 相关文档

## 📖 Document

[中文文档](https://seldomqa.github.io/)

[English document(readthedocs)](https://seldomqa.readthedocs.io/en/latest/index.html)

## 结构

```shell
docs/
├── README.md
├── conf.py # rst文档配置文件
├── deploy.sh # vuepress文档部署脚本
├── index.rst
├── markdown2rst.py # md转rst脚本
├── package.json
├── requirements.txt # python模块依赖
├── rst_docs # 用于存放rst文档
├── vpdocs # 用于vuepress文档
│   ├── README.md
│   ├── advanced
│   ├── db
│   ├── getting-started
│   ├── http
│   ├── introduce.md
│   ├── other
│   └── platform
└── yarn.lock
```

## 如何贡献文档

1. clone 本项目

```bash
git clone https://github.com/SeldomQA/seldom.git
```

2. 进入到文档目录

```bash
cd docs
```

3. 编辑相关文档（推荐编辑 vpdocs 目录下的文档，该目录的文档也是 seldom 的主要文档）

4. push 到 vuepress-docs 分支
