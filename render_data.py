import pygal
from datetime import datetime, date
from pygal.style import Style

invis_style = Style(background = 'transparent')

def generate(libraries, metric, chart_type):
	# default for chart_type is default chart to be created
	chart = None
	if metric == 'popularity':

		if chart_type == 'default' or chart_type == 'bar_raw':
			chart = generate_bar_chart_popularity(libraries)
		elif chart_type == 'pie':
			chart = generate_pie_chart_popularity(libraries)
		elif chart_type == 'gauge':
			chart = generate_solid_gauge_chart_popularity(libraries)

	elif metric == 'release-frequency':

		if chart_type == 'default' or chart_type == 'bar_avg':
			chart = generate_bar_chart_release_frequency(libraries)
		elif chart_type == 'box':
			chart = generate_box_chart_release_frequency(libraries)
		elif chart_type == 'line':
			chart = generate_line_chart_release_frequency(libraries)

	elif metric == 'last-modification-date':

		if chart_type == 'default' or chart_type == 'bar_days':
			chart = generate_bar_chart_last_modification(libraries)

	elif metric == 'performance':

		if chart_type == 'default' or chart_type == 'box':
			chart = generate_box_chart_performance(libraries)
		elif chart_type == 'gauge':
			chart = generate_solid_gauge_chart_popularity(libraries)

	elif metric == 'security':

		if chart_type == 'default' or chart_type == 'box':
			chart = generate_box_chart_security(libraries)
		elif chart_type == 'gauge':
			chart = generate_solid_gauge_chart_security(libraries)

	elif metric == 'issue-response-time':

		if chart_type == 'default' or chart_type == 'xy':
			chart = generate_xy_chart_issue_response_time(libraries)
		elif chart_type == 'box':
			chart = generate_box_chart_issue_response_time(libraries)

	elif metric == 'issue-closing-time':

		if chart_type == 'default' or chart_type == 'xy':
			chart = generate_xy_chart_issue_closing_time(libraries)
		elif chart_type == 'box':
			chart = generate_box_chart_issue_closing_time(libraries)

	elif metric == 'backwards-compatibility':

		if chart_type == 'default' or chart_type == 'bar':
			chart = generate_bar_chart_backwards_compatibility(libraries)
		elif chart_type == 'line':
			chart = generate_line_chart_backwards_compatibility(libraries)

	elif metric == 'last-discussed-on-so':

		if chart_type == 'default' or chart_type == 'box':
			chart = generate_box_chart_last_discussed(libraries)
		elif chart_type == 'scatter':
			chart = generate_scatter_chart_last_discussed(libraries)


	return chart

# popularity
def generate_bar_chart_popularity(libraries):
	bar_chart = pygal.Bar(title = 'Number Of Software Projects Making Use Of The Library' , x_title='', y_title='', x_label_rotation = -45, style = invis_style)
	sorted_libraries = sorted(libraries, key=lambda library: library.popularity, reverse=True)
	for library in sorted_libraries:
		bar_chart.add(library.name, library.popularity)
	return bar_chart

def generate_pie_chart_popularity(libraries):
	pie_chart = pygal.Pie(title = 'Number Of Software Projects Making Use Of The Library', x_title='', y_title='', x_label_rotation = -45, style = invis_style)
	sorted_libraries = sorted(libraries, key=lambda library: library.popularity, reverse=True)
	for library in sorted_libraries:
		pie_chart.add(library.name, library.popularity)
	return pie_chart

def generate_solid_gauge_chart_popularity(libraries):
	gauge_chart = pygal.SolidGauge(title = 'Number Of Software Projects Making Use Of The Library', x_title='', y_title='', x_label_rotation = -45, style = invis_style)
	sorted_libraries = sorted(libraries, key=lambda library: library.popularity, reverse=True)
	top_popularity = 0
	for library in sorted_libraries:
		if library.popularity > top_popularity:
			top_popularity = library.popularity

	for library in sorted_libraries:
		gauge_chart.add(library.name, [{'value':library.popularity, 'max_value':top_popularity}])
	return gauge_chart

# release frequency
def generate_bar_chart_release_frequency(libraries):
	bar_chart = pygal.Bar(title = 'Average Days Between Releases', x_title='', y_title='Days', x_label_rotation = -45, style = invis_style)
	
	all_release_times = []
	release_tuples = []
	for library in libraries:
		release_times = []
		for i in range(len(library.release_frequency) - 1):
			f_date = date(library.release_frequency[i].year, library.release_frequency[i].month, library.release_frequency[i].day)
			l_date = date(library.release_frequency[i + 1].year, library.release_frequency[i + 1].month, library.release_frequency[i + 1].day)
			time_to_release_all = l_date - f_date
			time_to_release = time_to_release_all.days
			release_times.append(time_to_release)

		avg_release_time = sum(release_times)/len(release_times)
		release_tuples.append((avg_release_time, len(release_times), library.name))
		# bar_chart.add(library.name, avg_release_time)
		# all_release_times.append(library.name + ': ' + str(len(release_times)))
	sorted_release_tuples = sorted(release_tuples, key=lambda release: release[0], reverse=False)
	for release_tuple in sorted_release_tuples:
		bar_chart.add(release_tuple[2], release_tuple[0])
		all_release_times.append(release_tuple[2] + ': ' + str(release_tuple[1]))
	# bar_chart.x_labels = all_release_times
	return bar_chart

def generate_box_chart_release_frequency(libraries):
	box_chart = pygal.Box(title = 'Days Between Releases', x_title='Total Releases', y_title='Days', x_label_rotation = -45, style = invis_style)
	
	all_release_times = []
	release_tuples = []
	for library in libraries:
		release_times = []
		for i in range(len(library.release_frequency) - 1):
			f_date = date(library.release_frequency[i].year, library.release_frequency[i].month, library.release_frequency[i].day)
			l_date = date(library.release_frequency[i + 1].year, library.release_frequency[i + 1].month, library.release_frequency[i + 1].day)
			time_to_release_all = l_date - f_date
			time_to_release = time_to_release_all.days
			release_times.append(time_to_release)

		avg_release_time = sum(release_times)/len(release_times)
		release_tuples.append((release_times, avg_release_time, len(release_times), library.name))
		# box_chart.add(library.name, release_times)
		# all_release_times.append(library.name + ': ' + str(len(release_times)))

	sorted_release_tuples = sorted(release_tuples, key=lambda release: release[1], reverse=False)
	for release_tuple in sorted_release_tuples:
		box_chart.add(release_tuple[3], release_tuple[0])
		all_release_times.append(release_tuple[3] + ': ' + str(release_tuple[2]))

	box_chart.x_labels = all_release_times
	return box_chart

def generate_line_chart_release_frequency(libraries):
	line_chart = pygal.Line(title = 'Average Days Between Releases', x_title='Release', y_title='Days', x_label_rotation = -45, style = invis_style)
	all_release_times = []
	for library in libraries:
		release_times = []
		for i in range(len(library.release_frequency) - 1):
			f_date = date(library.release_frequency[i].year, library.release_frequency[i].month, library.release_frequency[i].day)
			l_date = date(library.release_frequency[i + 1].year, library.release_frequency[i + 1].month, library.release_frequency[i + 1].day)
			time_to_release_all = l_date - f_date
			time_to_release = time_to_release_all.days
			release_times.append(time_to_release)

		line_chart.add(library.name, release_times)
		all_release_times.append(library.name + ': ' + str(len(release_times)))
	# line_chart.x_labels = all_release_times
	return line_chart

# last modification date
def generate_bar_chart_last_modification(libraries):
	bar_chart = pygal.Bar(title = 'Days Since Last Release', x_title='', y_title='Days', x_label_rotation = -45, style = invis_style)

	now = datetime.now()
	days_from_release = []
	for library in libraries:
		f_date = date(library.last_modification_date.year, library.last_modification_date.month, library.last_modification_date.day)
		l_date = date(now.year, now.month, now.day)
		time_from_release_all = l_date - f_date
		time_from_release = time_from_release_all.days
		days_from_release.append((time_from_release, library.name))

	sorted_days_from_release = sorted(days_from_release, key=lambda library: library[0], reverse=False)

	for library in sorted_days_from_release:
		bar_chart.add(library[1], library[0])

	return bar_chart

# performance
def generate_bar_chart_performance(libraries):
	bar_chart = pygal.Bar(range=(0,1), title = 'Percentage Of Total Performance Related Issues',  x_title='', y_title='Percentage', x_label_rotation = -45, style = invis_style)

	count = 0
	unsorted_list = []
	for library in libraries:
		for issue in library.issue_data:
			if issue.performance_issue == 'Yes':
				count += 1
		unsorted_list.append((count/len(library.issue_data), library.name))
		count = 0

	sorted_list = sorted(unsorted_list, key=lambda library: library[0], reverse=False)

	for library in sorted_list:
		bar_chart.add(library[1], library[0])

	return bar_chart

def generate_box_chart_performance(libraries):
	box_chart = pygal.Box(range=(0,1), title = 'Percentage Of Total Performance Related Issues', x_title='Total Performance Issues', y_title='Percentage', x_label_rotation = -45, style = invis_style)

	count = 0
	unsorted_list = []
	for library in libraries:
		for issue in library.issue_data:
			if issue.performance_issue == 'Yes':
				count += 1
		unsorted_list.append((count/len(library.issue_data), library.name, count))
		count = 0

	sorted_list = sorted(unsorted_list, key=lambda library: library[0], reverse=False)

	labels = []
	for library in sorted_list:
		box_chart.add(library[1], library[0])
		labels.append(library[1] + ': ' + str(library[2]))

	box_chart.x_labels = labels
	return box_chart

def generate_solid_gauge_chart_performance(libraries):
	gauge_chart = pygal.SolidGauge(title = 'Percentage Of Total Performance Related Issues', x_title='', y_title='', x_label_rotation = -45, style = invis_style)
	
	count = 0
	unsorted_list = []
	for library in libraries:
		for issue in library.issue_data:
			if issue.performance_issue == 'Yes':
				count += 1
		unsorted_list.append((count/len(library.issue_data), library.name, count))
		count = 0

	sorted_list = sorted(unsorted_list, key=lambda library: library[0], reverse=False)

	for library in sorted_list:
		gauge_chart.add(library[1], [{'value':library[0], 'max_value':1}])

	return gauge_chart


# security
def generate_bar_chart_security(libraries):
	bar_chart = pygal.Bar(range=(0,1), title = 'Percentage Of Total Security Related Issues', x_title='', y_title='Percentage', x_label_rotation = -45, style = invis_style)

	count = 0
	unsorted_list = []
	for library in libraries:
		for issue in library.issue_data:
			if issue.security_issue == 'Yes':
				count += 1
		unsorted_list.append((count/len(library.issue_data), library.name))
		count = 0

	sorted_list = sorted(unsorted_list, key=lambda library: library[0], reverse=False)

	for library in sorted_list:
		bar_chart.add(library[1], library[0])

	return bar_chart

def generate_box_chart_security(libraries):
	box_chart = pygal.Box(range=(0,1), title = 'Percentage Of Total Security Related Issues', x_title='Total Security Issues', y_title='Percentage', x_label_rotation = -45, style = invis_style)

	count = 0
	unsorted_list = []
	for library in libraries:
		for issue in library.issue_data:
			if issue.security_issue == 'Yes':
				count += 1
		unsorted_list.append((count/len(library.issue_data), library.name, count))
		count = 0

	sorted_list = sorted(unsorted_list, key=lambda library: library[0], reverse=False)

	labels = []
	for library in sorted_list:
		box_chart.add(library[1], library[0])
		labels.append(library[1] + ': ' + str(library[2]))

	box_chart.x_labels = labels
	return box_chart

def generate_solid_gauge_chart_security(libraries):
	gauge_chart = pygal.SolidGauge(title = 'Percentage Of Total Security Related Issues', x_title='', y_title='', x_label_rotation = -45, style = invis_style)
	
	count = 0
	unsorted_list = []
	for library in libraries:
		for issue in library.issue_data:
			if issue.security_issue == 'Yes':
				count += 1
		unsorted_list.append((count/len(library.issue_data), library.name, count))
		count = 0

	sorted_list = sorted(unsorted_list, key=lambda library: library[0], reverse=False)

	for library in sorted_list:
		gauge_chart.add(library[1], [{'value':library[0], 'max_value':1}])

	return gauge_chart

# issue closing time
def generate_xy_chart_issue_closing_time(libraries):
	xy_chart = pygal.XY(dots_size=4, range=(0,1), title = 'Average Time To Close An Issue vs Percentage of Issues Not Closed', x_title='Average Days To Close Issue', y_title='Percentage Of Issues Closed', x_label_rotation = -45, style = invis_style)
	for library in libraries:
		issue_count = len(library.issue_data)
		not_responded_count = 0
		response_times = []
		num_of_issues = 0
		for issue in library.issue_data:
			if issue.issue_closing_date == None:
				not_responded_count += 1
			else:
				response_times.append(issue.time_to_close)
			num_of_issues += 1

		avg = sum(response_times) / len(response_times)
		per = not_responded_count / num_of_issues
		xy_chart.add(library.name, [(avg, per)] )
	return xy_chart

def generate_box_chart_issue_closing_time(libraries):
	box_chart = pygal.Box(title = 'Days Taken To Close Issue', x_title='Total Issues Closed', y_title='Days', x_label_rotation = -45, style = invis_style)
	all_response_times = []
	for library in libraries:
		response_times = []
		for issue in library.issue_data:
			if issue.issue_closing_date != None:
				response_times.append(issue.time_to_close)

		box_chart.add(library.name, response_times)
		all_response_times.append(library.name + ': ' + str(len(response_times)))
	box_chart.x_labels = all_response_times
	return box_chart

# issue response time
def generate_xy_chart_issue_response_time(libraries):
	xy_chart = pygal.XY(dots_size=4, range=(0,1), title = 'Average Time To Respond To An Issue vs Percentage of Issues Not Responded To' , x_title='Average Days To Response', y_title='Percentage of Issues Not Responded To', x_label_rotation = -45, style = invis_style)
	for library in libraries:
		issue_count = len(library.issue_data)
		not_responded_count = 0
		response_times = []
		num_of_issues = 0
		for issue in library.issue_data:
			if issue.date_of_first_comment == None:
				not_responded_count += 1
			else:
				response_times.append(issue.time_to_response)
			num_of_issues += 1

		avg = sum(response_times) / len(response_times)
		per = not_responded_count / num_of_issues
		xy_chart.add(library.name, [(avg, per)] )
	return xy_chart

def generate_box_chart_issue_response_time(libraries):
	box_chart = pygal.Box(title = 'Days Taken To Respond To Issue', x_title='Total Issues Responsed To', y_title='Days', x_label_rotation = -45, style = invis_style)
	all_response_times = []
	for library in libraries:
		response_times = []
		for issue in library.issue_data:
			if issue.issue_closing_date != None:
				response_times.append(issue.time_to_response)

		box_chart.add(library.name, response_times )
		all_response_times.append(library.name + ': ' + str(len(response_times)))
	box_chart.x_labels = all_response_times
	return box_chart

# backwards compatability
def generate_bar_chart_backwards_compatibility(libraries):
	bar_chart = pygal.Bar(title = 'Average Number Of Breaking Changes Per Version', x_title='', y_title='', x_label_rotation = -45, style = invis_style)

	unsorted_list = []
	for library in libraries:
		unsorted_list.append((sum(library.backward_compatibilty)/len(library.backward_compatibilty), library.name))


	sorted_list = sorted(unsorted_list, key=lambda library: library[0], reverse=False)

	for library in sorted_list:
		bar_chart.add(library[1], library[0])

	return bar_chart

def generate_box_chart_backwards_compatibility(libraries):
	box_chart = pygal.Box(title = 'Number Of Breaking Changes Per Version', x_title='Total Number Of Versions', y_title='', x_label_rotation = -45, style = invis_style)

	labels = []
	for library in libraries:
		box_chart.add(library.name, library.backward_compatibilty)
		labels.append(library.name + ': ' + str(len(library.backward_compatibilty)))

	box_chart.x_labels = labels
	return box_chart

def generate_line_chart_backwards_compatibility(libraries):
	line_chart = pygal.Line(title = 'Number Of Breaking Changes Per Version', x_title='Version', y_title='Number Of Breaking Changes', x_label_rotation = -45, style = invis_style)

	for library in libraries:
		line_chart.add(library.name, library.backward_compatibilty)

	return line_chart

# last discussed on stack overflow
def generate_bar_chart_last_discussed(libraries):
	bar_chart = pygal.Bar(title = 'Days Since Last Discussed On Stack Overflow', x_title='', y_title='Days', x_label_rotation = -45, style = invis_style)

	now = datetime.now()
	days_from_release = []
	for library in libraries:
		if library.last_discussed_on_stack_overflow[0] != None:
			f_date = date(library.last_discussed_on_stack_overflow[0].year, library.last_discussed_on_stack_overflow[0].month, library.last_discussed_on_stack_overflow[0].day)
			l_date = date(now.year, now.month, now.day)
			time_from_release_all = l_date - f_date
			time_from_release = time_from_release_all.days
			days_from_release.append((time_from_release, library.name))


	sorted_days_from_release = sorted(days_from_release, key=lambda library: library[0], reverse=False)

	for library in sorted_days_from_release:
		bar_chart.add(library[1], library[0])

	return bar_chart

def generate_box_chart_last_discussed(libraries):
	box_chart = pygal.Box(title = 'Days Since Last Discussed On Stack Overflow', x_title='Total Discussions', y_title='', x_label_rotation = -45, style = invis_style)

	now = datetime.now()
	unsorted_list = []
	for library in libraries:
		if library.last_discussed_on_stack_overflow[0] != None:
			f_date = date(library.last_discussed_on_stack_overflow[0].year, library.last_discussed_on_stack_overflow[0].month, library.last_discussed_on_stack_overflow[0].day)
			l_date = date(now.year, now.month, now.day)
			time_from_release_all = l_date - f_date
			time_from_release = time_from_release_all.days
			unsorted_list.append((time_from_release, time_from_release, library.name, library.last_discussed_on_stack_overflow[1]))
		else:
			unsorted_list.append(([], 0, library.name, library.last_discussed_on_stack_overflow[1]))

	sorted_list = sorted(unsorted_list, key=lambda library: library[1], reverse=False)

	labels = []
	for library in sorted_list:
		box_chart.add(library[2], library[0])
		labels.append(library[2] + ': ' + str(library[3]))

	box_chart.x_labels = labels
	return box_chart

def generate_scatter_chart_last_discussed(libraries):
	xy_chart = pygal.XY(dots_size=4, stroke = False, title = 'Days Since Last Discussed On Stack Overflow', x_title='Days', y_title='Total Discussions', x_label_rotation = -45, style = invis_style)

	now = datetime.now()
	unsorted_list = []
	for library in libraries:
		if library.last_discussed_on_stack_overflow[0] != None:
			f_date = date(library.last_discussed_on_stack_overflow[0].year, library.last_discussed_on_stack_overflow[0].month, library.last_discussed_on_stack_overflow[0].day)
			l_date = date(now.year, now.month, now.day)
			time_from_release_all = l_date - f_date
			time_from_release = time_from_release_all.days
			unsorted_list.append((time_from_release, library.name, library.last_discussed_on_stack_overflow[1]))
		else:
			unsorted_list.append((0, library.name, library.last_discussed_on_stack_overflow[1]))

	sorted_list = sorted(unsorted_list, key=lambda library: library[1], reverse=False)

	labels = []
	for library in sorted_list:
		xy_chart.add(library[1], [(library[0], library[2])])
		labels.append(library[1] + ': ' + str(library[2]))

	# xy_chart.x_labels = labels
	return xy_chart