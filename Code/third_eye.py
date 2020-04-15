"""
Project = Third Eye : Surveillance System 
Developer = Vikas Patel 
  

"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl, QPointF
from PyQt5.QtGui import QDesktopServices, QColor
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
import surveillanceTest as surv
from Databases.database import SettingsDatabase


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        self.s = None
        self.shadow = QGraphicsDropShadowEffect(blurRadius=18, offset=QPointF(0.0, 0.0),color=QColor("#009dff"))
        self.btnShadow1 = QGraphicsDropShadowEffect(blurRadius=20, offset=QPointF(0.0, 0.0),color=QColor("#e5ff00"))
        self.btnShadow2 = QGraphicsDropShadowEffect(blurRadius=20, offset=QPointF(0.0, 0.0),color=QColor("#077a05"))
        self.btnShadow3 = QGraphicsDropShadowEffect(blurRadius=20, offset=QPointF(0.0, 0.0),color=QColor("#ff1500"))
        # Setting Database
        self.sdb = SettingsDatabase()
        # Thresh Hold value
        self.thresh = self.sdb.get_sensitivity()
        # admin password
        self.passwd = self.sdb.get_password()
        # camera ip
        self.camera_ip = 0

        # Style Sheet
        self.style_sheet = """
            QPushButton{
                border: 1px solid #009dff;
                border-radius :1px 5px 5px 1px;
                background-color:#ffffff;
            }
            QPushButton:hover{
                background-color:#009dff;
                border-radius :15px;
                color: #ffffff;
                font-weight: 200;
                border-color: transparent;
            }
            QPushButton#btn_alarm,QPushButton#btn_start_system,QPushButton#bnt_stop_system{
                border-radius :10px 15px 15px 10px;
            }
            QPushButton#btn_alarm:hover,QPushButton#btn_start_system:hover,QPushButton#bnt_stop_system:hover{
                border-color:transparent;
                border-radius :20px 20px 50px 50px;
            }
            QPushButton#btn_alarm{
                border: 1px solid #e5ff00;
            }
            QPushButton#btn_start_system{
                border: 1px solid #3dfc03;
            }
            QPushButton#bnt_stop_system{
                border: 1px solid #fc7844;
            }
            QPushButton#btn_github:hover{
                background-color:#000000;
                color:#ffffff;
            }
            QPushButton#btn_apppage:hover{
                background-color:#6d1bfa;
                color:#ffffff;
            }
            QPushButton#btn_blog:hover{
                background-color:#fa691b;
                color:#ffffff;
            }

            QLineEdit{
                border: 1px solid #009dff;
                border-radius: 10px;
            }
            #toolBox{
                background-color : #d4eeff;
                border: 1px solid #032473;
            }
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setMinimumSize(QtCore.QSize(640, 480))
        MainWindow.setMaximumSize(QtCore.QSize(640, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Assets/PNGs/camera.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(True)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        MainWindow.setGraphicsEffect(self.shadow)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tab_group = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_group.setGeometry(QtCore.QRect(10, 0, 621, 431))
        self.tab_group.setObjectName("tab_group")
        self.tab_group.setGraphicsEffect(self.shadow)
        self.shadow.setEnabled(True)
        self.tab_home = QtWidgets.QWidget()
        self.tab_home.setObjectName("tab_home")
        self.frame_home = QtWidgets.QFrame(self.tab_home)
        self.frame_home.setGeometry(QtCore.QRect(-10, -10, 631, 411))
        self.frame_home.setStyleSheet("")
        self.frame_home.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_home.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_home.setObjectName("frame_home")
        self.btn_alarm = QtWidgets.QPushButton(self.frame_home)
        self.btn_alarm.setGeometry(QtCore.QRect(440, 180, 161, 41))
        self.btn_alarm.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_alarm.setAutoFillBackground(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/PICTURES/PNGs/Icon-material-access-alarm.png"),  QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_alarm.setIcon(icon1)
        self.btn_alarm.setIconSize(QtCore.QSize(32, 32))
        self.btn_alarm.setAutoRepeat(False)
        self.btn_alarm.setAutoDefault(False)
        self.btn_alarm.setDefault(False)
        self.btn_alarm.setFlat(False)
        self.btn_alarm.setObjectName("btn_alarm")
        self.btn_alarm.setGraphicsEffect(self.btnShadow1)
        self.btn_start_system = QtWidgets.QPushButton(self.frame_home)
        self.btn_start_system.setGeometry(QtCore.QRect(440, 240, 161, 41))
        self.btn_start_system.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_start_system.setAutoFillBackground(False)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/home/32x32/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_start_system.setIcon(icon2)
        self.btn_start_system.setIconSize(QtCore.QSize(48, 48))
        self.btn_start_system.setAutoRepeat(False)
        self.btn_start_system.setAutoDefault(False)
        self.btn_start_system.setDefault(False)
        self.btn_start_system.setFlat(False)
        self.btn_start_system.setObjectName("btn_start_system")
        self.btn_start_system.setGraphicsEffect(self.btnShadow2)
        self.home_picture = QtWidgets.QLabel(self.frame_home)
        self.home_picture.setGeometry(QtCore.QRect(20, 40, 371, 321))
        self.home_picture.setText("")
        self.home_picture.setPixmap(QtGui.QPixmap(":/PICTURES/PNGs/Group 9.png"))
        self.home_picture.setScaledContents(True)
        self.home_picture.setObjectName("home_picture")
        self.bnt_stop_system = QtWidgets.QPushButton(self.frame_home)
        self.bnt_stop_system.setGeometry(QtCore.QRect(440, 300, 161, 41))
        self.bnt_stop_system.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bnt_stop_system.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bnt_stop_system.setAutoFillBackground(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/All/32x32/busy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bnt_stop_system.setIcon(icon3)
        self.bnt_stop_system.setIconSize(QtCore.QSize(48, 48))
        self.bnt_stop_system.setAutoRepeat(False)
        self.bnt_stop_system.setAutoDefault(False)
        self.bnt_stop_system.setDefault(False)
        self.bnt_stop_system.setFlat(False)
        self.bnt_stop_system.setObjectName("bnt_stop_system")
        self.bnt_stop_system.setGraphicsEffect(self.btnShadow3)
        self.logo = QtWidgets.QLabel(self.frame_home)
        self.logo.setGeometry(QtCore.QRect(370, 40, 251, 91))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(":/PICTURES/PNGs/logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/home/32x32/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab_group.addTab(self.tab_home, icon4, "")
        self.tab_settings = QtWidgets.QWidget()
        self.tab_settings.setObjectName("tab_settings")
        self.frame_settings = QtWidgets.QFrame(self.tab_settings)
        self.frame_settings.setGeometry(QtCore.QRect(10, -10, 631, 411))
        self.frame_settings.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_settings.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_settings.setObjectName("frame_settings")
        self.toolBox = QtWidgets.QToolBox(self.frame_settings)
        self.toolBox.setGeometry(QtCore.QRect(20, 40, 411, 311))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.toolBox.setFont(font)
        self.toolBox.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 411, 212))
        self.page.setObjectName("page")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 141, 31))
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setObjectName("label_2")
        self.ip_input = QtWidgets.QLineEdit(self.page)
        self.ip_input.setGeometry(QtCore.QRect(170, 20, 231, 31))
        self.ip_input.setObjectName("ip_input")
        self.label_4 = QtWidgets.QLabel(self.page)
        self.label_4.setGeometry(QtCore.QRect(20, 120, 141, 31))
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setObjectName("label_4")
        self.layoutWidget = QtWidgets.QWidget(self.page)
        self.layoutWidget.setGeometry(QtCore.QRect(170, 120, 231, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.threshOP_low = QtWidgets.QLabel(self.layoutWidget)
        self.threshOP_low.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        self.threshOP_low.setFont(font)
        self.threshOP_low.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.threshOP_low.setAlignment(QtCore.Qt.AlignCenter)
        self.threshOP_low.setObjectName("threshOP_low")
        self.horizontalLayout_3.addWidget(self.threshOP_low)
        self.threshIN = QtWidgets.QSlider(self.layoutWidget)
        self.threshIN.setMouseTracking(False)
        self.threshIN.setMinimum(1)
        self.threshIN.setMaximum(500)
        self.threshIN.setOrientation(QtCore.Qt.Horizontal)
        self.threshIN.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.threshIN.setObjectName("threshIN")
        self.threshIN.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.threshIN)
        self.threshOP_high = QtWidgets.QLabel(self.layoutWidget)
        self.threshOP_high.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        self.threshOP_high.setFont(font)
        self.threshOP_high.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.threshOP_high.setAlignment(QtCore.Qt.AlignCenter)
        self.threshOP_high.setObjectName("threshOP_high")
        self.horizontalLayout_3.addWidget(self.threshOP_high)
        self.threshOP = QtWidgets.QLabel(self.layoutWidget)
        self.threshOP.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        self.threshOP.setFont(font)
        self.threshOP.setFrameShape(QtWidgets.QFrame.Panel)
        self.threshOP.setFrameShadow(QtWidgets.QFrame.Raised)
        self.threshOP.setAlignment(QtCore.Qt.AlignCenter)
        self.threshOP.setObjectName("threshOP")
        self.horizontalLayout_3.addWidget(self.threshOP)
        self.btn_reset_thresh = QtWidgets.QPushButton(self.page)
        self.btn_reset_thresh.setGeometry(QtCore.QRect(240, 160, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_reset_thresh.setFont(font)
        self.btn_reset_thresh.setObjectName("btn_reset_thresh")
        self.btn_reset_thresh.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.btn_ip = QtWidgets.QPushButton(self.page)
        self.btn_ip.setGeometry(QtCore.QRect(240, 60, 111, 31))
        self.btn_ip.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_ip.setFont(font)
        self.btn_ip.setObjectName("btn_ip")
        self.line = QtWidgets.QFrame(self.page)
        self.line.setGeometry(QtCore.QRect(10, 100, 391, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.page)
        self.line_2.setGeometry(QtCore.QRect(0, 200, 411, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/PICTURES/PNGs/camera-vector.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.page, icon5, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 411, 212))
        self.page_2.setObjectName("page_2")
        self.label_3 = QtWidgets.QLabel(self.page_2)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 141, 31))
        self.label_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_3.setObjectName("label_3")
        self.mobile_in = QtWidgets.QLineEdit(self.page_2)
        self.mobile_in.setGeometry(QtCore.QRect(170, 10, 231, 31))
        self.mobile_in.setObjectName("mobile_in")
        self.label_5 = QtWidgets.QLabel(self.page_2)
        self.label_5.setGeometry(QtCore.QRect(20, 60, 141, 31))
        self.label_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_5.setObjectName("label_5")
        self.msg_in = QtWidgets.QLineEdit(self.page_2)
        self.msg_in.setGeometry(QtCore.QRect(170, 60, 231, 31))
        self.msg_in.setObjectName("msg_in")
        self.label_6 = QtWidgets.QLabel(self.page_2)
        self.label_6.setGeometry(QtCore.QRect(20, 110, 141, 31))
        self.label_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_6.setObjectName("label_6")
        self.email_in = QtWidgets.QLineEdit(self.page_2)
        self.email_in.setGeometry(QtCore.QRect(170, 110, 231, 31))
        self.email_in.setObjectName("email_in")
        self.line_3 = QtWidgets.QFrame(self.page_2)
        self.line_3.setGeometry(QtCore.QRect(0, 200, 411, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/All/32x32/future-projects.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.page_2, icon6, "")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_7 = QtWidgets.QLabel(self.page_3)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 141, 31))
        self.label_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_7.setObjectName("label_7")
        self.pass_in = QtWidgets.QLineEdit(self.page_3)
        self.pass_in.setGeometry(QtCore.QRect(160, 10, 231, 31))
        self.pass_in.setObjectName("pass_in")
        self.line_4 = QtWidgets.QFrame(self.page_3)
        self.line_4.setGeometry(QtCore.QRect(0, 170, 411, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/All/32x32/lock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.page_3, icon7, "")
        self.btn_setting_save = QtWidgets.QPushButton(self.frame_settings)
        self.btn_setting_save.setGeometry(QtCore.QRect(450, 270, 141, 51))

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_setting_save.setFont(font)
        self.btn_setting_save.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/All/32x32/check.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_setting_save.setIcon(icon8)
        self.btn_setting_save.setObjectName("btn_setting_save")
        self.btn_settings_reset = QtWidgets.QPushButton(self.frame_settings)
        self.btn_settings_reset.setGeometry(QtCore.QRect(450, 200, 141, 51))

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_settings_reset.setFont(font)
        self.btn_settings_reset.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_settings_reset.setObjectName("btn_settings_reset")
        self.label_8 = QtWidgets.QLabel(self.frame_settings)
        self.label_8.setGeometry(QtCore.QRect(30, 370, 551, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame_settings)
        self.label_9.setGeometry(QtCore.QRect(450, 60, 151, 91))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(":/PICTURES/PNGs/Group 10.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/settings/32x32/config.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab_group.addTab(self.tab_settings, icon9, "")
        self.tab_about = QtWidgets.QWidget()
        self.tab_about.setObjectName("tab_about")
        self.frame_about = QtWidgets.QFrame(self.tab_about)
        self.frame_about.setGeometry(QtCore.QRect(-10, -10, 631, 421))
        self.frame_about.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_about.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_about.setObjectName("frame_about")
        self.btn_github = QtWidgets.QPushButton(self.frame_about)
        self.btn_github.setGeometry(QtCore.QRect(420, 300, 81, 31))
        self.btn_github.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_github.setFont(font)
        self.btn_github.setObjectName("btn_github")
        self.label = QtWidgets.QLabel(self.frame_about)
        self.label.setGeometry(QtCore.QRect(400, 20, 211, 211))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/PICTURES/Pictures/vikas_icon.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.frame_about)
        self.textEdit.setGeometry(QtCore.QRect(20, 20, 371, 271))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame_about)
        self.textBrowser.setGeometry(QtCore.QRect(80, 240, 256, 71))
        self.textBrowser.setObjectName("textBrowser")
        self.btn_twitter = QtWidgets.QPushButton(self.frame_about)
        self.btn_twitter.setGeometry(QtCore.QRect(516, 300, 81, 31))
        self.btn_twitter.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_twitter.setFont(font)
        self.btn_twitter.setObjectName("btn_twitter")
        self.btn_blog = QtWidgets.QPushButton(self.frame_about)
        self.btn_blog.setGeometry(QtCore.QRect(420, 262, 81, 31))
        self.btn_blog.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_blog.setFont(font)
        self.btn_blog.setObjectName("btn_blog")
        self.btn_apppage = QtWidgets.QPushButton(self.frame_about)
        self.btn_apppage.setGeometry(QtCore.QRect(516, 262, 81, 31))
        self.btn_apppage.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_apppage.setFont(font)
        self.btn_apppage.setObjectName("btn_apppage")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/about-person/32x32/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab_group.addTab(self.tab_about, icon10, "")
        self.tab_contact = QtWidgets.QWidget()
        self.tab_contact.setObjectName("tab_contact")
        self.frame_contact = QtWidgets.QFrame(self.tab_contact)
        self.frame_contact.setGeometry(QtCore.QRect(-10, -10, 631, 421))
        self.frame_contact.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_contact.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_contact.setObjectName("frame_contact")
        self.groupBox = QtWidgets.QGroupBox(self.frame_contact)
        self.groupBox.setGeometry(QtCore.QRect(30, 30, 571, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox)
        self.plainTextEdit.setGeometry(QtCore.QRect(60, 30, 261, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.btn_email = QtWidgets.QPushButton(self.groupBox)
        self.btn_email.setGeometry(QtCore.QRect(380, 30, 131, 31))
        self.btn_email.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_email.setFont(font)
        self.btn_email.setObjectName("btn_email")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame_contact)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 110, 571, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(60, 30, 261, 31))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.btn_website = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_website.setGeometry(QtCore.QRect(380, 30, 131, 31))
        self.btn_website.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_website.setFont(font)
        self.btn_website.setObjectName("btn_website")
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame_contact)
        self.groupBox_3.setGeometry(QtCore.QRect(30, 190, 571, 161))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.groupBox_3)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(60, 30, 261, 31))
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.btn_twitter_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_twitter_2.setGeometry(QtCore.QRect(380, 30, 131, 31))
        self.btn_twitter_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_twitter_2.setFont(font)
        self.btn_twitter_2.setObjectName("btn_twitter_2")
        self.plainTextEdit_4 = QtWidgets.QPlainTextEdit(self.groupBox_3)
        self.plainTextEdit_4.setGeometry(QtCore.QRect(60, 70, 261, 31))
        self.plainTextEdit_4.setObjectName("plainTextEdit_4")
        self.btn_github_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_github_2.setGeometry(QtCore.QRect(380, 70, 131, 31))
        self.btn_github_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_github_2.setFont(font)
        self.btn_github_2.setObjectName("btn_github_2")
        self.btn_instamojo = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_instamojo.setGeometry(QtCore.QRect(380, 110, 131, 31))
        self.btn_instamojo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_instamojo.setFont(font)
        self.btn_instamojo.setObjectName("btn_instamojo")
        self.plainTextEdit_5 = QtWidgets.QPlainTextEdit(self.groupBox_3)
        self.plainTextEdit_5.setGeometry(QtCore.QRect(60, 110, 261, 31))
        self.plainTextEdit_5.setObjectName("plainTextEdit_5")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/home/32x32/contact.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab_group.addTab(self.tab_contact, icon11, "")
        self.tab_donate = QtWidgets.QWidget()
        self.tab_donate.setObjectName("tab_donate")
        self.frame_donate = QtWidgets.QFrame(self.tab_donate)
        self.frame_donate.setGeometry(QtCore.QRect(-10, -10, 631, 421))
        self.frame_donate.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_donate.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_donate.setObjectName("frame_donate")
        self.groupBox_4 = QtWidgets.QGroupBox(self.frame_donate)
        self.groupBox_4.setGeometry(QtCore.QRect(30, 40, 571, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.plainTextEdit_6 = QtWidgets.QPlainTextEdit(self.groupBox_4)
        self.plainTextEdit_6.setGeometry(QtCore.QRect(60, 30, 261, 31))
        self.plainTextEdit_6.setObjectName("plainTextEdit_6")
        self.btn_paypal = QtWidgets.QPushButton(self.groupBox_4)
        self.btn_paypal.setGeometry(QtCore.QRect(380, 30, 131, 31))
        self.btn_paypal.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_paypal.setFont(font)
        self.btn_paypal.setObjectName("btn_paypal")
        self.groupBox_5 = QtWidgets.QGroupBox(self.frame_donate)
        self.groupBox_5.setGeometry(QtCore.QRect(30, 130, 571, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.plainTextEdit_7 = QtWidgets.QPlainTextEdit(self.groupBox_5)
        self.plainTextEdit_7.setGeometry(QtCore.QRect(60, 30, 261, 31))
        self.plainTextEdit_7.setObjectName("plainTextEdit_7")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/home/32x32/donate.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab_group.addTab(self.tab_donate, icon12, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        MainWindow.setStyleSheet(self.style_sheet)
        self.statusBar.showMessage('Services Started | Click Start System to Start the Serveillance System')

        """ bind buttons with actions """
        #########################################################

        self.threshIN.setValue(int(self.thresh))
        self.threshOP.setText(self.thresh)

        self.btn_blog.clicked.connect(self.openBlog)
        self.btn_website.clicked.connect(self.openBlog)
        self.btn_apppage.clicked.connect(self.openAppPage)
        self.btn_twitter.clicked.connect(self.openTwitter)
        self.btn_twitter_2.clicked.connect(self.openTwitter)
        self.btn_github.clicked.connect(self.openGithub)
        self.btn_github_2.clicked.connect(self.openGithub)
        self.btn_instamojo.clicked.connect(self.openInstamojo)
        self.btn_paypal.clicked.connect(self.openPaypal)
        self.btn_email.clicked.connect(self.sendEmail)


        self.btn_start_system.clicked.connect(self.startSystem) # start system
        self.bnt_stop_system.clicked.connect(self.stopSystem) # stop system
        self.btn_alarm.clicked.connect(self.startAlarm) # start alarm

        self.btn_ip.clicked.connect(self.saveCameraIP) # connect
        self.btn_reset_thresh.clicked.connect(self.resetThresh) # resetThresh
        self.btn_settings_reset.clicked.connect(self.cancelIt) # cancel
        self.btn_setting_save.clicked.connect(self.saveSettings) # save Settings
        self.threshIN.valueChanged.connect(self.getThresh) # Sensitivity slider
        self.btn_alarm.setEnabled(False)
        self.bnt_stop_system.setEnabled(False)




        #########################################################

        self.retranslateUi(MainWindow)
        self.tab_group.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(0)
        self.threshIN.valueChanged['int'].connect(self.threshOP.setNum)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
#########################################################

    def openBlog(self):
        docDir = "www.villageprogrammer.blogspot.com/"
        QDesktopServices.openUrl(QUrl(docDir))

    def openAppPage(self):
        docDir = "www.villageprogrammer.blogspot.com/"
        QDesktopServices.openUrl(QUrl(docDir))

    def openGithub(self):
        docDir = "https://www.github.com/vikaspatelp83"
        QDesktopServices.openUrl(QUrl(docDir))

    def openTwitter(self):
        docDir = "https://www.twitter.com/devdp430"
        QDesktopServices.openUrl(QUrl(docDir))

    def openInstamojo(self):
        docDir = "https://www.instamojo.com/villageprogrammer"
        QDesktopServices.openUrl(QUrl(docDir))

    def openPaypal(self):
        docDir = "https://www.paypal.me/vikaspatelp83"
        QDesktopServices.openUrl(QUrl(docDir))

    def sendEmail(self):
        docDir = 'mailto:vikaspatelp83@gmail.com?Subject=Hello%20from%20third%20eye!'
        QDesktopServices.openUrl(QUrl(docDir))


#******************
    def saveCameraIP(self):
        ip = self.ip_input.text()
        if ip!="" or ip!="":
            self.camera_ip = ip
        else:
            self.camera_ip = 0
        print(self.camera_ip)
        self.statusBar.showMessage("📽 Video Feed Address Saved : "+str(self.camera_ip))



        """ Will implement later"""

    def saveSettings(self):
        password = self.pass_in.text()
        thresh = self.thresh
        mob = self.mobile_in.text()
        email = self.email_in.text()
        msg = self.msg_in.text()
        print(email)
        if not thresh=="" and not mob=="" and not email=="" and not msg=="":
            if password == self.passwd:
                self.sdb.set_sensitivity(thresh)
                self.sdb.set_mobile(mob)
                self.sdb.set_email(email)
                self.sdb.set_message(msg)
                print("Saving settings")
                self.statusBar.showMessage("💾 Settings Saved")
            else:
                self.statusBar.showMessage("❌❌❌❌❌Wrong Password")
        elif not thresh=="" and mob=="" and email=="" and msg=="":
            if password == self.passwd:
                self.sdb.set_sensitivity(thresh)
                print("Sensitivity Updated")
                self.statusBar.showMessage("💾 Sensitivity Updated")
            else:
                self.statusBar.showMessage("❌❌❌❌❌ Wrong Password")
        else:
            self.statusBar.showMessage("Empty Imput Field. Please fill the correct info.")
        
        print(self.sdb.getAll())

    def getThresh(self,value):
        self.thresh = value
        print(self.thresh)

    def resetThresh(self):
        print(self.thresh)
        self.sdb.set_sensitivity(20)
        self.statusBar.showMessage("Sensitivity Set to Default")



    def cancelIt(self):
        pass

    """
    Main Actions
    """

    def startAlarm(self):
        surv.start_alarm(self.s)
        print("Alarm Started")
        self.statusBar.showMessage("✅ Alarm Started")


    def startSystem(self):
        self.s = surv.start_system(self.camera_ip)
        self.btn_alarm.setEnabled(True)
        self.bnt_stop_system.setEnabled(True)
        self.btn_start_system.setEnabled(False)
        print("System started")
        self.statusBar.showMessage("😀 System Started")

    def stopSystem(self):
        surv.stop_system(self.s)
        self.btn_start_system.setEnabled(True)
        self.btn_alarm.setEnabled(False)
        self.bnt_stop_system.setEnabled(False)
        print("system stopped")
        self.statusBar.showMessage("❌ System Stopped")




#########################################################


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Third Eye : Surveillance System"))
        self.btn_alarm.setText(_translate("MainWindow", "    START ALARM"))
        self.btn_start_system.setText(_translate("MainWindow", "     START SYSTEM"))
        self.bnt_stop_system.setText(_translate("MainWindow", "      STOP SYSTEM"))
        self.tab_group.setTabText(self.tab_group.indexOf(self.tab_home), _translate("MainWindow", "Home"))
        self.label_2.setText(_translate("MainWindow", "IP Address"))
        self.label_4.setText(_translate("MainWindow", "Sensitivity"))
        self.threshOP_low.setText(_translate("MainWindow", "0"))
        self.threshOP_high.setText(_translate("MainWindow", "500"))
        self.threshOP.setText(_translate("MainWindow", str(self.thresh)))
        self.btn_reset_thresh.setText(_translate("MainWindow", "Reset Sensitivity"))
        self.btn_ip.setText(_translate("MainWindow", "Connect"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "Camera Settings"))
        self.label_3.setText(_translate("MainWindow", "Mobile Number"))
        self.label_5.setText(_translate("MainWindow", "Alert Message"))
        self.label_6.setText(_translate("MainWindow", "Alert Email"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "Alert Settings"))
        self.label_7.setText(_translate("MainWindow", "Password"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("MainWindow", "Admin Password"))
        self.btn_setting_save.setText(_translate("MainWindow", "Save Settings"))
        self.btn_settings_reset.setText(_translate("MainWindow", "Cancel"))
        self.label_8.setText(_translate("MainWindow", "Enter your admin password and click \"Save Settings\" to save new settings."))
        self.tab_group.setTabText(self.tab_group.indexOf(self.tab_settings), _translate("MainWindow", "Settings"))
        self.btn_github.setText(_translate("MainWindow", "GitHub"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Third Eye</span> is a Surveillance System. Capable of detecting motion and will alert you in case of security breach using SMS, Email and Alarm System.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Third Eye is developed by <a href=\"https://www.github.com/vikaspatelp83\"><span style=\" font-weight:600; text-decoration: underline; color:#0000ff;\">Vikas Patel </span></a>at DTech Software aka Villageprogrammer.</p></body></html>"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">Open Source Software</span></p></body></html>"))
        self.btn_twitter.setText(_translate("MainWindow", "Twitter"))
        self.btn_blog.setText(_translate("MainWindow", "Blog"))
        self.btn_apppage.setText(_translate("MainWindow", "App Page"))
        self.tab_group.setTabText(self.tab_group.indexOf(self.tab_about), _translate("MainWindow", "About"))
        self.groupBox.setTitle(_translate("MainWindow", "Email Me"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "vikaspatelp83@gmail.com"))
        self.btn_email.setText(_translate("MainWindow", "Send Email"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Website"))
        self.plainTextEdit_2.setPlainText(_translate("MainWindow", "www.villageprogrammer.tech"))
        self.btn_website.setText(_translate("MainWindow", "Open in Browser"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Follow Me"))
        self.plainTextEdit_3.setPlainText(_translate("MainWindow", "Twitter"))
        self.btn_twitter_2.setText(_translate("MainWindow", "Open in Browser"))
        self.plainTextEdit_4.setPlainText(_translate("MainWindow", "GitHub"))
        self.btn_github_2.setText(_translate("MainWindow", "Open in Browser"))
        self.btn_instamojo.setText(_translate("MainWindow", "Open in Browser"))
        self.plainTextEdit_5.setPlainText(_translate("MainWindow", "Buy Books at Instamojo"))
        self.tab_group.setTabText(self.tab_group.indexOf(self.tab_contact), _translate("MainWindow", "Contact"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Paypal"))
        self.plainTextEdit_6.setPlainText(_translate("MainWindow", "www.paypal.me/vikaspatelp83"))
        self.btn_paypal.setText(_translate("MainWindow", "Open Paypal"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Paytm/Google Pay"))
        self.plainTextEdit_7.setPlainText(_translate("MainWindow", "9575357966"))
        self.tab_group.setTabText(self.tab_group.indexOf(self.tab_donate), _translate("MainWindow", "Donate"))

# import Image Resources
import resource_icons


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
