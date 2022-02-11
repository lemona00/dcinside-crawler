import os
import sys
import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from crawler import Crawl


class Crawler(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # 창 설정
        self.setWindowTitle('crawl')
        self.setFixedSize(300, 280)

        # 갤러리 ID (현재는 불필요, 추후 확장을 위해)
        self.id_label = QLabel(self)
        self.id_label.setText("갤러리 아이디 입력 (현재는 입력 x)")
        self.id_label.setGeometry(10, 10, 270, 20)

        self.id_lineEdit = QLineEdit(self)
        self.id_lineEdit.setPlaceholderText("taeyeon_new1")
        self.id_lineEdit.setGeometry(10, 30, 200, 20)
        self.id_lineEdit.setReadOnly(True)

        # tag widgets
        self.tag_label = QLabel(self)
        self.tag_label.setText("태그 입력")
        self.tag_label.setGeometry(10, 50, 150, 20)
        self.tag_lineEdit = QLineEdit(self)
        self.tag_lineEdit.setPlaceholderText("제목 태그 입력 ex)[xx갤]")
        self.tag_lineEdit.setGeometry(10, 70, 200, 20)

        # 시작과 끝 페이지 지정 스핀박스

        self.page_label = QLabel(self)
        self.page_label.setText("페이지 지정")
        self.page_label.setGeometry(10, 90, 200, 20)

        self.page_spin_start = QSpinBox(self)
        self.page_spin_end = QSpinBox(self)

        self.page_start_label = QLabel(self)
        self.page_start_label.setText("페이지~")

        self.page_end_label = QLabel(self)
        self.page_end_label.setText("페이지")

        self.page_spin_start.setGeometry(10, 110, 30, 20)

        self.page_start_label.setGeometry(50, 110, 60, 20)

        self.page_spin_end.setGeometry(110, 110, 30, 20)

        self.page_end_label.setGeometry(160, 110, 60, 20)

        self.page_spin_start.setMinimum(1)
        self.page_spin_end.setMinimum(1)

        self.page_spin_start.valueChanged.connect(self.spin_value_changed)
        self.page_spin_end.valueChanged.connect(self.spin_value_changed)

        # 저장 버튼
        self.btn = QPushButton("저장 및 실행", self)
        self.btn.setGeometry(10, 150, 90, 40)
        self.btn.clicked.connect(self.save_and_start)

        # 상태창
        self.status_label = QLabel(self)
        self.status_label.setText("상태")
        self.status_label.setGeometry(10, 230, 90, 20)

    # 저장과 시작 버튼 클릭 이벤트

    def save_and_start(self):
        save = QFileDialog.getSaveFileName(self, "파일 저장", "%s" % time.strftime(
            "%Y-%m-%d", time.localtime(time.time())),
            "csv(*.csv);;메모장(*.txt)")

        if save[0] == "":
            error = QMessageBox()
            error.about(self, "파일 지정", "파일 위치를 지정해주세요")
        else:
            first_page = self.page_spin_start.value()
            last_page = self.page_spin_end.value()
            tag = self.tag_lineEdit.text()

            cw = Crawl()
            cw.run(first_page, last_page, save[0], tag)

    # 스핀박스 값 예외 방지용

    def spin_value_changed(self):
        if self.page_spin_start.value() > self.page_spin_end.value():
            self.page_spin_end.setValue(self.page_spin_start.value())
