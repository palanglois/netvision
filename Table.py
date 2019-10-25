class TableException(Exception):
    pass


class Table:
    def __init__(self, title):
        self.title = title
        self.columns = []  # 1st column contains the title
        self.rows = []
        self.are_columns_fixed = False
        self.td_str = None
        self.td_str_bold = None
        self.td_row_title_str = None
        self.width_percentage = None

    def add_column(self, title):
        if self.are_columns_fixed:
            raise TableException("You can't add a column after having added the first row!")
        self.columns.append(title)

    def add_columns(self, titles):
        if self.are_columns_fixed:
            raise TableException("You can't add a column after having added the first row!")
        self.columns += titles

    def add_titleless_columns(self, number):
        if self.are_columns_fixed:
            raise TableException("You can't add a column after having added the first row!")
        self.columns += [str(i + len(self.columns) + 1) for i in range(number)]

    def add_row(self, data, title=""):
        if title == "":
            title = str(len(self.rows) + 1)
        self.are_columns_fixed = True
        if len(data) != len(self.columns):
            raise TableException("Error! The number of data you fed does not match the number of columns you defined.")
        self._make_td_str()
        row_str = f"<tr>\n{self.td_row_title_str}{title}</td>\n{self.td_str}"
        row_str += f"</td>\n{self.td_str}".join([self._pretreat_data(str(x)) for x in data])
        row_str += "</td>\n</tr>\n"
        self.rows.append(row_str)

    def _pretreat_data(self, data):
        # Trick to properly reshape the Chart js objects
        if "new Chart(" in data:
            width_begin = data.find("parentNode.style.width") + 24
            width_end = data[width_begin:].find(';')
            data = data.replace(data[width_begin:width_begin + width_end], f"\"{self.width_percentage}%\"")
        return data

    def _make_td_str(self):
        row_title_weight = 5.
        self.width_percentage = 100. / float(len(self.columns) * row_title_weight + 1)
        self.td_str = f"<td align=\"center\" width=\"{row_title_weight * self.width_percentage}%\">"
        self.td_row_title_str = f"<td style=\"font-weight: bold;\" align=\"center\" width=\"{self.width_percentage}%\">"
        self.td_str_bold = f"<td style=\"font-weight: bold;\" align=\"center\" width=\"{self.width_percentage}%\">"

    def __str__(self):
        self._make_td_str()
        data = "<table width=100%>\n"
        # Columns titles
        data += f"<tr>\n{self.td_row_title_str}{self.title}</td>\n{self.td_str_bold}"
        data += f"</td>\n{self.td_str_bold}".join([x for x in self.columns])
        data += "</td>\n</tr>\n"
        # Rows
        data += "\n".join(self.rows)
        data += "</table>\n"
        return data
