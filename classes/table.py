class Table:
    def __init__(self, user_file=""):
        self.table = {}
        self.tombstone = "f4d1780b4dc07be1703603b92c3cc66f5f72df5ccf9242a7c0617dfd7012d0fa"
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
        val = self.table[key]
        if val == self.tombstone:
            return "Error: Invalid Key"
        return f"Returning Record {key}: {self.table[key]}."

    
    def update_record(self, key: str, val: str) -> bool:
        old_val = self.table[key]
        if old_val == self.tombstone:
            return "Error: Invalid Key"

        self.table[key] = val
        with open(self.internal_file, mode="r", encoding="utf-8") as f:
            updated_records = f.readlines()
            updated_records[key] = f'{key}, {value}'
        self.write_db(updated_records)
        
    def delete_record(self, key: str) -> bool:
        self.update_record(key, self.tombstone)
    
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

    def write_db(self, updated_records) -> bool:
        with open(self.internal_file, mode="w", encoding="utf-8") as f:
            f.writelines(updated_records)
        return True
        
