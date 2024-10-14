from PySide6.QtCore import QObject, Signal
from ckiptagger import WS, construct_dictionary
import pandas as pd


class WorkThread(QObject):
    logSignal = Signal(str)

    def __init__(self):
        super().__init__()
        self.ws = WS('./data', disable_cuda=False)

    def setData(self, 
                df: pd.DataFrame, 
                ckipInput: str, 
                ckipOutput: str, 
                longWord: list[str], 
                sameWord: list[str], 
                outputPath: str):
        self.df = df
        self.ckipInput = ckipInput
        self.ckipOutput = ckipOutput
        self.longWord = longWord
        self.sameWord = sameWord
        self.outputPath = outputPath

    def ckipProcess(self,content:str):
        if type(content) != str:
            return []
        result = self.ws([content])[0] if pd.notna(content) else []
        self.logSignal.emit(f'{content} -> \n {result}')


    def work(self):
        self.df[self.ckipOutput] = self.df[self.ckipInput].apply(self.ckipProcess)
        self.df.to_excel(f'{self.outputPath}.xlsx')
        self.df.to_json(f'{self.outputPath}.json', orient="records", lines=True, force_ascii=False)
        del self.ws
        self.thread().exit(0)
