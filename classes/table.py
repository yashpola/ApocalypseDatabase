class Table:
    def __init__(self, user_file=""):
        self.table = {}
        if user_file:
            self.read_db(user_file)
            self.internal_file = user_file
        else:
            internal_file = open(file="custom.csv", mode="w")
            self.internal_file = internal_file
            internal_file.close()
        self.idx = 0
        
    def add_record(self, record: str) -> str:
        self.table[self.idx] = record
        self.idx += 1
        self.write_record(self.idx, record)
        return f"Added Record {record} at {self.idx}"
        
    def get_record(self, key: str) -> str:
        return f"Returning Record {key}: {self.table[key]}."
    
    def update_record(self, key: str) -> bool:
        pass
        
    def delete_record(self, key: str) -> bool:
        pass
    
    def read_db(self, user_file: str) -> None:
            with open(file=user_file, mode="r", encoding="utf-8") as raw_file:
                records = raw_file.readlines()
                for record in records:
                    split_record = record.split(',')
                    key = split_record[0]
                    value = split_record[1]
                    self.table[key] = value
        
    def write_record(self, key: int, record: str) -> bool:
        with open(self.internal_file, mode="a", encoding="utf-8") as f:
            f.write(f"{key}, {record}")
        print(f"Wrote record {record} to file {self.internal_file} at {self.idx}")
        return True