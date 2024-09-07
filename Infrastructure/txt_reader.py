class TxtReader:
    def __init__(self, path):
        self.path = path

    def dict_to_txt(self, dates_dict):
        txt = open(self.path, "w")

        for matricula, date in dates_dict.items():
            txt.write(matricula+","+date)
            txt.write("\n")

        txt.close()


