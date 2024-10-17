from UI_ui import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QFileDialog, QAbstractItemView, QMessageBox, QTableView
from PySide6.QtCore import QStringListModel, QModelIndex, QThread
from PySide6.QtGui import QCloseEvent
from WorkThread import WorkThread
import pandas as pd
import os.path
import json
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from DataFrameModel import DataFrameModel


class MainWindow(QMainWindow, Ui_MainWindow):
    fileList = ["long_words.json", "same_words.json", "stop_words.json"]

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        # 斷詞側的介面設定
        # 事件綁定
        self.btnOpen.clicked.connect(self.openCKIPInputFile)
        self.btnSetLocation.clicked.connect(self.saveCKIPOutputFile)
        self.btnStartCKIP.clicked.connect(self.startCKIP)
        self.txtResult.setReadOnly(True)
        self.txtLongWord.returnPressed.connect(self.addLongWord)
        self.txtSameWord.returnPressed.connect(self.addSameWord)
        self.lstLongWord.doubleClicked.connect(self.removeLongWord)
        self.lstSameWord.doubleClicked.connect(self.removeSameWord)

        # 檢查長詞 同義詞 停用詞檔案是否存在
        for wordfile in self.fileList:
            if os.path.isfile(wordfile):
                continue
            # 不存在就建立空檔案
            with open(wordfile, mode="w", encoding="utf-8") as newf:
                json.dump([], newf, ensure_ascii=False)

        # 字串列表綁定
        self.longWordModel = QStringListModel()
        self.lstLongWord.setModel(self.longWordModel)
        self.lstLongWord.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        with open(self.fileList[0], mode="r", encoding="utf-8") as newf:
            self.longWordModel.setStringList(json.load(newf))

        self.sameWordModel = QStringListModel()
        self.lstSameWord.setModel(self.sameWordModel)
        self.lstSameWord.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        with open(self.fileList[1], mode="r", encoding="utf-8") as newf:
            self.sameWordModel.setStringList(json.load(newf))

        # 斷詞用執行緒，不然主視窗會卡住
        self.ckipThread = QThread()
        self.worker = WorkThread()
        self.worker.logSignal.connect(self.log)

        self.worker.moveToThread(self.ckipThread)
        self.ckipThread.started.connect(self.worker.work)
        self.ckipThread.finished.connect(self.ckipFinished)
        # 共現側的元件設定
        self.btnOpenCKIPed.clicked.connect(self.openCkipedFile)
        self.txtStopWord.returnPressed.connect(self.addStopWord)
        self.lstStopWord.doubleClicked.connect(self.removeStopWord)
        self.stopWordModel = QStringListModel()
        self.lstStopWord.setModel(self.stopWordModel)
        self.lstStopWord.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        with open(self.fileList[2], mode="r", encoding="utf-8") as newf:
            self.stopWordModel.setStringList(json.load(newf))
        self.btnSaveCooccurrence.clicked.connect(self.saveCooccurrence)
        self.btnPreviewCooccurrence.clicked.connect(self.previewCooccurrence)

    def openCKIPInputFile(self):
        openFilePath, _ = QFileDialog.getOpenFileName(
            self,
            "請選擇要開來斷詞的檔案",
            filter="Excel 檔案 (*.xlsx);;JSON 檔案 (*.json)",
        )
        self.txtInput.setText(openFilePath)
        if len(openFilePath) == 0:
            return

        if openFilePath.endswith(".xlsx"):
            df = pd.read_excel(openFilePath, index_col=[0])
        elif openFilePath.endswith(".json"):
            df = pd.read_json(openFilePath, orient="records", lines=True)
        else:
            df = pd.DataFrame()

        self.df = df
        df_columns = df.columns.tolist()
        self.cmbColumns.clear()
        self.cmbColumns.addItems(df_columns)

    def saveCKIPOutputFile(self):
        saveFilePath, _ = QFileDialog.getSaveFileName(
            self, "請選擇要把斷好詞的檔案的儲存位置"
        )
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
        if len(sameWord.split("|")) < 2:
            QMessageBox.critical(
                self,
                "輸入錯誤",
                "請輸入正確格式的同義詞表。同義詞之間用 ' | ' 隔開，只輸入一個詞無效！",
                QMessageBox.StandardButton.Ok,
            )
            return
        if sameWord.endswith("|"):
            QMessageBox.critical(
                self,
                "輸入錯誤",
                "請輸入正確格式的同義詞表。同義詞之間用 ' | ' 隔開，不需要以 ' | ' 結尾！",
                QMessageBox.StandardButton.Ok,
            )
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
        self.txtResult.appendPlainText(f"{message}\n")

    def startCKIP(self):
        self.worker.setData(
            self.df,
            self.cmbColumns.currentText(),
            self.txtCKIPOutputColumn.text(),
            self.longWordModel.stringList(),
            self.sameWordModel.stringList(),
            self.txtOutput.text(),
        )
        self.ckipThread.start()
        self.setStatus(True)

    def setStatus(self, isStartCkip: bool):
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
        QMessageBox.information(
            self, "結果", "斷詞完成！", QMessageBox.StandardButton.Ok
        )
        self.setStatus(False)

    def closeEvent(self, event: QCloseEvent):
        # 退出時儲存三個詞表
        with open(self.fileList[0], mode="w", encoding="utf-8") as newf:
            json.dump(self.longWordModel.stringList(),newf,ensure_ascii=False,indent=4)
        with open(self.fileList[1], mode="w", encoding="utf-8") as newf:
            json.dump(self.sameWordModel.stringList(),newf,ensure_ascii=False,indent=4)
        with open(self.fileList[2], mode="w", encoding="utf-8") as newf:
            json.dump(self.stopWordModel.stringList(),newf,ensure_ascii=False,indent=4)
        # 如果在斷詞就詢問
        if self.ckipThread.isRunning():
            btn = QMessageBox.question(
                self,
                "您確定要離開嗎？",
                "目前正在進行斷詞，退出將不會儲存結果，您確定要離開嗎",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            )
            if btn == QMessageBox.StandardButton.Yes:
                self.ckipThread.terminate()
                event.accept()
            else:
                event.ignore()

    def addStopWord(self):
        stopWord = self.txtStopWord.text().strip()
        # 字串為空就無視
        if len(stopWord) == 0 or stopWord.isspace():
            return
        num = self.stopWordModel.rowCount()
        self.stopWordModel.insertRow(num)
        index = self.stopWordModel.index(num)
        self.stopWordModel.setData(index, stopWord)
        self.txtStopWord.clear()

    def removeStopWord(self, index: QModelIndex):
        row = index.row()
        self.stopWordModel.removeRow(row)

    def openCkipedFile(self):
        openFilePath, _ = QFileDialog.getOpenFileName(
            self,
            "請選擇已斷詞完成的檔案",
            filter="Excel 檔案 (*.xlsx);;JSON 檔案 (*.json)",
        )
        self.txtInputCKIPedFile.setText(openFilePath)
        if len(openFilePath) == 0:
            return

        if openFilePath.endswith(".xlsx"):
            df = pd.read_excel(openFilePath, index_col=[0])
        elif openFilePath.endswith(".json"):
            df = pd.read_json(openFilePath, orient="records", lines=True)
        else:
            df = pd.DataFrame()
        self.df2 = df
        df_columns = df.columns.tolist()
        self.cmbCKIPDataColumn.clear()
        self.cmbCKIPDataColumn.addItems(df_columns)

    def getCooccurrence(self):
        # 確保斷詞結果是列表形式的字串
        documents = self.df2[self.cmbCKIPDataColumn.currentText()].apply(lambda x: " ".join(x))

        # 使用TF-IDF來找出詞彙的重要性
        # 停用詞
        tfidf_vectorizer = TfidfVectorizer(stop_words=self.stopWordModel.stringList())
        tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
        sum_tfidf = tfidf_matrix.sum(axis=0)
        tfidf_scores = [
            (word, sum_tfidf[0, idx])
            for word, idx in tfidf_vectorizer.vocabulary_.items()
        ]
        sorted_tfidf_scores = sorted(tfidf_scores, key=lambda x: x[1], reverse=True)[
            : self.sbTopWordCount.value()
        ]

        # 取得前100個最重要的詞彙
        top_words = [word[0] for word in sorted_tfidf_scores]
        vectorizer = CountVectorizer(
            vocabulary=top_words
        )  # 使用CountVectorizer僅針對這些詞彙建立詞頻矩陣
        X = vectorizer.fit_transform(documents)

        # 計算共現矩陣
        Xc = X.T * X
        Xc.setdiag(0)  # 將對角線設為0，不計算詞與其自身的共現

        # 將共現矩陣轉換為DataFrame
        features = vectorizer.get_feature_names_out()
        cooccurrence_matrix = pd.DataFrame(
            Xc.toarray(), index=features, columns=features
        )
        return cooccurrence_matrix

    def saveCooccurrence(self):
        saveFilePath, _ = QFileDialog.getSaveFileName(
            self,
            "請選擇要把斷好詞的檔案的儲存位置",
            filter="Excel 檔案 (*.xlsx);;CSV 檔案 (*.csv)",
        )
        self.txtCooccurrenceFilePath.setText(saveFilePath)
        if len(saveFilePath) == 0:
            return
        
        cooccurrence_matrix=self.getCooccurrence()

        if saveFilePath.lower().endswith(".xlsx"):
            cooccurrence_matrix.to_excel(saveFilePath)
        elif saveFilePath.lower().endswith(".csv"):
            cooccurrence_matrix.to_csv(saveFilePath)

    def previewCooccurrence(self):
        cooccurrence_matrix=self.getCooccurrence()
        self.cooc_previwview = QTableView()
        self.cooc_previwview.horizontalHeader().setStretchLastSection(True)
        self.cooc_previwview.setAlternatingRowColors(False)
        self.cooc_previwview.setSelectionBehavior(QTableView.SelectRows)

        self.cooc_previwviewmodel = DataFrameModel(cooccurrence_matrix)
        self.cooc_previwview.setModel(self.cooc_previwviewmodel)
        self.cooc_previwview.show()