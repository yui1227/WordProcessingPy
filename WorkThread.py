from PySide6.QtCore import QObject, Signal
from ckiptagger import WS, construct_dictionary
import pandas as pd


class WorkThread(QObject):
    logSignal = Signal(str)

    def __init__(self):
        super().__init__()
        self.ws = WS("./data", disable_cuda=False)

    def setData(
        self,
        df: pd.DataFrame,
        ckipInput: str,
        ckipOutput: str,
        longWord: list[str],
        sameWord: list[str],
        outputPath: str,
    ):
        self.df = df
        self.ckipInput = ckipInput
        self.ckipOutput = ckipOutput
        self.longWord = longWord
        self.sameWord = sameWord
        self.outputPath = outputPath

    def ckipProcess(self, content: str, long_words: list[tuple]):
        if type(content) != str:
            return []
        result = (
            self.ws([content], recommend_dictionary=long_words)[0]
            if pd.notna(content)
            else []
        )
        self.logSignal.emit(f"{content} -> \n {result}")
        return result

    def getAllLongWords(self):
        # 把同義詞裡面所有的詞加到長詞列表裡，並生成長詞字典
        all_long_word = [
            word for samewords in self.sameWord for word in samewords.split("|")
        ] + self.longWord
        all_long_word_dict = {word: 1 for word in all_long_word}
        all_long_word_tuple_list = construct_dictionary(all_long_word_dict)
        return all_long_word_tuple_list

    def replaceSameWords(
        self, ckip_list: list[str], same_word: dict[str, list[str]]
    ) -> list[str]:
        if type(ckip_list) == str:
            ckip_list = eval(ckip_list)
        # 走訪斷詞好的陣列
        for idx in range(len(ckip_list)):
            # 每個字去檢查
            for main_word, replace_words in same_word.items():
                # 如果要取代的字有在特定列表裡
                if ckip_list[idx] in replace_words:
                    ckip_list[idx] = main_word
        return ckip_list

    def getSameWords(self) -> dict[str, list[str]]:
        same_words_dict = {
            key: values
            for long_word in self.sameWord
            for key, *values in [long_word.split("|")]
        }
        return same_words_dict

    def work(self):
        # 把同義詞裡面所有的詞加到長詞列表裡，並生成長詞字典
        all_long_word_dict = self.getAllLongWords()
        # 斷詞
        self.df[self.ckipOutput] = self.df[self.ckipInput].apply(
            self.ckipProcess, args=(all_long_word_dict,)
        )
        # 同義詞取代
        self.df[self.ckipOutput] = self.df[self.ckipOutput].apply(
            self.replaceSameWords, args=(self.getSameWords(),)
        )

        # 存檔
        self.df.to_excel(f"{self.outputPath}.xlsx")
        self.df.to_json(
            f"{self.outputPath}.json", orient="records", lines=True, force_ascii=False
        )
        del self.ws
        self.thread().exit(0)
