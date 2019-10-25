from HtmlGenerator import HtmlGenerator


def main():
    webpage = HtmlGenerator(path="test/test.html")

    # Make a table
    webpage.add_subtitle("Table 1")
    table1 = webpage.add_table("Test table")
    table1.add_column("Column1")
    table1.add_column("Column2")
    table1.add_column("Column3")
    table1.add_column("Column3")
    table1.add_row(["data1", "data2", "data3", webpage.mesh("test/output_atlas.obj")], "line1")

    webpage.add_subtitle("Table 2")
    table2 = webpage.add_table("Test table 2")
    table2.add_column("Column1")
    table2.add_column("Column2")
    table2.add_row(["data1", "data2"], "line1")

    webpage.return_html()


if __name__ == "__main__":
    main()
