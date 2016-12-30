import os

def access_key():
  return os.environ['S3_ACCESS']

def secret_key():
  return os.environ['S3_SECRET']
