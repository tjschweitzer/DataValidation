
class ColumnConfig:
    def __init__(self,name,c_type,value=None,start_index=-1,end_index=-1):
        """
        Configuration of each column and the value or placement of the value
        :param name: column name
        :param c_type: data type
        :param value: value, used if value is constant for the column
        :param start_index: start index of the column value
        :param end_index: end index of the column value
        """
        self.name = name
        self.c_type = c_type
        self.value = value
        self.start_index = start_index
        self.end_index = end_index

    def get_value(self,line):
        if self.value != None:
            return self.value

        return line[self.start_index:self.end_index]
