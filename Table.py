class TableException(Exception):
    pass


class Table:
    def __init__(self, title):
        self.title = title
        self.columns = []  # 1st column contains the title
        self.rows = []
        self.are_columns_fixed = False
        self.td_str = None

    def add_column(self, title):
        if self.are_columns_fixed:
            raise TableException("You can't add a column after having added the first row!")
        self.columns.append(title)

    def add_row(self, data, title=""):
        self.are_columns_fixed = True
        if len(data) != len(self.columns):
            raise TableException("Error! The number of data you fed does not match the number of columns you defined.")
        self._make_td_str()
        row_str = f"<tr>\n{self.td_str}{title}</td>\n{self.td_str}"
        row_str += f"</td>\n{self.td_str}".join(data)
        row_str += "</td>\n</tr>\n"
        self.rows.append(row_str)

    def _make_td_str(self):
        width_percentage = 100. / float(len(self.columns) + 1)
        self.td_str = f"<td align=\"center\" width=\"{width_percentage}%\">"

    def __str__(self):
        self._make_td_str()
        data = "<table width=100%>\n"
        # Columns titles
        data += f"<tr>\n{self.td_str}{self.title}</td>\n{self.td_str}"
        data += f"</td>\n{self.td_str}".join([x for x in self.columns])
        data += "</td>\n</tr>\n"
        # Rows
        data += "\n".join(self.rows)
        data += "</table>"
        return data
