import json
from json2html import *

from math import pi

import pandas as pd

from bokeh.io import output_file, show
from bokeh.palettes import Category20c
from bokeh.plotting import figure
from bokeh.transform import cumsum

file_path = "../jsontohtml/test.json"

with open(file_path) as jsonInput:
    data = jsonInput.read().replace('\n', '')
jsonInput.close()


def show():
    output_file("html_table_data.html")

    x = {
        'Passed': 157,
        'Failed': 93,
        'Skipped': 89,
    }

    data = pd.Series(x).reset_index(name='value').rename(columns={'index': 'country'})
    data['angle'] = data['value'] / data['value'].sum() * 2 * pi
    data['color'] = Category20c[len(x)]

    p = figure(plot_height=350, title="Pie Chart", toolbar_location=None,
               tools="hover", x_range=(-0.5, 1.0))

    p.wedge(x=0, y=1, radius=0.4,
            start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
            line_color="white", fill_color='color', legend='country', source=data)

    p.axis.axis_label = None
    p.axis.visible = False
    p.grid.grid_line_color = None

    show(p)


def json_dictionary():
    return json.loads(data)


def return_count_of_tests(what):
    test_summary = json_dictionary()["central testing integration"]["test_summury"]
    return test_summary[what]


def get_total_tests():
    return return_count_of_tests("passed") + return_count_of_tests("failed") + return_count_of_tests("skipped")


print("passed tests")
print(return_count_of_tests("passed"))
print("failed tests")
print(return_count_of_tests("failed"))
print("skipped tests")
print(return_count_of_tests("skipped"))
print("total tests")
print(get_total_tests())


def get_tests_list(what):
    passed_tests = json_dictionary()["central testing integration"][what]
    return passed_tests


def make_html_table_from_passed_tests():
    passed_tests_list = get_tests_list("passed_tests")
    return json2html.convert(json=passed_tests_list)


def make_html_table_from_failed_tests():
    failed_tests_list = get_tests_list("failed_tests")
    return json2html.convert(json=failed_tests_list)


def make_html_table_from_skipped_tests():
    skipped_tests_list = get_tests_list("skipped_tests")
    return json2html.convert(json=skipped_tests_list)


def get_summary():
    summary = json_dictionary()["central testing integration"]["test_summury"]
    return json2html.convert(json=summary)


html_file = open("html_table_data.html", "w")

html_file.writelines("<html>")

html_file.writelines("<body>")

html_file.writelines("<head>")

html_file.writelines("<meta name='viewport' content='width=device-width, initial-scale=1.0'>")

html_file.writelines("<style>")

html_file.writelines(

    ".mainContainer{"
    "margin-top: 170px;"
    "height: auto; "
    "}"

    ".header"
    "{"
    "position: absolute;"
    "width: 100% ;"
    "height: 157px; "
    "left: 0px; "
    "top: 0px; "
    "background: #64A8F0;"
    "display: flex;"
    "justify-content: center;"
    "align-items: center;"
    "}"

    ".reportHeader{"
    "position:" "absolute;"
    "height: 28px;"
    "top: 50px;"
    "font-family: " "monospace; "
    "font-style: " "normal;"
    "font-weight: normal;"
    "font-size: 50px; "
    "line-height: 28px; "
    "color:white;"
    "text-align: center;"
    "display: inline-block;"
    "}"

    "table{"
    "width: 100%;"
    "font-family: " "Trebuchet MS,Arial,Helvetica,sans-serif;"
    "border-collapse: " "collapse;"
    "}"

    "td{"
    "border:" "1px,solid,#ddd;"
    "padding: 8px;"
    "}"

    "tr:nth-child(even)"
    "{background-color: #f2f2f2;"
    "}"

    "tr:hover"
    "{"
    "background-color: #ddd;"
    "}"

    "th {"
    "padding-top: 12px;"
    "padding-bottom: 12px;"
    "text-align: left;"
    "background-color: #64A8F0;"
    "color: white;"
    "}"

    "#rightCheck"
    "{"
    "size: 15px; "
    "color:green;"
    "}"
)

html_file.writelines("</style>")

html_file.writelines("</head>")

html_file.writelines("<div class='header'>")

html_file.writelines("<h1 class='reportHeader'>Central Testing XRay Report</h1>")

html_file.writelines("</div>")

html_file.writelines("<div class='mainContainer'>")

html_file.writelines("<span style='font-size:30px;'>Passed Tests &#9989;</span>")

html_file.write("<div>" + make_html_table_from_passed_tests() + "</div>")

html_file.writelines("<span style='font-size:30px;'>Failed Tests &#10060;</span>")

html_file.write("<div>" + make_html_table_from_failed_tests() + "</div>")

html_file.writelines("<span style='font-size:30px;'> Skipped Tests &#10067;</span>")

html_file.write("<div>" + make_html_table_from_skipped_tests() + "</div>")

html_file.writelines("<span style='font-size:30px;'> Test summary &#9759;</span>")

html_file.write("<div>" + get_summary() + "</div>")

html_file.writelines("</div>")

html_file.writelines("<body>")

html_file.writelines("</html>")

html_file.close()
