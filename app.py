from flask import Flask, render_template, request, jsonify
import pygal
from pygal.style import Style
from extract_data import getRawData
from render_data import generate
from generate_table import generate_table

app = Flask(__name__)
parsed_domains = None

@app.route('/')
def hello_world(name=None):
    global parsed_domains
    parsed_domains = getRawData()

    domain_list = ["",
                   "cryptography",
                   "databases",
                   "json",
                   "logging",
                   "mocking",
                   "object-relational mapping",
                   "security",
                   "testing",
                   "utilities",
                   "xml"]

    domain_dict = {
        "": [],
        "cryptography": ["bouncycastle","commons crypto","conceal","chimera","spongycastle","keyczar","conscrypt"],
        "databases": ["h2","derby"],
        "json": ["gson","json.simple"],
        "logging": ["slf4j","log4j2","logback","commons logging","tinylog","blitz4j","minlog"],
        "mocking": ["mockito","easymock","powermock","jmock"],
        "object-relational mapping": ["hibernate orm","mybatis3","ormlite"],
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

    return render_template('index.html',domain_list=domain_list, domain_dict=domain_dict, chart_types=chart_types)

# Handles generating a list of charts
@app.route('/generate_chart', methods=['POST'])
def handle_data():
    global parsed_domains
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

    # Gets the Domain, Library, and Metrics selected in the CSS form
    metric_dict = request.json

    # Dictionary that maps metrics to their default chart type
    default_dict={'popularity': 'bar_raw',
                    'release-frequency':'bar_avg',
                    'last-modification-date':'bar_days',
                    'performance':'box',
                    'security':'box',
                    'issue-response-time':'xy',
                    'issue-closing-time':'xy',
                    'backwards-compatibility':'bar',
                    'last-discussed-on-so':'box'}

    # Generate a chart for each metric
    charts=[]
    for metric in metric_dict['metrics']:

        # Get the library objects corresponding to the libraries selected in the CSS form
        lib_list=[]
        for domain in parsed_domains:
            if domain.name == metric_dict['domain']:
                for library in domain.libraries:
                    if library.name in metric_dict['libraries']:
                        lib_list.append(library)

        # Depending on chart type make a table or a chart
        if metric['chart_type'] == 'raw_data':
            chart = generate_table(lib_list, metric['metric'])
            vis_type = 'raw_data'

        else:
            chart = generate(lib_list, metric['metric'], metric['chart_type'])
            vis_type = 'chart'
            chart = chart.render_data_uri()

        # Check if it is the default chart
        def_chart= metric['chart_type']
        if def_chart == 'default':
            def_chart = default_dict[metric['metric']]

        # Chart dictionary with chart and chart info
        chart_dict = {'metric':metric['metric'],
        'type':vis_type,
        'data': chart,
        'chart_type': def_chart
        }

        charts.append(chart_dict)

    # Pass the charts and chart info back to the CSS
    return jsonify(charts)

# Handles generating a single chart, effectively the same as handle_data()
@app.route('/generate_one_chart', methods=['POST'])
def handle_one_data():
    global parsed_domains
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


    metric_dict = request.json
    default_dict={'popularity': 'bar_raw',
                    'release-frequency':'bar_avg',
                    'last-modification-date':'bar_days',
                    'performance':'box',
                    'security':'box',
                    'issue-response-time':'xy',
                    'issue-closing-time':'xy',
                    'backwards-compatibility':'bar',
                    'last-discussed-on-so':'box'}

    metric_dict = request.json
    metric = metric_dict['metric']

    lib_list=[]
    for domain in parsed_domains:
        if domain.name == metric_dict['domain']:
            for library in domain.libraries:
                if library.name in metric_dict['libraries']:
                    lib_list.append(library)

    if metric['chart_type'] == 'raw_data':
        chart = generate_table(lib_list, metric['metric'])
        vis_type = 'raw_data'
    else:
        chart = generate(lib_list, metric['metric'], metric['chart_type'])
        vis_type = 'chart'
        chart = chart.render_data_uri()

    def_chart= metric['chart_type']
    if def_chart == 'default':
        def_chart = default_dict[metric['metric']]

    chart_dict = {'metric':metric['metric'],
        'type':vis_type,
        'data': chart,
        'chart_type': def_chart
        }

    return jsonify(chart_dict)
