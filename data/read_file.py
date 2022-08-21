import pandas as pd
from dataclasses import dataclass
import os
from os.path import abspath


@dataclass
class DataFrame():
    """чтение датафрейма 
    """
    file:str = os.path.join(__file__[:__file__.rfind("\\")],"cars93.csv")
    
    def read(self):
        """чтение и отдача его как есть
        """
        _data = pd.read_csv(self.file)
        return(_data)


if __name__ == "__main__":
    df =DataFrame()
    df.read()