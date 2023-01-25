from PyQt5 import QtCore, QtGui, QtWidgets
import random
import pymongo
        
LNames = ['აბაშიძე', 'გიგაური', 'არჩვაძე', 'ახალაია', 'ბაძაღუა', 'ბერიანიძე', 'ბერიშვილი', 'გვენცაძე', 'დალაქიშვილი',
          'ანთიძე', 'გიორგაძე', 'გოგალაძე', 'გოცირიძე', 'ვარდიძე', 'ზარანდია', 'თადუმაძე', 'ლაბაძე', 'კვარაცხელია',
          'კუსრაძე', 'კვესელავა', 'კაპანაძე', 'კასრაძე', 'კვინიკაძე', 'კოპაძე', 'კანკია', 'კორძაია', 'მიქავა', 'მელია',
          'მონიავა', 'ნიაური', 'ლაცაბიძე', 'მიქაძე', 'ნემსიწვერიძე', 'მაისურაძე', 'მაცაბერიძე', 'მჟავია', 'მაჩალაძე',
          'ოდიშარია', 'მეტრეველი', 'ნეფარიძე', 'მოდებაძე', 'მარჯანიძე', 'მუმლაძე', 'ნასრაშვილი',  'ჯანჯღავა', 'მოსია',
          'ნოზაძე', 'ნუცუბიძე', 'ონიანი', 'ოქრუაშვილი', 'პერტია', 'რაზმაძე', 'რევაზაშვილი', 'საგანელიძე', 'ჯახაია',
          'სალუქვაძე', 'სამსონაშვილი', 'სამხარაძე', 'სარალიძე', 'სართანია', 'სარიშვილი', 'სიმონიშვილი', 'სხილაძე',
          'ხურციძე', 'სიხარულიძე', 'ტაბატაძე', 'ფაცაცია', 'ფილაური', 'ფუხაშვილი', 'ქობალია', 'ყიფშიძე', 'შაინიძე',
          'ფიფია', 'შენგელია', 'შეროზია', 'შველიძე', 'ჩხეიძე', 'ჩადუნელი', 'ჩიკვაშვილი', 'ცქიტიშვილი', 'ჩოკორაია',
          'ცაგურია', 'ცერცვაძე', 'ცუხიშვილი', 'ძინძიბაძე', 'წერეთელი', 'წიკლაური', 'ჭავჭანიძე', 'ჩირაძე', 'ჭელიძე',
          'ჭანტურია', 'სირაძე', 'შონია', 'ხანჯალაძე', 'ხარაზიშვილი', 'ხელაძე', 'ხვინგია', 'ხუციშვილი', 'ჯანელიძე',
          'ჯოხაძე']

FNames = ['ანა', 'ანუკი', 'ბარბარე', 'გვანცა', 'დიანა', 'ეკა', 'ელენე', 'ვერონიკა', 'ვიქტორია', 'თათია', 'ლამზირა',
          'თეა', 'თეკლე', 'თინიკო', 'თამარი', 'იზაბელა', 'ია', 'იამზე', 'ლია', 'ლიკა', 'ლანა', 'მარიკა', 'მანანა',
          'მაია', 'მაკა', 'მარიამი', 'ნანა', 'ნანი', 'ნატა', 'ნატო', 'ნინო', 'ნონა', 'ოლიკო', 'ქეთევანი', 'სალომე',
          'სოფიკო', 'ნია', 'ქრისტინე', 'შორენა', 'ხატია', 'ალეკო', 'ალიკა', 'ამირან', 'ანდრია', 'არჩილი', 'ასლანი',
          'ბაჩუკი', 'ბექა',   'გიგა', 'გიორგი', 'დავითი',
          'გიგი', 'გოგა', 'დათა', 'ერეკლე', 'თემური', 'იაკობ', 'ილია', 'ირაკლი', 'ლადო', 'ლაშა', 'მიხეილ',
          'ნიკა', 'ოთარი', 'პაატა', 'რამაზ', 'რამინი', 'რატი', 'რაული', 'რევაზი', 'რომა', 'რომანი', 'სანდრო',
          'საბა', 'სერგი', 'სიმონ', 'შალვა', 'შოთა', 'ცოტნე', 'ჯაბა']

Subject = ['პროგრამირების საფუძვლები', 'კალკულუსი', 'შესავალი ფიზიკაში', 'კომპიუტერული უნარჩვევები',
           'ქიმიის შესავალი', 'ბიოლოგიის შესავალი', 'ალგორითმები I', 'შესავალი ელექტრონიკაში',
           'მონაცემთა სტრუქტურები', 'ალგორითმები II']

Point = [str(i) for i in range(101)]
ch = random.choice
Stud_recs = [' '.join([ch(LNames), ch(FNames), ch(Subject), ch(Point)]) for _ in range(10)]

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["pythonMagaria"]
myTabl = mydb["pupils"]

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1017, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #labels
        self.idLabel = QtWidgets.QLabel(self.centralwidget)
        self.idLabel.setGeometry(QtCore.QRect(5, 10, 221, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.idLabel.setFont(font)
        self.idLabel.setObjectName("label")

        self.lasNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.lasNameLabel.setGeometry(QtCore.QRect(5, 110, 221, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lasNameLabel.setFont(font)
        self.lasNameLabel.setObjectName("label")

        self.nameLabel = QtWidgets.QLabel(self.centralwidget)
        self.nameLabel.setGeometry(QtCore.QRect(5, 210, 221, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nameLabel.setFont(font)
        self.nameLabel.setObjectName("label")

        self.subLabel = QtWidgets.QLabel(self.centralwidget)
        self.subLabel.setGeometry(QtCore.QRect(5, 310, 221, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.subLabel.setFont(font)
        self.subLabel.setObjectName("label")

        self.markLabel = QtWidgets.QLabel(self.centralwidget)
        self.markLabel.setGeometry(QtCore.QRect(5, 410, 221, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.markLabel.setFont(font)
        self.markLabel.setObjectName("label")

        # text input
        self.idInput = QtWidgets.QTextEdit(self.centralwidget)
        self.idInput.setGeometry(QtCore.QRect(80, 20, 351, 61))
        self.idInput.setObjectName("textInput")

        self.lastNameInput = QtWidgets.QTextEdit(self.centralwidget)
        self.lastNameInput.setGeometry(QtCore.QRect(80, 120, 351, 61))
        self.lastNameInput.setObjectName("textInput")

        self.nameInput = QtWidgets.QTextEdit(self.centralwidget)
        self.nameInput.setGeometry(QtCore.QRect(80, 220, 351, 61))
        self.nameInput.setObjectName("textInput")

        self.subInput = QtWidgets.QTextEdit(self.centralwidget)
        self.subInput.setGeometry(QtCore.QRect(80, 320, 351, 61))
        self.subInput.setObjectName("textInput")

        self.markInput = QtWidgets.QTextEdit(self.centralwidget)
        self.markInput.setGeometry(QtCore.QRect(80, 420, 351, 61))
        self.markInput.setObjectName("textInput")

        # buttons
        self.writeAllDataButt = QtWidgets.QPushButton(self.centralwidget)
        self.writeAllDataButt.setGeometry(QtCore.QRect(490, 20, 421, 61))
        self.writeAllDataButt.setObjectName("writeAllDataButt")
        self.writeAllDataButt.setText('ყველა ჩანაწერის გაკეთება')

        self.searchButt = QtWidgets.QPushButton(self.centralwidget)
        self.searchButt.setGeometry(QtCore.QRect(490, 130, 421, 61))
        self.searchButt.setObjectName("searchButt")
        self.searchButt.setText('ძებნა')

        self.updateButt = QtWidgets.QPushButton(self.centralwidget)
        self.updateButt.setGeometry(QtCore.QRect(490, 240, 421, 61))
        self.updateButt.setObjectName("updateButt")
        self.updateButt.setText('განახლება')

        self.removeButt = QtWidgets.QPushButton(self.centralwidget)
        self.removeButt.setGeometry(QtCore.QRect(490, 350, 421, 61))
        self.removeButt.setObjectName("removeButt")
        self.removeButt.setText('წაშლა')

        self.writeButt = QtWidgets.QPushButton(self.centralwidget)
        self.writeButt.setGeometry(QtCore.QRect(80, 490, 351, 61))
        self.writeButt.setObjectName("writeButt")
        self.writeButt.setText('ჩაწერა')

        self.closeButt = QtWidgets.QPushButton(self.centralwidget)
        self.closeButt.setGeometry(QtCore.QRect(800, 500, 80, 40))
        self.closeButt.setObjectName("closeButt")
        self.closeButt.setText('close')

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1017, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.closeButt.clicked.connect(exit)
        self.writeAllDataButt.clicked.connect(self.writeAllDataToDb)
        self.searchButt.clicked.connect(self.findPupil)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.idLabel.setText(_translate("MainWindow", "იდენტ")) 
        self.lasNameLabel.setText(_translate("MainWindow", "გვარი"))
        self.nameLabel.setText(_translate("MainWindow", "სახელი")) 
        self.subLabel.setText(_translate("MainWindow", "საგანი")) 
        self.markLabel.setText(_translate("MainWindow", "შეფასება")) 
        
    def writeAllDataToDb(self):
        for i in range(0,len(Stud_recs)):
            dicti = {
                'name' : Stud_recs[i].split()[1],
                'surname' : Stud_recs[i].split()[0],
                'subject' : Stud_recs[i].split()[2]+ ' ' +Stud_recs[i].split()[3],
                'mark' : Stud_recs[i].split()[4]
            }
            myTabl.insert_one(dicti)

    def findPupil(self):
        if len(self.nameInput.toPlainText())> 0 and len(self.lastNameInput.toPlainText())> 0:
            found = myTabl.find({'name':self.nameInput.toPlainText(),'surname':self.lastNameInput.toPlainText()})
        elif len(self.nameInput.toPlainText())> 0:
            found = myTabl.find({'name':self.nameInput.toPlainText()})
        elif len(self.lastNameInput.toPlainText())> 0:
            found = myTabl.find({'surname':self.lastNameInput.toPlainText()})

        for i in found:
            print(i)
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
