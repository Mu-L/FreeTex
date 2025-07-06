import re

import requests
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import (
    QApplication,
    QDialog,
    QHBoxLayout,
    QLabel,
    QMenu,
    QVBoxLayout,
)

from constants import SOFTWARE_VERSION
from qfluentwidgets import (
    InfoBar,
    InfoBarPosition,
    PushButton,
)


class UpdateCheckerThread(QThread):
    """版本检查线程"""
    updateAvailable = pyqtSignal(str)  # 有新版本时发出信号
    noUpdate = pyqtSignal()  # 没有新版本时发出信号
    error = pyqtSignal(str)  # 检查出错时发出信号

    def __init__(self, current_version):
        super().__init__()
        self.current_version = current_version

    def run(self):
        try:
            # 获取最新release信息
            response = requests.get(
                "https://api.github.com/repos/zstar1003/FreeTex/releases/latest",
                timeout=10
            )

            response.raise_for_status()
            latest = response.json()
            latest_version = latest["tag_name"]

            # 移除版本号前的'v'进行比较
            current = self.current_version.lstrip('v').split('.')
            latest = latest_version.lstrip('v').split('.')

            # 转换版本号为整数进行比较
            current = [int(re.sub(r'\D', '', x)) for x in current]
            latest = [int(re.sub(r'\D', '', x)) for x in latest]

            # 比较版本号
            if latest > current:
                self.updateAvailable.emit(latest_version)
            else:
                self.noUpdate.emit()
        except Exception as e:
            self.error.emit(str(e))

class AboutDialog(QDialog):
    """关于软件对话框"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("关于软件")
        self.setWindowFlags(Qt.Dialog | Qt.MSWindowsFixedSizeDialogHint | Qt.WindowCloseButtonHint)
        self.setModal(True)
        self.setFixedSize(500, 400)  # 增加高度以获得更好的间距

        self.update_checker = None

        # 创建主布局
        layout = QVBoxLayout(self)
        layout.setSpacing(16)  # 减小间距
        layout.setContentsMargins(32, 32, 32, 32)  # 增加外边距
        layout.setAlignment(Qt.AlignCenter)

        # 软件名称和版本
        title_label = QLabel(f"FreeTex {SOFTWARE_VERSION}")
        title_label.setStyleSheet("""
            font-size: 28px;
            font-weight: bold;
            padding: 12px;
            margin-bottom: 8px;
            background: transparent;
            selection-background-color: rgb(204, 232, 255);
            selection-color: black;
        """)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setTextInteractionFlags(Qt.TextSelectableByMouse)
        title_label.setCursor(QCursor(Qt.IBeamCursor))
        layout.addWidget(title_label)

        # 添加分隔空间
        layout.addSpacing(8)

        # 制作者信息
        author_label = QLabel("制作者：zstar")
        author_label.setStyleSheet("""
            font-size: 16px;
            margin: 4px 0;
            background: transparent;
            selection-background-color: rgb(204, 232, 255);
            selection-color: black;
        """)
        author_label.setAlignment(Qt.AlignCenter)
        author_label.setTextInteractionFlags(Qt.TextSelectableByMouse)
        author_label.setCursor(QCursor(Qt.IBeamCursor))
        layout.addWidget(author_label)

        # 微信公众号
        wechat_label = QLabel("微信公众号：我有一计")
        wechat_label.setStyleSheet("""
            font-size: 16px;
            margin: 4px 0;
            background: transparent;
            selection-background-color: rgb(204, 232, 255);
            selection-color: black;
        """)
        wechat_label.setAlignment(Qt.AlignCenter)
        wechat_label.setTextInteractionFlags(Qt.TextSelectableByMouse)
        wechat_label.setCursor(QCursor(Qt.IBeamCursor))
        layout.addWidget(wechat_label)

        # 理念
        concept_label = QLabel("理念：一直致力于构建免费好用的软件")
        concept_label.setStyleSheet("""
            font-size: 16px;
            margin: 4px 0;
            background: transparent;
            selection-background-color: rgb(204, 232, 255);
            selection-color: black;
        """)
        concept_label.setAlignment(Qt.AlignCenter)
        concept_label.setWordWrap(True)
        concept_label.setTextInteractionFlags(Qt.TextSelectableByMouse)
        concept_label.setCursor(QCursor(Qt.IBeamCursor))
        layout.addWidget(concept_label)

        # 项目地址
        github_label = QLabel("项目地址：https://github.com/zstar1003/FreeTex")
        github_label.setStyleSheet("""
            font-size: 16px;
            margin: 4px 0;
            background: transparent;
            selection-background-color: rgb(204, 232, 255);
            selection-color: black;
        """)
        github_label.setAlignment(Qt.AlignCenter)
        github_label.setTextInteractionFlags(Qt.TextSelectableByMouse)
        github_label.setCursor(QCursor(Qt.IBeamCursor))
        layout.addWidget(github_label)

        # 添加一个弹性空间
        layout.addStretch(1)

        # 底部按钮
        button_layout = QHBoxLayout()
        button_layout.setSpacing(16)  # 增加按钮之间的间距
        button_layout.setAlignment(Qt.AlignCenter)  # 按钮居中对齐
        
        self.updateButton = PushButton("检查更新")
        self.updateButton.clicked.connect(self.check_update)
        
        self.closeButton = PushButton("关闭")
        self.closeButton.clicked.connect(self.accept)
        
        button_layout.addWidget(self.updateButton)
        button_layout.addWidget(self.closeButton)
        layout.addLayout(button_layout)

        # 设置窗口样式
        self.setStyleSheet("""
            QDialog {
                background-color: white;
            }
            PushButton {
                padding: 8px 24px;
                font-size: 14px;
                min-width: 120px;
                border: 1px solid rgba(0, 0, 0, 0.073);
                border-radius: 5px;
                border-bottom: 1px solid rgba(0, 0, 0, 0.183);
                background: rgba(255, 255, 255, 0.7);
                color: black;
            }
            PushButton:hover {
                background: rgba(249, 249, 249, 0.5);
            }
            PushButton:pressed {
                color: rgba(0, 0, 0, 0.63);
                background: rgba(249, 249, 249, 0.3);
                border-bottom: 1px solid rgba(0, 0, 0, 0.073);
            }
            PushButton:disabled {
                color: rgba(0, 0, 0, 0.36);
                background: rgba(249, 249, 249, 0.3);
                border: 1px solid rgba(0, 0, 0, 0.06);
                border-bottom: 1px solid rgba(0, 0, 0, 0.06);
            }
            QLabel {
                background: transparent;
            }
            QMenu {
                background-color: white;
                color: black;
                border: 1px solid rgb(200, 200, 200);
                padding: 4px;
            }
            QMenu::item {
                padding: 4px 24px 4px 24px;
                border: 1px solid transparent;
                background: transparent;
            }
            QMenu::item:selected {
                background-color: rgb(204, 232, 255);
            }
            QMenu::separator {
                height: 1px;
                background: rgb(200, 200, 200);
                margin: 4px 0px 4px 0px;
            }
        """)

        # 为所有标签设置自定义上下文菜单
        for label in [title_label, author_label, wechat_label, concept_label, github_label]:
            label.setContextMenuPolicy(Qt.CustomContextMenu)
            label.customContextMenuRequested.connect(lambda pos, l=label: self.showLabelContextMenu(pos, l))  # noqa: E741

    def check_update(self):
        """检查更新"""
        # 禁用检查更新按钮
        self.updateButton.setEnabled(False)
        self.updateButton.setText("正在检查...")

        # 创建并启动检查线程
        self.update_checker = UpdateCheckerThread(SOFTWARE_VERSION)
        self.update_checker.updateAvailable.connect(self.on_update_available)
        self.update_checker.noUpdate.connect(self.on_no_update)
        self.update_checker.error.connect(self.on_check_error)
        self.update_checker.finished.connect(lambda: self.updateButton.setEnabled(True))
        self.update_checker.start()

    def on_update_available(self, new_version):
        """有新版本可用"""
        self.updateButton.setText("检查更新")
        InfoBar.success(
            title="发现新版本",
            content=f"有新版本 {new_version} 可用，请前往 GitHub 下载",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            duration=5000,
            parent=self
        )

    def on_no_update(self):
        """当前已是最新版本"""
        self.updateButton.setText("检查更新")
        InfoBar.info(
            title="检查更新",
            content="当前已是最新版本",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            duration=2000,
            parent=self
        )

    def on_check_error(self, error_msg):
        """检查更新出错"""
        self.updateButton.setText("检查更新")
        InfoBar.error(
            title="检查更新失败",
            content=f"错误信息：{error_msg}",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            duration=3000,
            parent=self
        )

    def showLabelContextMenu(self, pos, label):
        """显示标签的上下文菜单"""
        menu = QMenu(self)
        copyAction = menu.addAction("复制")
        copyAction.triggered.connect(lambda: QApplication.clipboard().setText(label.text()))
        menu.exec_(label.mapToGlobal(pos))

    def showEvent(self, event):
        """显示事件，用于居中显示对话框"""
        super().showEvent(event)
        if self.parent():
            parent_geo = self.parent().geometry()
            x = parent_geo.x() + (parent_geo.width() - self.width()) // 2
            y = parent_geo.y() + (parent_geo.height() - self.height()) // 2
            self.move(x, y) 