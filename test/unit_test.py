from HtmlGenerator import HtmlGenerator


def main():

    # Gather a few data to display

    # A curve
    curve_data = {"loss": [1, 2, 3, 5]}

    # A parameter dict
    mydict = {
        "key1": 0,
        "key2": 1,
        "key3": [5, 6, 7],
        "key4": 3.141592,
        "key5": "toto",
        "key6": {"toto": 1, "tata": 2},
    }

    # A random matrix
    import numpy as np
    rows = 10
    cols = 6
    rand_matrix = np.random.randint(-50, 50, (rows, cols)) / 5.0

    # Let's make a website!
    webpage = HtmlGenerator(path="test/test.html")

    # Make a title and a subtitle
    webpage.add_title("Table 1")
    webpage.add_subtitle("This is a subtitle")

    # Make a 1st table
    table1 = webpage.add_table()
    table1.add_column("Accuracy1")
    table1.add_column("Accuracy2")
    table1.add_column("Curve")
    table1.add_column("Mesh")
    curve = webpage.curve(curve_data, title="My curve")
    table1.add_row([0.5, curve, curve, webpage.mesh("test/output_atlas.obj")], "line1")
    webpage.return_html()

    # Make a 2nd table
    webpage.add_title("Table 2")
    table2 = webpage.add_table()
    table2.add_columns(["Column1", "Column2"])
    table2.add_titleless_columns(1)

    table2.add_row(["data1", webpage.image("lena.jpeg"), webpage.dict(mydict), 0])
    table2.add_row([{"data1": 0.5}, webpage.image("lena.jpeg"), curve, webpage.confMat(rand_matrix)])
    table2.add_row(["Additional_data"]*9)
    table2.add_row(["Additional_data"]*9)
    table2.add_row([webpage.image("lena.jpeg")]*2)

    # curve_2 = webpage.curve(curve_data, title="My curve", width_factor=0.8)
    webpage.add_curve(curve_data, title="My curve", width_factor=0.6)

    webpage.return_html()


if __name__ == "__main__":
    main()
