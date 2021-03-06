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

    readable_metrics = {
        "popularity": "Popularity",
        "release-frequency": "Release Frequency",
        "last-modification-date": "Last Modification Date",
        "performance": "Performance",
        "security": "Security",
        "issue-response-time": "Issue Response Time",
        "issue-closing-time": "Issue Closing Time",
        "backwards-compatibility": "Backwards Compatibility",
        "last-discussed-on-so": "Last Discussed On Stack Overflow"
    }

    chart_types = {
        "popularity" : [
            {
                "key":"bar_raw",
                "readable":"Bar Chart"
            }, {
                "key":"pie",
                "readable":"Pie Chart"
            }, {
                "key":"gauge",
                "readable":"Solid Gauge"
            }, {
                "key":"raw_data",
                "readable":"Raw Data"
            }
        ],
        "release-frequency" : [
            {
                "key":"bar_avg",
                "readable":"Bar Chart"
            }, {
                "key":"box",
                "readable":"Box Plot"
            }, {
                "key":"raw_data",
                "readable":"Raw Data"
            }
        ],
        "last-modification-date" : [
            {
                "key":"bar_days",
                "readable":"Bar Chart"
            }, {
                "key":"raw_data",
                "readable":"Raw Data"
            }
        ],
        "performance" : [
            {
                "key":"gauge",
                "readable":"Solid Gauge"
            }, {
                "key":"box",
                "readable":"Box Plot"
            }, {
                "key":"raw_data",
                "readable":"Raw Data"
            }
        ],
        "security" : [
            {
                "key":"gauge",
                "readable":"Solid Gauge"
            }, {
                "key":"box",
                "readable":"Box Plot"
            }, {
                "key":"raw_data",
                "readable":"Raw Data"
            }
        ],
        "issue-response-time" : [
            {
                "key":"xy",
                "readable":"Scatter Plot"
            }, {
                "key":"box",
                "readable":"Box Plot"
            }, {
                "key":"raw_data",
                "readable":"Raw Data"
            }
        ],
        "issue-closing-time" : [
            {
                "key":"xy",
                "readable":"Scatter Plot"
            }, {
                "key":"box",
                "readable":"Box Plot"
            }, {
                "key":"raw_data",
                "readable":"Raw Data"
            }
        ],
        "backwards-compatibility" : [
            {
                "key":"bar",
                "readable":"Bar Chart"
            }, {
                "key":"line",
                "readable":"Line Graph"
            }, {
                "key":"raw_data",
                "readable":"Raw Data"
            }
        ],
        "last-discussed-on-so" : [
            {
                "key":"box",
                "readable":"Box Plot"
            }, {
                "key":"scatter",
                "readable":"Scatter Plot"
            }, {
                "key":"raw_data",
                "readable":"Raw Data"
            }
        ]
    }

    default_dict={'popularity': 'bar_raw',
                    'release-frequency':'bar_avg',
                    'last-modification-date':'bar_days',
                    'performance':'box',
                    'security':'box',
                    'issue-response-time':'xy',
                    'issue-closing-time':'xy',
                    'backwards-compatibility':'bar',
                    'last-discussed-on-so':'box'}

    return render_template('index.html',domain_list=domain_list, domain_dict=domain_dict, chart_types=chart_types, default_dict=default_dict, readable_metrics=readable_metrics)

# Handles generating a list of charts
@app.route('/generate_chart', methods=['POST'])
def handle_data():
    global parsed_domains

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
        chart_dict = {
            'metric':metric['metric'],
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
        if(metric_dict['read_only']):
            chart = chart.render_data_uri(force_uri_protocol='')
        else:
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
