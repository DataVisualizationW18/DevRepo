def generate_table(libraries, metric):

    metric = metric.lower()

    if metric == 'popularity':
        html ="""
        <table class="hover"> 
            <thead>
                <tr>
                    <th width="150">Library</th>
                    <th width="150">Popularity Count</th>
                </tr>
            </thead>
            <tbody>"""

        for library in libraries:
            row = """
            <tr>
                <td>""" + library.name + """</td>
                <td>""" + str(library.popularity) + """</td>
            </tr>"""
            html += row
    
        html +="""
            </tbody>
        </table>"""

    elif metric == 'last modification date':
        html ="""
        <table class="hover"> 
            <thead>
                <tr>
                    <th width="150">Library</th>
                    <th width="200">Last Modification Date (YYYY-MM-DD)</th>
                </tr>
            </thead>
            <tbody>"""

        for library in libraries:
            row = """
            <tr>
                <td>""" + library.name + """</td>
                <td>""" + library.last_modification_date.toStr() + """</td>
            </tr>"""
            html += row
    
        html +="""
            </tbody>
        </table>"""

    elif metric == 'last discussed':
        html ="""
            <table class="hover"> 
            <thead>
                <tr>
                    <th width="150">Library</th>
                    <th width="200">Last Discussed on Stack Overflow (YYYY-MM-DD)</th>
                    <th width="200">Number of Questions Asked in Stack Overflow (YYYY-MM-DD)</th>
                </tr>
            </thead>
            <tbody>"""

        for library in libraries:

            date = library.last_discussed_on_stack_overflow[0]
            if date == None:
                date = 'Never'
            else:
                date = date.toStr()

            row = """
            <tr>
                <td>""" + library.name + """</td>
                <td>""" + date + """</td>
                <td>""" + str(library.last_discussed_on_stack_overflow[1]) + """</td>
            </tr>"""
            html += row
    
        html +="""
            </tbody>
        </table>"""

    elif metric == 'performance':

        html ="""
            <table class="hover"> 
            <thead>
                <tr>
                    <th width="150">Issue ID</th>
                    <th width="150">Library</th>
                    <th width="200">Issue Creation Date (YYYY-MM-DD)</th>
                    <th width="200">Issue Closing Date (YYYY-MM-DD)</th>
                    <th width="200">Date of First Comment (YYYY-MM-DD)</th>
                </tr>
            </thead>
            <tbody>"""

        for library in libraries:
            for issue in library.issue_data:
                
                if issue.performance_issue.lower() == 'yes':               

                    date1 = date_check(issue.issue_creation_date)
                    date2 = date_check(issue.issue_closing_date)
                    date3 = date_check(issue.date_of_first_comment)

                    row = """
                    <tr>
                        <td>""" + str(issue.issueID) + """</td>
                        <td>""" + library.name + """</td>
                        <td>""" + date1 + """</td>
                        <td>""" + date2 + """</td>
                        <td>""" + date3 + """</td>
                    </tr>"""
                    html+=row

        html +="""
            </tbody>
        </table>"""

    elif metric == 'security':
        
        html ="""
            <table class="hover"> 
            <thead>
                <tr>
                    <th width="150">Issue ID</th>
                    <th width="150">Library</th>
                    <th width="200">Issue Creation Date (YYYY-MM-DD)</th>
                    <th width="200">Issue Closing Date (YYYY-MM-DD)</th>
                    <th width="200">Date of First Comment (YYYY-MM-DD)</th>
                </tr>
            </thead>
            <tbody>"""

        for library in libraries:
            for issue in library.issue_data:
                
                if issue.security_issue.lower() == 'yes':               

                    date1 = date_check(issue.issue_creation_date)
                    date2 = date_check(issue.issue_closing_date)
                    date3 = date_check(issue.date_of_first_comment)

                    row = """
                    <tr>
                        <td>""" + str(issue.issueID) + """</td>
                        <td>""" + library.name + """</td>
                        <td>""" + date1 + """</td>
                        <td>""" + date2 + """</td>
                        <td>""" + date3 + """</td>
                    </tr>"""
                    html+=row

        html +="""
            </tbody>
        </table>"""

    elif metric == 'issue response time':
        html ="""
            <table class="hover"> 
            <thead>
                <tr>
                    <th width="150">Issue ID</th>
                    <th width="150">Library</th>
                    <th width="200">Issue Creation Date (YYYY-MM-DD)</th>
                    <th width="200">Date of First Comment (YYYY-MM-DD)</th>
                </tr>
            </thead>
            <tbody>"""

        for library in libraries:
            for issue in library.issue_data:              

                date1 = date_check(issue.issue_creation_date)
                date3 = date_check(issue.date_of_first_comment)

                row = """
                    <tr>
                        <td>""" + str(issue.issueID) + """</td>
                        <td>""" + library.name + """</td>
                        <td>""" + date1 + """</td>
                        <td>""" + date3 + """</td>
                    </tr>"""
                html+=row

        html +="""
            </tbody>
        </table>"""

    elif metric == 'issue closing time':
        html ="""
            <table class="hover"> 
            <thead>
                <tr>
                    <th width="150">Issue ID</th>
                    <th width="150">Library</th>
                    <th width="200">Issue Creation Date (YYYY-MM-DD)</th>
                    <th width="200">Issue Closing Date (YYYY-MM-DD)</th>
                </tr>
            </thead>
            <tbody>"""

        for library in libraries:
            for issue in library.issue_data:
                
                if issue.security_issue.lower() == 'yes':               

                    date1 = date_check(issue.issue_creation_date)
                    date2 = date_check(issue.issue_closing_date)

                    row = """
                    <tr>
                        <td>""" + str(issue.issueID) + """</td>
                        <td>""" + library.name + """</td>
                        <td>""" + date1 + """</td>
                        <td>""" + date2 + """</td>
                    </tr>"""
                    html+=row

        html +="""
            </tbody>
        </table>"""

    # also trouble
    elif metric == 'backwards compatibility':
        pass
    #this one is trouble
    elif metric == 'release frequency':
        pass

    return(html)

def date_check(date):

    if date == None:
        date = 'Never'
    else:
        date = date.toStr()
    
    return date