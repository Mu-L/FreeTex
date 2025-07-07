<div align="center">
  <img src="resources/images/logo.png" width="400" alt="FreeTex">
</div>

<div align="center">
  <img src="https://img.shields.io/badge/Version-1.0.0-blue" alt="Version">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-AGPL3.0-green" alt="License"></a>
  <h4>
    <a href="README.md">🇨🇳 Chinese</a>
    <span> | </span>
    <a href="README_EN.md">🇬🇧 English</a>
  </h4>
</div>

## 🌟 Introduction

FreeTex is a free intelligent formula recognition software that can identify mathematical formulas in images and convert them into editable LaTeX format.

Features:

- No internet connection required  
  Uses locally deployed models, eliminating the need for network calls and ensuring complete data privacy

- Multi-type image recognition
  Supports recognition of various image types including handwritten, printed, and scanned formulas

- Simple and user-friendly operation
  Supports three operation modes: image upload, screenshot, and paste, with shortcut keys for improved efficiency

- Multiple export formats
  Recognition results can be directly copied to Word or LaTeX format with one click, no additional operations needed

- Multiple recognition engine support
  Supports both local recognition and multimodal model recognition

Video demonstration and tutorial:

[![FreeTex: Free Intelligent Formula Recognition Tool](https://i0.hdslb.com/bfs/archive/54175a1a4552c6236d05188bb63ff9ff26ccea54.jpg@672w_378h_1c.avif)](https://www.bilibili.com/video/BV1zPV2zVEMG)

## 📦 Usage

### 1. Quick Start

1. Download the software

For Windows:

- [Baidu Netdisk Download](https://pan.baidu.com/s/1MupcVrl4epva1UP-bSWovg?pwd=8888)(Extraction code: 8888)

For macOS:

- [Baidu Netdisk Download](https://pan.baidu.com/s/1NstYEU4TcWubJSAO8WcLTw?pwd=8888)(Extraction code: 8888)

2. Install the software and start using

For specific usage instructions, please refer to the tutorial above.

> [!NOTE]
> For Windows version, the software must be placed in a non-Chinese path to run properly.

### 2. Run from Source

#### Environment Setup

Create a new environment:

```bash
conda create -n freetex python=3.8
conda activate freetex
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Replace CPU-based PyTorch with GPU version:

```bash
pip install torch==2.4.0 torchvision==0.19.0 --index-url https://download.pytorch.org/whl/cu118
```

#### Download Model

Download the `unimernet_small` model and place it under `models`:

```bash
cd models
git lfs install
git clone https://huggingface.co/wanderkid/unimernet_small
```

#### Compile Resource Files

```bash
pyrcc5 resources/app.qrc -o resources/app_rc.py -compress 3
```

#### Launch Application

```bash
python main.py
```

Once running, the usage is the same as the quick start method above.

# 🏗️ Project Structure

```
FreeTex/
├── .gitignore
├── .python-version
├── LICENSE
├── README.md
├── README_EN.md
├── config.json
├── demo.yaml
├── docs/
│   ├── images/
│   ├── index.html
│   ├── script.js
│   └── style.css
├── libs/
│   ├── index.html
│   └── katex/
├── main.py
├── main.spec
├── models/
├── pyproject.toml
├── qfluentwidgets/
├── requirements.txt
├── resources/
├── scripts/
├── test_imgs/
├── tools/
├── unimernet/
└── uv.lock
```

## 📮 Notice
**Call for Bad Cases:** If you have encountered any cases where the model performs poorly, I would greatly appreciate it if you could share them in the issue.

## 🚀 Acknowledgements

This project is based on the following open-source projects:

* [UniMERNet](https://github.com/opendatalab/UniMERNet)
* [PyQt-Fluent-Widgets](https://github.com/zhiyiYo/PyQt-Fluent-Widgets)
* [KaTeX](https://github.com/KaTeX/KaTeX)

Thanks to all the contributors:

<a href="https://github.com/zstar1003/FreeTex/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=zstar1003/FreeTex" />
</a>

## Star History

![Star History](https://starchart.cc/zstar1003/FreeTex.svg)
