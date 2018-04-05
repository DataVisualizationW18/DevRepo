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

        # two headers library popularity count
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

    elif metric == 'release frequency':
        
        html ="""
        <table class="hover"> 
            <thead>
                <tr>"""

        rows = ""

        for library in libraries:

            html += """"<th width="150">Release Dates for""" + library.name + """</th>"""
            rows += "<td>" + library.release_frequency
        html +=""" </tr>
            </thead>
            <tbody>"""

        # two headers library popularity count
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
        pass
    elif metric == 'performance':
        pass
    elif metric == 'security':
        pass
    elif metric == 'issue response time':
        pass
    elif metric == 'issue closing time':
        pass
    elif metric == 'backwards compatibility':
        pass
    elif metric == 'last discussed':
        pass

    return(html)