<div align="center">
  <img src="resources/images/logo.png" width="400" alt="FreeTex">
</div>

<div align="center">
  <img src="https://img.shields.io/badge/版本-1.0.0-blue" alt="版本">
  <a href="LICENSE"><img src="https://img.shields.io/badge/许可证-AGPL3.0-green" alt="许可证"></a>
  <h4>
    <a href="README.md">🇨🇳 中文</a>
    <span> | </span>
    <a href="README_EN.md">🇬🇧 English</a>
  </h4>
</div>

## 🌟 简介

FreeTex是一个免费的公式智能识别软件，它可以识别图像中的数学公式并将其转换为可编辑的Latex格式。

视频演示及操作教程：

[![FreeTex：免费的智能公式识别神器](https://i0.hdslb.com/bfs/archive/54175a1a4552c6236d05188bb63ff9ff26ccea54.jpg@672w_378h_1c.avif)](https://www.bilibili.com/video/BV1zK31zKEPp)

想对识别结果进行编辑？可以看看我的工具站：https://xdxsb.top/FreeTool

## 📦 使用方式

### 1. 快速使用

1. 下载软件

- windows系统：

  - [Github](https://github.com/zstar1003/FreeTex/releases/download/v1.0.0/FreeTex_setup_v1.0.0.exe)
  - [夸克网盘](https://pan.quark.cn/s/6d094961e2c3)

- macos系统(arm)：

  - 方式一；直接下载：[Github](https://github.com/zstar1003/FreeTex/releases/download/v1.0.0/FreeTex-Installer-1.0.0.dmg)
  - 方式二；用Homebrew进行安装：`brew install freetex`
  > [!NOTE]
  > mac版本使用多模态模型时，会出现`No module named 'openai'`这个问题，解决方式见[issue#44](https://github.com/zstar1003/FreeTex/issues/44)


2. 安装软件，开始使用

  具体使用方式可参考上面的适配教程。

  > [!NOTE]
  > windows版本使用时需放置软件在非中文路径下，否则无法正常启动。

### 2. 源码运行

> [!NOTE]
> 请注意：主分支是在mac环境下进行开发，如果是windows环境，建议切换至本项目的win分支。

#### 配置环境

uv:
```bash
uv sync
```

#### 下载模型

下载unimernet_small模型放置在`models`下:

下载方式：
```bash
cd models
git lfs install
git clone https://huggingface.co/wanderkid/unimernet_small
```

#### 运行软件

```bash
python main.py
```

运行后，软件操作方式与上一节相同。


## 🚀 鸣谢

本项目基于以下开源项目开发：

- [UniMERNet](https://github.com/opendatalab/UniMERNet)

- [PyQt-Fluent-Widgets](https://github.com/zhiyiYo/PyQt-Fluent-Widgets)

- [KaTeX](https://github.com/KaTeX/KaTeX)

感谢此项目贡献者们：

<a href="https://github.com/zstar1003/FreeTex/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=zstar1003/FreeTex" />
</a>

## Star History

![Star History](https://starchart.cc/zstar1003/FreeTex.svg)