from Infrastructure.txt_reader import TxtHandler


class SqlHandler:
    def __init__(self, path):
        self.path = path

    def create_table_from_txt(self, txt_path):
        txtHandler = TxtHandler(txt_path)
        txtHandler.read_txt()

        with open(self.path, "w") as sql_file:
            sql_file.write(
                f"CREATE TABLE IF NOT EXISTS gps_data (matricula VARCHAR(100) PRIMARY KEY,pos_date VARCHAR(50));")
            sql_file.write("\n")
            for matricula, pos_date in txtHandler.dict_pos_date.items():
                sql_file.write(f"INSERT INTO gps_data (matricula, pos_date)\nVALUES ('{matricula}','{pos_date.strip()}');")
                sql_file.write("\n")

            sql_file.close()
