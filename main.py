import os, sys, serial

from PyQt4 import QtGui
from PyQt4 import QtCore

COMINDEX = 0

real_serial = serial.Serial(timeout=1)

class CanWindow(QtGui.QFrame):
    def __init__(self):
        super(QtGui.QFrame, self).__init__()
        self.vbox = QtGui.QVBoxLayout()
        self.comportbox = QtGui.QHBoxLayout()
        self.hbox = QtGui.QHBoxLayout()
        self.hbox2 = QtGui.QHBoxLayout()

        self.setWindowTitle("RS232 Pin Programmer")

        self.logo_label = QtGui.QLabel()
        self.logo_label.setAlignment(QtCore.Qt.AlignCenter)
        self.logo_label.setPixmap(QtGui.QPixmap(os.getcwd() + "/logo.png"))

        self.comboBox = QtGui.QComboBox()
        com_list = sniff_serial()
        for com in com_list:
            self.comboBox.addItem(com)
        self.comboBox.currentIndexChanged.connect(self.comboboxChanged)
        self.comport_button = QtGui.QPushButton("Connect")
        self.comport_button.clicked.connect(self.open_comport)

        self.pp1_button = QtGui.QPushButton("PP1")
        self.pp1_button.setCheckable(True)
        self.pp2_button = QtGui.QPushButton("PP2")
        self.pp2_button.setCheckable(True)
        self.pp3_button = QtGui.QPushButton("PP3")
        self.pp3_button.setCheckable(True)
        self.pp4_button = QtGui.QPushButton("PP4")
        self.pp4_button.setCheckable(True)
        self.pp5_button = QtGui.QPushButton("PP5")
        self.pp5_button.setCheckable(True)
        self.pp6_button = QtGui.QPushButton("PP6")
        self.pp6_button.setCheckable(True)
        self.pp7_button = QtGui.QPushButton("PP7")
        self.pp7_button.setCheckable(True)
        self.pp8_button = QtGui.QPushButton("PP8")
        self.pp8_button.setCheckable(True)
        self.pp9_button = QtGui.QPushButton("PP9")
        self.pp9_button.setCheckable(True)
        self.pp10_button = QtGui.QPushButton("PP10")
        self.pp10_button.setCheckable(True)
        self.pp11_button = QtGui.QPushButton("PP11")
        self.pp11_button.setCheckable(True)
        self.pp12_button = QtGui.QPushButton("PP12")
        self.pp12_button.setCheckable(True)
        self.pp13_button = QtGui.QPushButton("PP13")
        self.pp13_button.setCheckable(True)
        self.pp14_button = QtGui.QPushButton("PP14")
        self.pp14_button.setCheckable(True)
        self.pp15_button = QtGui.QPushButton("PP15")
        self.pp15_button.setCheckable(True)
        self.pp16_button = QtGui.QPushButton("PP16")
        self.pp16_button.setCheckable(True)
        self.pp17_button = QtGui.QPushButton("PP17")
        self.pp17_button.setCheckable(True)
        self.pp18_button = QtGui.QPushButton("PP18")
        self.pp18_button.setCheckable(True)
        self.pp19_button = QtGui.QPushButton("PP19")
        self.pp19_button.setCheckable(True)
        self.pp20_button = QtGui.QPushButton("PP20")
        self.pp20_button.setCheckable(True)

        self.pp1_button.clicked[bool].connect(self.set_pp)
        self.pp2_button.clicked[bool].connect(self.set_pp)
        self.pp3_button.clicked[bool].connect(self.set_pp)
        self.pp4_button.clicked[bool].connect(self.set_pp)
        self.pp5_button.clicked[bool].connect(self.set_pp)
        self.pp6_button.clicked[bool].connect(self.set_pp)
        self.pp7_button.clicked[bool].connect(self.set_pp)
        self.pp8_button.clicked[bool].connect(self.set_pp)
        self.pp9_button.clicked[bool].connect(self.set_pp)
        self.pp10_button.clicked[bool].connect(self.set_pp)
        self.pp11_button.clicked[bool].connect(self.set_pp)
        self.pp12_button.clicked[bool].connect(self.set_pp)
        self.pp13_button.clicked[bool].connect(self.set_pp)
        self.pp14_button.clicked[bool].connect(self.set_pp)
        self.pp15_button.clicked[bool].connect(self.set_pp)
        self.pp16_button.clicked[bool].connect(self.set_pp)
        self.pp17_button.clicked[bool].connect(self.set_pp)
        self.pp18_button.clicked[bool].connect(self.set_pp)
        self.pp19_button.clicked[bool].connect(self.set_pp)
        self.pp20_button.clicked[bool].connect(self.set_pp)

        self.comportbox.addWidget(self.comboBox)
        self.comportbox.addWidget(self.comport_button)

        self.hbox.addWidget(self.pp1_button)
        self.hbox.addWidget(self.pp2_button)
        self.hbox.addWidget(self.pp3_button)
        self.hbox.addWidget(self.pp4_button)
        self.hbox.addWidget(self.pp5_button)
        self.hbox.addWidget(self.pp6_button)
        self.hbox.addWidget(self.pp7_button)
        self.hbox.addWidget(self.pp8_button)
        self.hbox.addWidget(self.pp9_button)
        self.hbox.addWidget(self.pp10_button)
        self.hbox2.addWidget(self.pp11_button)
        self.hbox2.addWidget(self.pp12_button)
        self.hbox2.addWidget(self.pp13_button)
        self.hbox2.addWidget(self.pp14_button)
        self.hbox2.addWidget(self.pp15_button)
        self.hbox2.addWidget(self.pp16_button)
        self.hbox2.addWidget(self.pp17_button)
        self.hbox2.addWidget(self.pp18_button)
        self.hbox2.addWidget(self.pp19_button)
        self.hbox2.addWidget(self.pp20_button)

        self.vbox.addWidget(self.logo_label)
        self.vbox.addLayout(self.hbox)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.comportbox)

        self.setLayout(self.vbox)

    def set_pp(self, pressed):
        source = self.sender()

        if pressed:
            if source.text() == "PP1":
                send_msg('A')
                print("PP1 TOGGLED ON")
                ## msg = "PP1 Pressed: Serial 'A'"
                ## print(msg)
            if source.text() == "PP2":
                send_msg('B')
                print("PP2 TOGGLED ON")
                ## msg = "PP2 Pressed: Serial 'B'"
                ## print(msg)
            if source.text() == "PP3":
                send_msg('C')
                print("PP3 TOGGLED ON")
                ## msg = "PP3 Pressed: Serial 'C'"
                ## print(msg)
            if source.text() == "PP4":
                send_msg('D')
                print("PP4 TOGGLED ON")
                ## msg = "PP4 Pressed: Serial 'D'"
                ## print(msg)
            if source.text() == "PP5":
                send_msg('E')
                print("PP5 TOGGLED ON")
                ## msg = "PP5 Pressed: Serial 'E'"
                ## print(msg)
            if source.text() == "PP6":
                send_msg('F')
                print("PP6 TOGGLED ON")
                ## msg = "PP6 Pressed: Serial 'F'"
                ## print(msg)
            if source.text() == "PP7":
                send_msg('G')
                print("PP7 TOGGLED ON")
                ## msg = "PP7 Pressed: Serial 'G'"
                ## print(msg)
            if source.text() == "PP8":
                send_msg('H')
                print("PP8 TOGGLED ON")
                ## msg = "PP8 Pressed: Serial 'H'"
                ## print(msg)
            if source.text() == "PP9":
                send_msg('I')
                print("PP9 TOGGLED ON")
                ## msg = "PP9 Pressed: Serial 'I'"
                ## print(msg)
            if source.text() == "PP10":
                send_msg('J')
                print("PP10 TOGGLED ON")
                ## msg = "PP10 Pressed: Serial 'J'"
                ## print(msg)
            if source.text() == "PP11":
                send_msg('K')
                print("PP11 TOGGLED ON")
                ## msg = "PP11 Pressed: Serial 'K'"
                ## print(msg)
            if source.text() == "PP12":
                send_msg('L')
                print("PP12 TOGGLED ON")
                ## msg = "PP12 Pressed: Serial 'L'"
                ## print(msg)
            if source.text() == "PP13":
                send_msg('M')
                print("PP13 TOGGLED ON")
                ## msg = "PP13 Pressed: Serial 'M'"
                ## print(msg)
            if source.text() == "PP14":
                send_msg('N')
                print("PP14 TOGGLED ON")
                ## msg = "PP14 Pressed: Serial 'N'"
                ## print(msg)
            if source.text() == "PP15":
                send_msg('O')
                print("PP15 TOGGLED ON")
                ## msg = "PP15 Pressed: Serial 'O'"
                ## print(msg)
            if source.text() == "PP16":
                send_msg('P')
                print("PP16 TOGGLED ON")
                ## msg = "PP16 Pressed: Serial 'P'"
                ## print(msg)
            if source.text() == "PP17":
                send_msg('Q')
                print("PP17 TOGGLED ON")
                ## msg = "PP17 Pressed: Serial 'Q'"
                ## print(msg)
            if source.text() == "PP18":
                send_msg('R')
                print("PP18 TOGGLED ON")
                ## msg = "PP18 Pressed: Serial 'R'"
                ## print(msg)
            if source.text() == "PP19":
                send_msg('S')
                print("PP19 TOGGLED ON")
                ## msg = "PP19 Pressed: Serial 'S'"
                ## print(msg)
            if source.text() == "PP20":
                send_msg('T')
                print("PP20 TOGGLED ON")
                ## msg = "PP20 Pressed: Serial 'T'"
                ## print(msg)
        else:
            if source.text() == "PP1":
                send_msg('a')
                print("PP1 TOGGLED OFF")
                ## msg = "PP1 De-pressed: Serial 'a'"
                ## print(msg)
            if source.text() == "PP2":
                send_msg('b')
                print("PP2 TOGGLED OFF")
                ## msg = "PP2 De-pressed: Serial 'b'"
                ## print(msg)
            if source.text() == "PP3":
                send_msg('c')
                print("PP3 TOGGLED OFF")
                ## msg = "PP3 De-pressed: Serial 'c'"
                ## print(msg)
            if source.text() == "PP4":
                send_msg('d')
                print("PP4 TOGGLED OFF")
                ## msg = "PP4 De-pressed: Serial 'd'"
                ## print(msg)
            if source.text() == "PP5":
                send_msg('e')
                print("PP5 TOGGLED OFF")
                ## msg = "PP5 De-pressed: Serial 'e'"
                ## print(msg)
            if source.text() == "PP6":
                send_msg('f')
                print("PP6 TOGGLED OFF")
                ## msg = "PP6 De-pressed: Serial 'f'"
                ## print(msg)
            if source.text() == "PP7":
                send_msg('g')
                print("PP7 TOGGLED OFF")
                ## msg = "PP7 De-pressed: Serial 'g'"
                ## print(msg)
            if source.text() == "PP8":
                send_msg('h')
                print("PP8 TOGGLED OFF")
                ## msg = "PP8 De-pressed: Serial 'h'"
                ## print(msg)
            if source.text() == "PP9":
                send_msg('i')
                print("PP9 TOGGLED OFF")
                ## msg = "PP9 De-pressed: Serial 'i'"
                ## print(msg)
            if source.text() == "PP10":
                send_msg('j')
                print("PP10 TOGGLED OFF")
                ## msg = "PP10 De-pressed: Serial 'j'"
                ## print(msg)
            if source.text() == "PP11":
                send_msg('k')
                print("PP11 TOGGLED OFF")
                ## msg = "PP11 De-pressed: Serial 'k'"
                ## print(msg)
            if source.text() == "PP12":
                send_msg('l')
                print("PP12 TOGGLED OFF")
                ## msg = "PP12 De-pressed: Serial 'l'"
                ## print(msg)
            if source.text() == "PP13":
                send_msg('m')
                print("PP13 TOGGLED OFF")
                ## msg = "PP13 De-pressed: Serial 'm'"
                ## print(msg)
            if source.text() == "PP14":
                send_msg('n')
                print("PP14 TOGGLED OFF")
                ## msg = "PP14 De-pressed: Serial 'n'"
                ## print(msg)
            if source.text() == "PP15":
                send_msg('o')
                print("PP15 TOGGLED OFF")
                ## msg = "PP15 De-pressed: Serial 'o'"
                ## print(msg)
            if source.text() == "PP16":
                send_msg('p')
                print("PP16 TOGGLED OFF")
                ## msg = "PP16 De-pressed: Serial 'p'"
                ## print(msg)
            if source.text() == "PP17":
                send_msg('q')
                print("PP17 TOGGLED OFF")
                ## msg = "PP17 De-pressed: Serial 'q'"
                ## print(msg)
            if source.text() == "PP18":
                send_msg('r')
                print("PP18 TOGGLED OFF")
                ## msg = "PP18 De-pressed: Serial 'r'"
                ## print(msg)
            if source.text() == "PP19":
                send_msg('s')
                print("PP19 TOGGLED OFF")
                ## msg = "PP19 De-pressed: Serial 's'"
                ## print(msg)
            if source.text() == "PP20":
                send_msg('t')
                print("PP20 TOGGLED OFF")
                ## msg = "PP20 De-pressed: Serial 't'"
                ## print(msg)

    def comboboxChanged(self, com_port):
        global COMINDEX
        COMINDEX = com_port

    def open_comport(self):
        global COMINDEX
        com_list = sniff_serial()
        real_serial.baudrate = 9600
        try:
            real_serial.setPort(com_list[COMINDEX])
            if real_serial.is_open:
                real_serial.close()
            real_serial.open()
            print("COM Initialized. Opened on " + com_list[COMINDEX])
        except IndexError:
            print("No valid COM port selected.")


def send_msg(input):
    try:
        real_serial.write(input.encode('ascii'))
    except serial.SerialException:
        print("PEBCAK: 'Connect' a valid COM port.")

def sniff_serial():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    else:
        raise EnvironmentError("Unsupported OS platform")

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    w = CanWindow()
    w.show()
    sys.exit(app.exec_())