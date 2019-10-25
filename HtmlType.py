class HtmlType:
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
        body.append(f'<td> <a download={path} href={path} title="ImageName"> <img  src={path} width={size} height={size} /></a></td>\n')
        return "".join(body)

    def curve(self, data, title = None, x_labels = None , font_color = "black", width = "300px", ):
        body = []
        body.append(self.curveGen.make_curve(data=data, font_color=font_color, title=title, width=width, x_labels=x_labels))
        self.hasCurveHeader = True
        return "".join(body)

    def text(self, text):
        return text


    def mesh(self, mesh_path, title = None):