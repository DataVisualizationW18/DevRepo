from extract_data import getRawData
import render_data

parsed_domains = getRawData()

chart = render_data.generate_bar_chart_popularity(parsed_domains[1].libraries)
chart.render_to_file('bar_chart.svg')
chart = render_data.generate_pie_chart_popularity(parsed_domains[1].libraries)
chart.render_to_file('pie_chart.svg')
chart = render_data.generate_xy_chart_issue_closing_time(parsed_domains[1].libraries)
chart.render_to_file('xy_chart.svg')
chart = render_data.generate_box_chart_issue_closing_time(parsed_domains[1].libraries)
chart.render_to_file('box_chart.svg')

chart = render_data.generate_xy_chart_issue_response_time(parsed_domains[1].libraries)
chart.render_to_file('xy_chart_2.svg')
chart = render_data.generate_box_chart_issue_response_time(parsed_domains[1].libraries)
chart.render_to_file('box_chart_2.svg')