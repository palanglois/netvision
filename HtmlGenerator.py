from os.path import join, dirname
import sys
import CurveGenerator
import MeshGenerator

"""
TODO : faire les verif dans HTML type
"""


class Table:
    def __init__(self, title="My-Table"):
        self.hasRow = False
        self.title = title
        self.columns = []
        self.columns.append((self.title, self.type_builder.text))

    def add_column(self, title=None, types=None):
        if self.hasRow:
            print("This table is already defined")
            sys.exit("This table is already defined")

    def add_line(self):
        self.hasRow = True


class HtmlGenerator:
    def __init__(self, path=None):
        self.path = path
        self.head = []
        self.body = []
        self.curveGen = CurveGenerator.CurveGenerator()
        self.meshGen = MeshGenerator.MeshGenerator()
        self.hasCurveHeader = False
        self.hasMeshHeader = False
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

    def return_html(self):
        self.add_javascript_libraries()
        self.body.append(self.meshGen.end_mesh())
        self.body.append("</body>\n")
        self.head.append('</head>\n')

        begin_html = '<!DOCTYPE html>\n<html>\n'
        self.head_str = "".join(self.head)
        self.body_str = "".join(self.body)
        end_html = "</html>\n"
        webpage = begin_html + self.head_str + self.body_str + end_html
        if self.path is not None:
            with open(self.path, 'w') as output_file:
                output_file.write(webpage)
        return webpage

    def make_body(self, title="My Cool Visualization"):
        self.body.append('<body style=\"background-color: lightgrey;\">\n')
        self.body.append('<center>\n')
        self.body.append('\t<div class=\"blank\"></div>\n')
        self.body.append('\t<h1>\n')
        self.body.append(f'\t\t{title}\n')
        self.body.append('\t</h1>\n')
        self.body.append('</center>\n')
        self.body.append('<div class=\"blank\"></div>\n')

    def add_html_in_body(self, html_content):
        """
        :param html_content: html string.
        :return:
        """
        self.body.append(html_content)

    def title(self, title_content):
        body = []
        body.append('\t<h2>\n')
        body.append(f'\t\t{title_content}\n')
        body.append('\t</h2>\n')
        return "".join(body)

    def subtitle(self, sub_title_content):
        body = []
        body.append('\t<h3>\n')
        body.append(f'\t\t{sub_title_content}\n')
        body.append('\t</h3>\n')
        return "".join(body)

    def image(self, path, size="300px"):
        body = []
        body.append(f'<td> <a download={path} href={path} title="ImageName"> '
                    f'<img  src={path} width={size} height={size} /></a></td>\n')
        return "".join(body)

    def curve(self, data, title=None, x_labels=None, font_color="black", width="300px", ):
        body = []
        body.append(self.curveGen.make_curve(data=data, font_color=font_color,
                                             title=title, width=width, x_labels=x_labels))
        self.hasCurveHeader = True
        return "".join(body)

    def text(self, text):
        return text

    def mesh(self, mesh_path, title=None):
        self.hasMeshHeader = True
        return self.meshGen.make_mesh(mesh_path, title)


if __name__ == '__main__':
    webpage = HtmlGenerator(path="test/test.html")
    webpage.add_html_in_body(webpage.mesh("test/output_atlas.obj"))
    webpage.add_html_in_body(webpage.mesh("test/output_atlas.obj"))
    webpage.add_html_in_body(webpage.mesh("test/output_atlas.obj"))
    webpage.add_html_in_body(webpage.mesh("test/output_atlas.obj"))
    webpage.return_html()
