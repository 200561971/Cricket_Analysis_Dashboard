import csv

class CsvWriter:
    def __init__(self,file_path) -> None:
        self.file_path = file_path
        with open(self.file_path,'a',encoding="UTF8") as file:
            file.close()



    def write_header(self,header):
        with open(self.file_path,'w',encoding='UTF8') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            file.close()


    def write_row(self,row):
        with open(self.file_path,'a',encoding='UTF8') as file:
            writer = csv.writer(file)
            writer.writerow(row)
            file.close()
        


    def write_rows(self, rows):
        with open(self.file_path,'a',encoding='UTF8') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
            file.close()