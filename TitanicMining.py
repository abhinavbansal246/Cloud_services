__author__ = 'Devcenter'
'''
 Refrences###########

 http://boto.readthedocs.org/en/latest/
http://aws.amazon.com/rds/sqlserver/

http://stackoverflow.com/questions/4328336/how-to-position-two-divs-side-by-side-where-the-second-width-is-100
http://www.highcharts.com/demo/pie-basic
http://docs.orange.biolab.si/reference/rst/Orange.classification.bayes.html
'''

import boto
import boto.dynamodb
import pprint
import csv
import Orange
import re


AWS_ACCESS_KEY_ID=''
AWS_SECRET_ACCESS_KEY=''

conn = boto.dynamodb.connect_to_region(
        'us-west-2',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
#print conn.list_tables()
table = conn.get_table('')
content=""
#print table

#pprint.pprint(conn.describe_table('test3'))

def insertData(f):
	#print f
	item_data = {
	    'new': f,
	    }

	item = table.new_item(hash_key='training',attrs=item_data)
	item.put()

def writeOut(s):
	f = open("output.txt", "w")
	print "train"
	#print str(training)[11:-23]
	f.write(s)
	f.close()


def fetch():
	training=table.get_item(hash_key='training')
	#print "some" 
	#print training
	train=training["new"]
	s=str(training)[11:-23]
	writeOut(s)
	
def format():
	with open("output.txt", "rb") as csvfile:
		table = csv.reader(csvfile, delimiter='\t', quotechar='\n') 
		for row in table:
			print row
		csvfile.close()

def classify(train):
	titanic = Orange.data.Table("Dataset.txt")
	sample = Orange.data.Table("sample.txt")
	learner = Orange.classification.bayes.NaiveLearner()
	classifier = learner(titanic)
	print "Go"
	print ""
	feed=""
	s= str(classifier)

	s=re.split(' |\n',s)
	while "" in s:
		for row in s:
			if(len(row)==0):
				s.remove(row)
	print classifier
	
	#print classifier("['1st', 'adult', 'male', 'yes']")
	'''
	for inst in sample[:5]:
		print inst.getclass(), classifier(inst)
	'''

with open('Dataset.csv', 'rb') as content_file:
	reader = csv.reader(content_file)
	for row in reader:
		#print '    '.join(row)
		content = content+ '    '.join(row)
		
	insertData(content)
fetch()
classify(content)
