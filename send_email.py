import smtplib
from email.mime.multipart import MIMEMultipart  #MIME stands for Multipurpose Internet Mail Extension
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import matplotlib.pyplot as plt 
import credentials as CD

month_mapping = {
	1 : 'January',
	2 : 'February',
	3 : 'March',
	4 : 'April',
	5 : 'May',
	6 : 'June',
	7 : 'July',
	8 : 'August',
	9 : 'September',
	10 : 'October',
	11 : 'November', 
	12 : 'December'
}

def get_text(curr_month) : 

	body = """Hey there, 

This is an automated message from your expenditure management app, we have compiled your spending patterns for the month of 
"""
	end_body = """
PFA a few charts pertaining to the same 

Feel free to drop in suggestions for us to make improvements
Till then,
Ciao 
"""

	body = body + month_mapping[curr_month] + end_body
	return body


def get_credentials() : 
	### --- decide sender , password , receiver 
	sender = CD.sender
	password = CD.password 
	return sender , password

def send_report( file_paths , curr_month ) : 

	files = [ open(file, 'rb') for file in file_paths ]	
	sender , password = get_credentials()

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(sender, password)

	message = MIMEMultipart()
	message['From'] = sender
	receiver = input(" Enter email id to send message to ")
	message['To'] = receiver
	message['Subject'] = ' Detailed report of your spending patterns '

	body = get_text( curr_month )
	message.attach(MIMEText(body, 'plain'))

	#Attachment
	for idx in range(len(files)) : 
		msgObj = MIMEBase( 'application', 'octet-stream' )
		msgObj.set_payload( files[idx].read() )
		encoders.encode_base64(msgObj)
		msgObj.add_header('Content-Disposition', 'attachment' ,filename = file_paths[idx] )
		message.attach(msgObj)

	text = message.as_string()
	server.sendmail(sender, receiver, text)
	server.quit()
