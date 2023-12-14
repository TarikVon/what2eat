# 😋 \[v1.2\] What to Eat Today?

## 📝 简介

<!-- <img src="https://www.tarikvon.cn/images/imgHost/20231214172102.png" width="50%"> -->

What to Eat Today? 是一个基于兰州大学某轻食外卖群微信点单的开发的小项目（面向个人，功能较为简单）。由于其麻烦 ~~且及其不友好~~ 的点餐流程，和某人经常要花半个小时来想今天该吃什么 ~~最终还忘记点了~~ 的情况，该项目旨在为用户提供便捷、多样化的餐饮选择，解决日常选择困难症 ~~与懒癌~~ 。

## 🛠️ 功能

本项目的主要功能包括：

- 一站式挑选菜品：再也不用在公告里面一个一个找啦\~
- 随机菜单生成：还在因为今天吃什么而烦恼吗？尝尝各种新口味叭\~

## 📘 如何使用？

### 🌐 网站在线使用：

    学习 Django 中...
    敬请期待项目部署（绝对不是因为懒）

### 🏠 本地使用（需要有 Python 环境）：

1. 📥 克隆本项目到本地：

   1.1 在线下载（推荐）：
   [what2eat.zip](https://www.tarikvon.cn/files/what2eat.zip)

   1.2 克隆仓库（需要安装 git）：

   ```bash
   cd Desktop # 此处可替换为其他路径，这里放到桌面
   git clone https://github.com/TarikVon/what2eat.git
   ```

2. ▶️ 运行程序：

   ```bash
   cd what2eat # 此处可替换为其他路径，这里打开 ./what2eat/ 文件夹
   python main.py
   ```

3. 💡 一些小技巧：

   1. 为了让用户操作更加便捷 ~~和让懒狗更懒~~ ，我们设置了用户键入回车的时候进行随机选择，你就可以从头回车到底来快速选择。
      ⚠️ 但要注意最后填写信息的时候如果选择回车，个人信息就要自己填了！
   2. `v1.2` 版本新增了对多重选择的支持，你现在可以在一个类中同时选择多项了： ~~长期爽食！！~~

      <img src="https://www.tarikvon.cn/images/imgHost/20231214171612.png" width="50%"><img src="https://www.tarikvon.cn/images/imgHost/20231214172035.png" width="50%">

## 📚 技术栈

本项目使用以下技术：

- 编程语言：Python
- Web 框架：Django
- 操作系统：Linux
- 数据库：PostgreSQL

## 🤝 贡献

我们欢迎各种形式的贡献，不论是新功能，代码审查，文档改进或是反馈建议。

## 📜 许可证

项目采用 [MIT 协议](LICENSE)。
