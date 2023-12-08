import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

#the json file should be put in the same location as the python file or give the entire path.
creds = ServiceAccountCredentials.from_json_keyfile_name('evaluation-407510-8f31bc069971.json', scope)

client = gspread.authorize(creds)
    
#Create one workbook name it 'TestSheet' and at the bottom rename Sheet1 as 'names'
sh = client.open('docs').worksheet('InteEV') 

#Create a list the way you want and add the data to excel worksheet,
#just use the append_row function of the sh object created.
#To read all the data just use the read_all_values() function and you get a list of lists.

row = ["Jason","221","Photography"]
sh.append_row(row)