from PyQt5 import QtWidgets
from shopping_list import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.show_selected_items)
        print("დაეჭირა")
        self.ui.comboBox.currentTextChanged.connect(self.on_combo_changed)

    def on_combo_changed(self, text):
        print(f"ComboBox-ში არჩეულია: {text}")

    def show_selected_items(self):
        print("ღილაკზე დააჭირეს")
        items = []
        food = self.ui.comboBox.currentText()
        food_time  = {"საუზმე": " 7:00", "სადილი":" 14:00", "ვახშამი": " 18:00"}
        time_label = food_time.get(food, "უცნობი დრო")

        if self.ui.checkBox_puri.isChecked():
            items.append("პური")
        if self.ui.checkBox_kvercxi.isChecked():
            items.append("კვერცხი")
        if self.ui.checkBox_yveli.isChecked():
            items.append("ყველი")
        if self.ui.checkBox_arajani.isChecked():
            items.append("არაჟანი")
        if self.ui.checkBox_brinji.isChecked():
            items.append("ბრინჯი")
        if self.ui.checkBox_pomidori.isChecked():
            items.append("პომიდორი")

        if items:
            result = "შერჩეული პროდუქტებია: " + ", ".join(items)+"."+ f" ამ საკვების მისაღები დროა:{time_label} "
        else:
            result = "არცერთი პროდუქტი არ არის მონიშნული."

        self.ui.label_result.setText(result)
        self.ui.label_result.setWordWrap(True)
        self.ui.label_result.adjustSize()  

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
