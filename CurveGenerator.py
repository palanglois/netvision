from os.path import join, dirname

class CurveGenerator:
    def __init__(self):
        self.curve_it = 0
        self.colors = ["#c0392b", " #2980b9", "#27ae60"]
        self.chart_path = join(dirname(__file__), "js/Chart.bundle.min.js")

    def make_header(self):
        with open(self.chart_path, "r") as charjs_file:
            ret_str = "  <script type=\"text/javascript\">\n  " + charjs_file.read().replace("\n", "\n  ")
            ret_str += "Chart.defaults.global.elements.line.fill = false;\n  </script>\n"
            return ret_str

    def make_curve(self, data,
                   font_color="white",
                   title=None,
                   width="100%",
                   x_labels=None):

        out_string = ""

        data_real_dict = {"type": "line",
                          "datasets": [{"data": v, 'label': k,
                                        "xLabels": [x + 1 for x in range(len(data[[x for x in data.keys()][0]]))],
                                        'borderColor': self.colors[i % len(self.colors)]}
                                       for i, (k, v) in enumerate(data.items())]}
        if x_labels is None:
            data_real_dict["labels"] = [x + 1 for x in range(len(data[[x for x in data.keys()][0]]))]
        else:
            data_real_dict["labels"] = x_labels
        mini, maxi = min([min(v) for k, v in data.items()]), max([max(v) for k, v in data.items()])
        scales_dict = {"yAxes": [{"display": "true",
                                  "ticks": {"fontColor": font_color, "suggestedMin": mini, "suggestedMax": maxi}}],
                       "xAxes": [{"ticks": {"autoSkip": 'false', "fontColor": font_color}}]}
        options_dict = {"scales": scales_dict, "legend": {"labels": {"fontColor": font_color}}}
        if title is not None:
            options_dict["title"] = {"display": "false", "text": title, "fontColor": font_color}
        options = str(options_dict)
        out_string += "  <td align=\"center\" width=%s><canvas id=\"line-chart-%i\" " \
                      "width=\"100%%\" height=\"100%%\"></canvas>\n" % (width, self.curve_it)
        ctx = "document.getElementById(\"line-chart-" + str(self.curve_it) + "\")"
        out_string += "  <script>\n"
        out_string += "    var myLineChart = new Chart(%s, {type: 'line', data: %s, options: %s});\n" % \
                      (ctx, str(data_real_dict), options)
        out_string += "    myLineChart.canvas.parentNode.style.width = '%s';\n" % width
        out_string += "  </script>\n"
        out_string += "  </td>\n"
        self.curve_it += 1

        return out_string
