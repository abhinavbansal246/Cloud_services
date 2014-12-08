__author__ = 'Devcenter'

# Refrences###########
# http://boto.readthedocs.org/en/latest/
#http://aws.amazon.com/rds/sqlserver/


AWS_ACCESS_KEY_ID=''
AWS_SECRET_ACCESS_KEY='/'
s3 = boto.connect_s3(AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY)

#creating the connection and accesing the bucket
conn = boto.connect_s3(AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY)
bucket_name=''
mybucket = conn.get_bucket(bucket_name)


state=Key(mybucket)
state.key='state'
k = Key(mybucket)
k.key = 'uni'

print "Uploading some data to " + bucket_name + " with key: " + state.key
start = time.time()
state.set_contents_from_filename('state.xls')
print "Uploading some data to " + bucket_name + " with key: " + k.key
k.set_contents_from_filename('uni.csv')
end= time.time()

mybucket.get_all_keys()
print 'time taken to upload'
print end - start