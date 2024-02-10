class MockCSR:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.values = []
        self.column_indices = []
        self.row_pointers = [0]

    def add_service(self, merchant_id, pincode):
        if merchant_id >= len(self.row_pointers):
            self.row_pointers.append(len(self.values))

        self.values.append(1)
        self.column_indices.append(pincode)

    def done(self):
        self.row_pointers.append(len(self.values))

    def is_there(self, merchant_id, pincode):
        if merchant_id < 0 or merchant_id >= len(self.row_pointers) - 1:
            return False
        row_start = self.row_pointers[merchant_id]
        row_end = self.row_pointers[merchant_id + 1]

        for i in range(row_start, row_end):
            if self.column_indices[i] == pincode and self.values[i] == 1:
                return True

        return False

    def based_merchants(self, pincode):
        merchants = [mi for mi in range(len(self.row_pointers) - 1)
                     if any(self.column_indices[i] == pincode and self.values[i] == 1
                            for i in range(self.row_pointers[mi], self.row_pointers[mi + 1]))]
        return merchants

