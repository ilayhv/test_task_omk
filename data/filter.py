from dataclasses import dataclass

@dataclass
class Filter():
    """фильтр по значениям в тестовом датафрейме
    """
    column:str = None
    number:int = None
    equal:str = None
    data_frame:str = None
    search_param:dict=None
    
    def convert_args(self):
        """поиск атрибутов поиска в полученных
        аргументах запроса реализована доп проверка на undefined
        так как по умолчанию возвращает такое значение
        """
        if "number" in self.search_param:
            if self.search_param["number"] != "undefined":
                self.number = self.search_param["number"]
        if "equal" in self.search_param:
            if self.search_param["equal"] != "undefined":
                self.equal = self.search_param["equal"]
        if "column" in self.search_param:
            if self.search_param["column"] != "undefined":
                self.column = self.search_param["column"]                
                
    def filtering(self):
        """ непосредственно фильтрация датафрейма
        """            
        if (self.number is not None and
            self.equal is not None and
            self.column is not None):
            
            if self.equal == "over":
                temp = self.data_frame[self.column]>=int(self.number)
            if self.equal == "less":
                temp = self.data_frame[self.column]<=int(self.number)                
            if self.equal == "equal":
                temp = self.data_frame[self.column]<=int(self.number)              
            return self.data_frame[temp]
        else:
            return self.data_frame