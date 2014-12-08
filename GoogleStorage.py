#!/usr/bin/python

import boto
import gcs_oauth2_boto_plugin
import os
import shutil
import StringIO
import tempfile
import time

#https://cloud.google.com/storage/docs/gspythonlibrary

GOOGLE_STORAGE = 'gs'



my_bucket=''

project_id = ''

header_values = {"x-goog-project-id": project_id}

# Upload these files to bucket.
#for filename in tempfiles:
dir='./upload/'
for filename in os.listdir(dir):
  start = time.time()
  with open(os.path.join(dir, filename), 'r') as localfile:

    dst_uri = boto.storage_uri(
        my_bucket + '/' + filename, GOOGLE_STORAGE)

    dst_uri.new_key().set_contents_from_file(localfile)
    end=time.time()
    print "file %s uploaded in %d seconds" %(filename, end-start)

  print 'Successfully created "%s/%s"' % (
      dst_uri.bucket_name, dst_uri.object_name)
  

