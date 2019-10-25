import CurveGenerator
import MeshGenerator
import Table
import ConfusionMatrixGenerator

"""
TODO : 
path de sortie = un dossier 'html'

make minified version of javascript
Zoom curves
Flag deploy
    -- add a zipping function of the whole sources

Add barPlot
Gerer les pointclouds
Gerer les textures
Add minimized obj converter
Mesh generator should resize itself

todo : le jour ou j'ai que ca a foutre
-- bar de chargement
-- gerer les matrices (ou tensor) images numpy (sans avoir a les save quelque avant)
-- make a package pipy

"""


class HtmlGenerator:
    def __init__(self, path=None, title="NetVision visualization"):
        self.path = path
        self.head = []
        self.body = []
        self.curveGen = CurveGenerator.CurveGenerator()
        self.meshGen = MeshGenerator.MeshGenerator()
        self.confMatGen = ConfusionMatrixGenerator.ConfusionMatrixGenerator()
        self.tables = []
        self.title = title
        self.hasCurveHeader = False
        self.hasMeshHeader = False
        self.hasDict = False
        self.make_header()
        self.make_body()

    def make_header(self):
        self.head.append('<head>\n')
        self.head.append('\t<title></title>\n')
        self.head.append('\t<meta name=\"keywords\" content= \"Visual Result\" />  <meta charset=\"utf-8\" />\n')
        self.head.append('\t<meta name=\"robots\" content=\"index, follow\" />\n')
        self.head.append('\t<meta http-equiv=\"Content-Script-Type\" content=\"text/javascript\" />\n')
        self.head.append('\t<meta http-equiv=\"expires\" content=\"0\" />\n')
        self.head.append('\t<meta name=\"description\" content= \"Project page of style.css\" />\n')
        self.head.append('\t<link rel=\"shortcut icon\" href=\"favicon.ico\" />\n')
        self.head.append(" <style> .hor-bar { width:100%; background-color:black;  height:1px;   }"
                         " h3{  margin-top:10px; } </style>")

    def add_javascript_libraries(self):
        if self.hasCurveHeader:
            self.head.append(self.curveGen.make_header())
        if self.hasMeshHeader:
            self.head.append(self.meshGen.make_header())

    def add_css(self):
        if self.hasDict:
            self.head.append(self.add_css_for_add_dict())

    def return_html(self):
        self.add_javascript_libraries()
        self.add_css()

        self.body.append(self.meshGen.end_mesh())
        self.body.append("</body>\n")
        self.head.append('</head>\n')

        begin_html = '<!DOCTYPE html>\n<html>\n'
        self.head_str = "".join(self.head)
        self.body_str = "".join([str(x) for x in self.body])
        end_html = "</html>\n"
        webpage = begin_html + self.head_str + self.body_str + end_html
        if self.path is not None:
            with open(self.path, 'w') as output_file:
                output_file.write(webpage)
        return webpage

    def make_body(self):
        self.body.append('<body style=\"background-color: lightgrey;\">\n')
        self.body.append('<center>\n')
        self.body.append('\t<div class=\"blank\"></div>\n')
        self.body.append('\t<h1>\n')
        self.body.append(f'\t\t{self.title}\n')
        self.body.append('\t</h1>\n')
        self.body.append('</center>\n')
        self.body.append('<div class=\"blank\"></div>\n')

    def add_html_in_body(self, html_content):
        """
        :param html_content: html string.
        :return:
        """
        self.body.append(html_content)

    def add_title(self, title_content):
        body = []
        body.append('\t<h2>\n')
        body.append(f'\t\t{title_content}\n')
        body.append('\t</h2>\n')
        self.body.append("".join(body))

    def add_subtitle(self, sub_title_content):
        body = []
        body.append('\t<h3>\n')
        body.append(f'\t\t{sub_title_content}\n')
        body.append('\t</h3>\n')
        self.body.append("".join(body))

    def image(self, path, size="300px"):
        body = []
        body.append(f'<a download={path} href={path} title="ImageName"> '
                    f'<img  src={path} width={size} height={size} /></a>\n')
        return "".join(body)

    def curve(self, data, title=None, x_labels=None, font_color="black", width="300px", ):
        body = []
        body.append(self.curveGen.make_curve(data=data, font_color=font_color,
                                             title=title, width=width, x_labels=x_labels))
        self.hasCurveHeader = True
        return "".join(body)

    def text(self, text):
        return text

    def mesh(self, mesh_path, title=""):
        self.hasMeshHeader = True
        return self.meshGen.make_mesh(mesh_path, title)

    def add_table(self, title=""):
        table = Table.Table(title)
        self.body.append(table)
        return table

    def add_confMat(self,  data, rows_titles=None, colums_titles=None, title="Confusion", colormap=None):
        return self.confMatGen.make_confusionmatrix( data, rows_titles, colums_titles, title=title, colormap=colormap)

    def add_dict(self,  data, title="PARAMETERS"):
        self.hasDict = True
        out_string = f"<span class=\"value\">{title} </span></br>\n"
        for key in data.keys():
            out_string += f"<span class=\"key\"> {key} </span> : <span class=\"value\">{data[key]} </span></br>\n"
        return out_string

    def add_css_for_add_dict(self):
        outstring = ""
        outstring += "<style>\n\
              .key {\n\
                color: #2980b9;\n\
                font-weight:bold; \n\
              }\n\
              .value { /* OK, a bit contrived... */\n\
                color: #c0392b;\n\
                font-weight:bold; \n\
                }</style>\n\
            "
        return outstring

if __name__ == '__main__':
    import numpy as np
    webpage = HtmlGenerator(path="test/test.html")
    mydict = {
        "key1": 0,
        "key2": 1,
        "key3": [5,6,7],
        "key4": np.pi,
        "key5": "toto",
        "key6": {"toto":1, "tata":2},
    }
    webpage.add_html_in_body(webpage.add_dict(mydict))
    rows = 20
    cols = 22
    rand_matrix = np.random.randint(-50,50,(rows,cols))/5.0
    # webpage.add_html_in_body(webpage.mesh("test/output_atlas.obj"))
    #
    # import matplotlib.pyplot as plt
    # colormap = plt.get_cmap("nipy_spectral")
    # webpage.add_html_in_body(webpage.add_confMat(rand_matrix, colormap=colormap))
    #
    # webpage.add_html_in_body(webpage.mesh("test/output_atlas.obj"))
    webpage.return_html()
