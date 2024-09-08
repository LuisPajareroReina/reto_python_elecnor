class TxtHandler:
    def __init__(self, path):
        self.path = path
        self.dict_pos_date = {}

    def dict_to_txt(self, dates_dict):
        txt = open(self.path, "w")

        for matricula, date in dates_dict.items():
            txt.write(matricula + "," + date)
            txt.write("\n")

        txt.close()

    def read_txt(self):
        with open(self.path) as txt_file:
            for line in txt_file:
                if ',' in line:
                    matricula, pos_date = line.split(",")
                    self.dict_pos_date[matricula] = pos_date

    def get_last_date_from_txt(self, matricula):
        return self.dict_pos_date[matricula]

