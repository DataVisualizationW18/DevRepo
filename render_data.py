import pygal

def generate_bar_chart_popularity(libraries):
	bar_chart = pygal.Bar()
	sorted_libraries = sorted(libraries, key=lambda library: library.popularity, reverse=True)
	for library in sorted_libraries:
		bar_chart.add(library.name, library.popularity)
	return bar_chart

def generate_pie_chart_popularity(libraries):
	pie_chart = pygal.Pie()
	sorted_libraries = sorted(libraries, key=lambda library: library.popularity, reverse=True)
	for library in sorted_libraries:
		pie_chart.add(library.name, library.popularity)
	return pie_chart

def generate_hor_bar_chart_popularity(libraries):
	bar_chart = pygal.HorizontalBar()
	sorted_libraries = sorted(libraries, key=lambda library: library.popularity, reverse=True)
	for library in sorted_libraries:
		bar_chart.add(library.name, library.popularity)
	return bar_chart

def generate_xy_chart_issue_closing_time(libraries):
	xy_chart = pygal.XY(range=(0,1))
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
	box_chart = pygal.Box(x_title='Total Responses', x_label_rotation = 0)
	all_response_times = []
	for library in libraries:
		response_times = []
		for issue in library.issue_data:
			if issue.issue_closing_date != None:
				response_times.append(issue.time_to_close)

		box_chart.add(library.name, response_times)
		all_response_times.append(str(len(response_times)))
	box_chart.x_labels = all_response_times
	return box_chart

def generate_xy_chart_issue_response_time(libraries):
	xy_chart = pygal.XY(range=(0,1))
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
	box_chart = pygal.Box(x_title='Total Responses', x_label_rotation = 0)
	all_response_times = []
	for library in libraries:
		response_times = []
		for issue in library.issue_data:
			if issue.issue_closing_date != None:
				response_times.append(issue.time_to_response)

		box_chart.add(library.name, response_times )
		all_response_times.append(str(len(response_times)))
	box_chart.x_labels = all_response_times
	return box_chart