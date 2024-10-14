from UI_ui import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QFileDialog, QAbstractItemView, QMessageBox
from PySide6.QtCore import QStringListModel, QModelIndex, QThread
from WorkThread import WorkThread
import pandas as pd


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        # 斷詞側的介面設定
        self.btnOpen.clicked.connect(self.openCKIPInputFile)
        self.btnSetLocation.clicked.connect(self.saveCKIPOutputFile)
        self.btnStartCKIP.clicked.connect(self.startCKIP)
        self.txtResult.setReadOnly(True)

        self.longWordModel = QStringListModel()
        self.lstLongWord.setModel(self.longWordModel)
        self.lstLongWord.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers
        )

        self.sameWordModel = QStringListModel()
        self.lstSameWord.setModel(self.sameWordModel)
        self.lstSameWord.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers
        )

        self.txtLongWord.returnPressed.connect(self.addLongWord)
        self.txtSameWord.returnPressed.connect(self.addSameWord)

        self.lstLongWord.doubleClicked.connect(self.removeLongWord)
        self.lstSameWord.doubleClicked.connect(self.removeSameWord)

        self.ckipThread = QThread()
        self.worker = WorkThread()
        self.worker.logSignal.connect(self.log)

        self.worker.moveToThread(self.ckipThread)
        self.ckipThread.started.connect(self.worker.work)
        self.ckipThread.finished.connect(self.ckipFinished)

    def openCKIPInputFile(self):
        openFilePath, _ = QFileDialog.getOpenFileName(
            self, "請選擇要開來斷詞的檔案", filter='Excel 檔案 (*.xlsx);;JSON 檔案 (*.json)')
        self.txtInput.setText(openFilePath)
        if len(openFilePath) == 0:
            return

        if openFilePath.endswith('.xlsx'):
            df = pd.read_excel(openFilePath, index_col=[0])
        elif openFilePath.endswith('.json'):
            df = pd.read_json(openFilePath, orient="records", lines=True)
        else:
            df = pd.DataFrame()

        self.df = df
        df_columns = df.columns.tolist()
        self.cmbColumns.clear()
        self.cmbColumns.addItems(df_columns)

    def saveCKIPOutputFile(self):
        saveFilePath, _ = QFileDialog.getSaveFileName(self, '請選擇要把斷好詞的檔案的儲存位置')
        self.txtOutput.setText(saveFilePath)

    def addLongWord(self):
        longWord = self.txtLongWord.text().strip()
        # 字串為空就無視
        if len(longWord) == 0 or longWord.isspace():
            return
        num = self.longWordModel.rowCount()
        self.longWordModel.insertRow(num)
        index = self.longWordModel.index(num)
        self.longWordModel.setData(index, longWord)
        self.txtLongWord.clear()

    def addSameWord(self):
        sameWord = self.txtSameWord.text().strip()
        # 字串為空就無視
        if len(sameWord) == 0 or sameWord.isspace():
            return
        # 只輸入一個詞
        if len(sameWord.split('|')) < 2:
            QMessageBox.critical(
                self, '輸入錯誤', '請輸入正確格式的同義詞表。同義詞之間用 \' | \' 隔開，只輸入一個詞無效！', QMessageBox.StandardButton.Ok)
            return
        if sameWord.endswith('|'):
            QMessageBox.critical(
                self, '輸入錯誤', '請輸入正確格式的同義詞表。同義詞之間用 \' | \' 隔開，不需要以 \' | \' 結尾！', QMessageBox.StandardButton.Ok)
            return
        num = self.sameWordModel.rowCount()
        self.sameWordModel.insertRow(num)
        index = self.sameWordModel.index(num)
        self.sameWordModel.setData(index, sameWord)
        self.txtSameWord.clear()

    def removeLongWord(self, index: QModelIndex):
        row = index.row()
        self.longWordModel.removeRow(row)

    def removeSameWord(self, index: QModelIndex):
        row = index.row()
        self.sameWordModel.removeRow(row)

    def log(self, message: str):
        self.txtResult.appendPlainText(f'{message}\n')

    def startCKIP(self):
        self.worker.setData(self.df,
                            self.cmbColumns.currentText(),
                            self.txtCKIPOutputColumn.text(),
                            self.longWordModel.stringList(),
                            self.sameWordModel.stringList(),
                            self.txtOutput.text())
        self.ckipThread.start()
        self.setStatus(True)

    def setStatus(self,isStartCkip:bool):
        self.btnOpen.setEnabled(not isStartCkip)
        self.btnSetLocation.setEnabled(not isStartCkip)
        self.cmbColumns.setEnabled(not isStartCkip)
        self.txtCKIPOutputColumn.setEnabled(not isStartCkip)
        self.txtLongWord.setEnabled(not isStartCkip)
        self.txtSameWord.setEnabled(not isStartCkip)
        self.lstLongWord.setEnabled(not isStartCkip)
        self.lstSameWord.setEnabled(not isStartCkip)
        self.btnStartCKIP.setEnabled(not isStartCkip)

    def ckipFinished(self):
        QMessageBox.information(self,'結果','斷詞完成！',QMessageBox.StandardButton.Ok)
        self.setStatus(False)
