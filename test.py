from extract_data import getRawData
import render_data

parsed_domains = getRawData()

# popularity has bar, pie and gauge
# chart = render_data.generate_bar_chart_popularity(parsed_domains[1].libraries)
# chart.render_to_file('bar_chart.svg')
# chart = render_data.generate_pie_chart_popularity(parsed_domains[1].libraries)
# chart.render_to_file('pie_chart.svg')
# chart = render_data.generate_solid_gauge_chart_popularity(parsed_domains[1].libraries)
# chart.render_to_file('gauge_chart.svg')

# release frequency has box and bar
# chart = render_data.generate_box_chart_release_frequency(parsed_domains[1].libraries)
# chart.render_to_file('box_chart_3.svg')
# chart = render_data.generate_bar_chart_release_frequency(parsed_domains[1].libraries)
# chart.render_to_file('bar_chart_3.svg')
chart = render_data.generate_line_chart_release_frequency(parsed_domains[1].libraries)
chart.render_to_file('line_chart_2.svg')

# last modification date has bar
# chart = render_data.generate_bar_chart_last_modification(parsed_domains[1].libraries)
# chart.render_to_file('bar_chart_4.svg')

# performance has box, gauge and bar
# chart = render_data.generate_bar_chart_performance(parsed_domains[1].libraries)
# chart.render_to_file('bar_chart_5.svg')
# chart = render_data.generate_box_chart_performance(parsed_domains[1].libraries)
# chart.render_to_file('box_chart_4.svg')
# chart = render_data.generate_solid_gauge_chart_performance(parsed_domains[1].libraries)
# chart.render_to_file('gauge_chart_2.svg')

# security has box, gauge and bar
# chart = render_data.generate_bar_chart_security(parsed_domains[1].libraries)
# chart.render_to_file('bar_chart_6.svg')
# chart = render_data.generate_box_chart_security(parsed_domains[1].libraries)
# chart.render_to_file('box_chart_5.svg')
# chart = render_data.generate_solid_gauge_chart_security(parsed_domains[1].libraries)
# chart.render_to_file('gauge_chart_3.svg')

# issue closing time has xy and box
# chart = render_data.generate_xy_chart_issue_closing_time(parsed_domains[1].libraries)
# chart.render_to_file('xy_chart.svg')
# chart = render_data.generate_box_chart_issue_closing_time(parsed_domains[1].libraries)
# chart.render_to_file('box_chart.svg')

# issue response time has xy and box
# chart = render_data.generate_xy_chart_issue_response_time(parsed_domains[1].libraries)
# chart.render_to_file('xy_chart_2.svg')
# chart = render_data.generate_box_chart_issue_response_time(parsed_domains[1].libraries)
# chart.render_to_file('box_chart_2.svg')

# backwards compatability has bar and box
# chart = render_data.generate_bar_chart_backwards_compatibility(parsed_domains[1].libraries)
# chart.render_to_file('bar_chart_7.svg')
# chart = render_data.generate_box_chart_backwards_compatibility(parsed_domains[1].libraries)
# chart.render_to_file('box_chart_6.svg')
# chart = render_data.generate_line_chart_backwards_compatibility(parsed_domains[1].libraries)
# chart.render_to_file('line_chart_1.svg')

# last discussed on stack overflow has bar and box
# chart = render_data.generate_bar_chart_last_discussed(parsed_domains[1].libraries)
# chart.render_to_file('bar_chart_8.svg')
# chart = render_data.generate_box_chart_last_discussed(parsed_domains[1].libraries)
# chart.render_to_file('box_chart_7.svg')
# chart = render_data.generate_scatter_chart_last_discussed(parsed_domains[1].libraries)
# chart.render_to_file('scatter_chart_1.svg')