import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from datetime import datetime  #실시간 시간 날짜

now_time = datetime.now() #현재 시간

class layouts(QDialog):#레이아웃 나누는 class
    def __init__(self):
        QDialog.__init__(self, flags=Qt.Widget)

        #예제
        self.lb_1 = QLabel()
        self.lb_2 = QLabel()
        self.lb_3 = QLabel()
        self.lb_4 = QLabel()
        self.lb_5 = QLabel()

        #배치될 날씨 관련 위젯 변수 선언
        weather = QLabel() #날씨
        now_temperature = QLabel() #현재 온도
        now_temperature_max = QLabel() #최고 기온
        now_temperature_min = QLabel() #최저 기온
        dust = QLabel() #미세먼지
        dust_Ul = QLabel() #초미세먼지
        mask = QLabel() #마스크

        #배치될 옷차림 관련 위젯 변수 선언
        date = QLabel() #그날 날짜
        date_temperature = QLabel() #그날 온도
        date_evaluation = QLabel() #그날 평가

        # 레이아웃 선언 및 Form Widget에 설정
        self.layout_1 = QBoxLayout(QBoxLayout.LeftToRight, self)
        self.layout_2 = QBoxLayout(QBoxLayout.LeftToRight)
        self.layout_3 = QBoxLayout(QBoxLayout.TopToBottom)

        # 부모 레이아웃에 자식 레이아웃을 추가
        self.layout_1.addLayout(self.layout_2)
        self.layout_1.addLayout(self.layout_3)

        self.setLayout(self.layout_1)
        self.init_widget()


        #left_layout = QVBoxLayout #왼쪽
       # middle_layout = QVBoxLayout #중간
        #right_layout = QVBoxLayout #오른쪽

        #main_layout.addWidget(left_layout)
        #main_layout.addWidget(middle_layout)
        #main_layout.addWidget(right_layout)

        #self.layout(main_layout)

    def init_widget(self):
        self.setWindowTitle("Layout Basic")
        self.setFixedWidth(640)
        self.setFixedHeight(480)

        self.lb_1.setText("Label 1")
        self.lb_2.setText("Label 2")
        self.lb_3.setText("Label 3")
        self.lb_4.setText("Label 4")
        self.lb_5.setText("Label 5")

        self.lb_1.setStyleSheet("background-color: yellow")
        self.lb_2.setStyleSheet("background-color: red")
        self.lb_3.setStyleSheet("background-color: blue")
        self.lb_4.setStyleSheet("background-color: pink")
        self.lb_5.setStyleSheet("background-color: grey")

        self.layout_2.addWidget(self.lb_1)
        self.layout_2.addWidget(self.lb_2)

        self.layout_3.addWidget(self.lb_3)
        self.layout_3.addWidget(self.lb_4)
        self.layout_3.addWidget(self.lb_5)

#GUI 보여주기
app = QApplication([])
dialog = layouts()
dialog.show()
app.exec_()