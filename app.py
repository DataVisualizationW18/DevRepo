from flask import Flask, render_template, request, jsonify
import pygal
from pygal.style import Style
from extract_data import getRawData

app = Flask(__name__)

@app.route('/')
def hello_world(name=None):
    #parsed_domains = getRawData()

    domain_list = {
        "": [],
        "cryptography": ["bouncycastle","commons crypto","conceal","chimera","spongycastle","keyczar","conscrypt"],
        "databases": ["h2","derby"],
        "json": ["gson","json.simple"],
        "logging": ["slf4j","log4j2","logback","commons logging","tinylog","blitz4j","minlog"],
        "mocking": ["mockito","easymock","powermock","jmock"],
        "object-relational-mapping": ["hibernate orm","mybatis3","ormlite"],
        "security": ["shiro","spring security"],
        "testing": ["junit4","testng"],
        "utilities": ["guava","commons lang"],
        "xml": ["xerces2-j","dom4j","jdom"]
    }

    chart_types = {
        "popularity" : [
            "bar_raw",
            "pie",
            "gauge",
            "raw_data"
        ],
        "release-frequency" : [
            "bar_avg",
            "box",
            "raw_data"
        ],
        "last-modification-date" : [
            "bar_days",
            "raw_data"
        ],
        "performance" : [
            "gauge",
            "box",
            "raw_data"
        ],
        "security" : [
            "gauge",
            "box",
            "raw_data"
        ],
        "issue-response-time" : [
            "xy",
            "box",
            "raw_data"
        ],
        "issue-closing-time" : [
            "xy",
            "box",
            "raw_data"
        ],
        "backwards-compatibility" : [
            "bar",
            "line",
            "raw_data"
        ],
        "last-discussed-on-so" : [
            "box",
            "scatter",
            "raw_data"
        ]
    }

    return render_template('index.html',domain_list=domain_list, chart_types=chart_types)


@app.route('/generate_chart', methods=['POST'])
def handle_data():
    chart_types = {
        "popularity" : [
            "bar_raw",
            "pie",
            "gauge"
        ],
        "release-frequency" : [
            "bar_avg",
            "box"
        ],
        "last-modification-date" : [
            "bar_days"
        ],
        "performance" : [
            "gauge",
            "box"
        ],
        "security" : [
            "gauge",
            "box"
        ],
        "issue-response-time" : [
            "xy",
            "box"
        ],
        "issue-closing-time" : [
            "xy",
            "box"
        ],
        "backwards-compatibility" : [
            "bar",
            "line"
        ],
        "last-discussed-on-so" : [
            "box",
            "scatter"
        ]
    }

    print(request.json)

    invisBackground_style = Style(background='transparent')

    line_chart = pygal.Bar(style = invisBackground_style, width=600)
    line_chart.title = 'Browser usage evolution (in %)'
    line_chart.x_labels = map(str, range(2002, 2013))
    line_chart.add('Firefox', [None, None, 0, 16.6, 25, 31, 36.4, 45.5, 46.3, 42.8, 37.1])
    line_chart.add('Chrome',  [None, None, None, None, None, None, 0, 3.9, 10.8, 23.8, 35.3])
    line_chart.add('IE',      [85.8, 84.6, 84.7, 74.5, 66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
    line_chart.add('Others',  [14.2, 15.4, 15.3, 8.9, 9, 10.4, 8.9, 5.8, 6.7, 6.8, 7.5])
    chart = line_chart.render_data_uri()

    line_chart2 = pygal.Bar(style = invisBackground_style, width=1200)
    line_chart2.title = 'Browser usage evolution (in %)'
    line_chart2.x_labels = map(str, range(2002, 2013))
    line_chart2.add('Firefox', [None, None, 0, 16.6, 25, 31, 36.4, 45.5, 46.3, 42.8, 37.1])
    line_chart2.add('Chrome',  [None, None, None, None, None, None, 0, 3.9, 10.8, 23.8, 35.3])
    line_chart2.add('IE',      [85.8, 84.6, 84.7, 74.5, 66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
    line_chart2.add('Others',  [14.2, 15.4, 15.3, 8.9, 9, 10.4, 8.9, 5.8, 6.7, 6.8, 7.5])
    chart2 = line_chart2.render_data_uri()

    charts = []
    charts.append({
        "metric": "popularity",
        "type": "chart",
        "data": chart,
        "chart_type": "bar_raw"
    });
    charts.append({
        "metric": "performance",
        "type": "chart",
        "data": chart,
        "chart_type": "box"
    });
    charts.append({
        "metric": "issue-closing-time",
        "type": "chart",
        "data": chart2,
        "chart_type": "xy"
    });
    charts.append({
        "metric": "security",
        "type": "raw_data",
        "data": "",
        "chart_type": "raw_data"
    });

    return jsonify(charts)


@app.route('/generate_one_chart', methods=['POST'])
def handle_one_data():
    chart_types = {
        "popularity" : [
            "bar_raw",
            "pie",
            "gauge"
        ],
        "release-frequency" : [
            "bar_avg",
            "box"
        ],
        "last-modification-date" : [
            "bar_days"
        ],
        "performance" : [
            "gauge",
            "box"
        ],
        "security" : [
            "gauge",
            "box"
        ],
        "issue-response-time" : [
            "xy",
            "box"
        ],
        "issue-closing-time" : [
            "xy",
            "box"
        ],
        "backwards-compatibility" : [
            "bar",
            "line"
        ],
        "last-discussed-on-so" : [
            "box",
            "scatter"
        ]
    }

    invisBackground_style = Style(background='transparent')

    line_chart = pygal.Bar(style = invisBackground_style, width=600)
    line_chart.title = 'Browser usage evolution (in %)'
    line_chart.x_labels = map(str, range(2002, 2013))
    line_chart.add('Firefox', [None, None, 0, 16.6, 25, 31, 36.4, 45.5, 46.3, 42.8, 37.1])
    line_chart.add('IE',      [85.8, 84.6, 84.7, 74.5, 66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
    line_chart.add('Others',  [14.2, 15.4, 15.3, 8.9, 9, 10.4, 8.9, 5.8, 6.7, 6.8, 7.5])
    chart = line_chart.render_data_uri()

    print(request.json)

    return jsonify({
        "metric": "popularity",
        "type": "chart",
        "data": chart,
        "chart_type": "bar_raw"
    })
