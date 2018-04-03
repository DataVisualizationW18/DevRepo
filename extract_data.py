import xlrd
from xlrd import open_workbook
from datetime import datetime

class Domain(object):
  def __init__(self, name):
    self.name = name
    self.librarys = []

class Library(object):
  def __init__(self, name, github_repo, domain):
    self.name = name
    self.domain = domain
    self.github_repo = github_repo
    self.popularity = 0
    self.release_frequency = []
    self.last_modification_date = None
    self.backward_compatibilty = []
    self.last_discussed_on_stack_overflow = [None, 0]
    self.issue_data = []

class IssueData(object):
  def __init__(self, issueID, issue_creation_date, issue_closing_date, date_of_first_comment, performance_issue, security_issue):
    self.issueID = issueID
    self.issue_creation_date = issue_creation_date
    self.issue_closing_date = issue_closing_date
    self.date_of_first_comment = date_of_first_comment
    self.performance_issue = performance_issue
    self.security_issue = security_issue

class Date(object):
  def __init__(self, year, month, day):
    self.year = year
    self.month = month
    self.day = day

def getDomainsAndLibraries(sheet):
  global Domains
  # print('getDomainsAndLibraries')
  for row in range(1, sheet.nrows):
    values = []
    for col in range(sheet.ncols):
      value = (sheet.cell(row,col).value)
      values.append(value)
    already_created = False
    for i in Domains:
      if i.name == values[2]:
        already_created = True
        i.librarys.append(Library(*values))
    if not already_created:
      Domains.append(Domain(values[2]))
      Domains[len(Domains) - 1].librarys.append(Library(*values))

def getPopularity(sheet):
  global Domains
  # print('getPopularity')
  for row in range(1, sheet.nrows):
    values = []
    for col in range(sheet.ncols):
      value = (sheet.cell(row,col).value)
      values.append(value)

    for domain in Domains:
      for library in domain.librarys:
        if library.name == values[0]:
          library.popularity = int(values[1])

def getReleaseFrequency(sheet, wb):
  global Domains
  # print('getReleaseFrequency')
  for col in range(0, sheet.ncols):

    values = []
    noSpaces = sheet.cell(0,col).value.split()

    # print(noSpaces[len(noSpaces) - 1])
    # print(sheet.cell(1,col))
    # print(sheet.cell(2,col).value)
    # time = xlrd.xldate.xldate_as_datetime(sheet.cell(2,col).value, wb.datemode)
    # print(time.strftime("%Y"), time.strftime("%m"), time.strftime("%d"))
    for row in range(1, sheet.nrows):
      # print(sheet.cell(row,col).value)
      # value = (sheet.cell(row,col).value.split('-'))
      if (sheet.cell(row,col).value != ''):
        time = xlrd.xldate.xldate_as_datetime(sheet.cell(row,col).value, wb.datemode)
        new_time = Date(int(time.strftime("%Y")), int(time.strftime("%m")), int(time.strftime("%d")))
        # print(value)
        values.append(new_time)

    for domain in Domains:
      for library in domain.librarys:
        name = library.name.split()
        if name[len(name)-1] == noSpaces[len(noSpaces) - 1]:
          library.release_frequency = values

def getLastModificationDate(sheet, wb):
  # print('getLastModificationDate')
  global Domains

  for row in range(1, sheet.nrows):
    values = []
    for col in range(sheet.ncols):
      value = (sheet.cell(row,col).value)
      values.append(value)

    for domain in Domains:
      for library in domain.librarys:
        if library.name == values[0]:
          time = xlrd.xldate.xldate_as_datetime(values[1], wb.datemode)
          library.last_modification_date = Date(int(time.strftime("%Y")), int(time.strftime("%m")), int(time.strftime("%d")))

def getBackwardsCompatibility(sheet):
  # print('getBackwardsCompatibility')
  global Domains

  for col in range(1, sheet.ncols):

    values = []
    noSpaces = sheet.cell(0,col).value.split()

    for row in range(1, sheet.nrows):
      if (sheet.cell(row,col).value != ''):
        value = int(sheet.cell(row,col).value)

        values.append(value)

    for domain in Domains:
      for library in domain.librarys:
        name = library.name.split()
        if name[len(name)-1] == noSpaces[len(noSpaces) - 1]:
          library.backward_compatibilty = values

def getLastDiscussedOnStackOverflow(sheet, wb):
  # print('getLastDiscussedOnStackOverflow')
  global Domains

  for row in range(1, sheet.nrows):
    values = []
    for col in range(sheet.ncols):
      value = (sheet.cell(row,col).value)
      values.append(value)

    for domain in Domains:
      for library in domain.librarys:
        if library.name == values[0]:
          if values[1] != 'Never':
            time = xlrd.xldate.xldate_as_datetime(values[1], wb.datemode)
            library.last_discussed_on_stack_overflow[0] = Date(int(time.strftime("%Y")), int(time.strftime("%m")), int(time.strftime("%d")))
          library.last_discussed_on_stack_overflow[1] = int(values[2])

def getIssueData(sheet, wb):
  # print('getIssueData')
  global Domains

  for row in range(1, sheet.nrows):
    values = []
    for col in range(sheet.ncols):
      value = (sheet.cell(row,col).value)
      values.append(value)

    for domain in Domains:
      for library in domain.librarys:
        if library.name == values[1]:

          if type(values[2]) == str and values[2] != 'None':
            time2 = values[2].split()
            new_time2 = time2[0].split('-')
            time_2 = Date(new_time2[0], new_time2[1], new_time2[2])
          elif values[2] != 'None':
            time2 = xlrd.xldate.xldate_as_datetime(values[2], wb.datemode)
            time_2 = Date(int(time2.strftime("%Y")), int(time2.strftime("%m")), int(time2.strftime("%d")))
          else:
            time_2 = None
          if type(values[3]) == str and values[3] != 'None':
            time3 = values[3].split()
            new_time3 = time3[0].split('-')
            time_3 = Date(new_time3[0], new_time3[1], new_time3[2])
          elif values[3] != 'None':
            time3 = xlrd.xldate.xldate_as_datetime(values[3], wb.datemode)
            time_3 = Date(int(time3.strftime("%Y")), int(time3.strftime("%m")), int(time3.strftime("%d")))
          else:
            time_3 = None
          if type(values[4]) == str and values[4] != 'None':
            time4 = values[4].split()
            new_time4 = time4[0].split('-')
            time_4 = Date(new_time4[0], new_time4[1], new_time4[2])
          elif values[4] != 'None':
            time4 = xlrd.xldate.xldate_as_datetime(values[4], wb.datemode)
            time_4 = Date(int(time4.strftime("%Y")), int(time4.strftime("%m")), int(time4.strftime("%d")))
          else:
            time_4 = None
          library.issue_data.append(IssueData(values[0], time_2, time_3, time_4, values[5], values[6]))



def getRawData():
  global all_libraries
  global Domains
  wb = open_workbook('Metric_Data.xlsx')

  all_libraries = []
  Domains = []

  for sheet in wb.sheets():

    if sheet.name == 'Library Info':
      getDomainsAndLibraries(sheet)

    elif sheet.name == 'Popularity':
      getPopularity(sheet)

    elif sheet.name == 'Release Frequency':
      getReleaseFrequency(sheet, wb)

    elif sheet.name == 'Last Modification Date':
      getLastModificationDate(sheet, wb)

    elif sheet.name == 'Backwards Compatibility':
      getBackwardsCompatibility(sheet)

    elif sheet.name == 'Last Discussed on Stack Overflo':
      getLastDiscussedOnStackOverflow(sheet, wb)

    elif sheet.name == 'Issue Data':
      getIssueData(sheet, wb)

  # return all_libraries
  return Domains

if __name__ == '__main__':

  print()
  temp = getRawData()
  # for library in temp:
  #   # print(library.name, library.domain, library.github_repo, library.popularity, library.last_modification_date.year)
  #   print(library.name, library.issue_data[0].issueID)
  for domain in temp:
    print(domain.name)
    for library in domain.librarys:
      print(library.name, library.domain)
    print()
