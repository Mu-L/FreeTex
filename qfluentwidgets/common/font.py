# coding: utf-8
import platform
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget


def setFont(widget: QWidget, fontSize=14, weight=QFont.Normal):
    """ set the font of widget

    Parameters
    ----------
    widget: QWidget
        the widget to set font

    fontSize: int
        font pixel size

    weight: `QFont.Weight`
        font weight
    """
    widget.setFont(getFont(fontSize, weight))


def getFont(fontSize=14, weight=QFont.Normal):
    """ create font

    Parameters
    ----------
    fontSize: int
        font pixel size

    weight: `QFont.Weight`
        font weight
    """
    font = QFont()

    # 根据平台设置字体优先级,避免在macOS上查找不存在的Windows字体
    system = platform.system()
    if system == 'Darwin':  # macOS
        font.setFamilies(['PingFang SC', 'Hiragino Sans GB', 'STHeiti'])
    elif system == 'Windows':
        font.setFamilies(['Segoe UI', 'Microsoft YaHei', 'SimSun'])
    else:  # Linux 或其他
        font.setFamilies(['Noto Sans', 'Liberation Sans', 'DejaVu Sans'])

    font.setPixelSize(fontSize)
    font.setWeight(weight)
    return font