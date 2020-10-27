import numpy as np
import pandas as pd
import re

def get_zip_code(text):
  zip_code_pattern = r"\d{4}"
  return re.findall(zip_code_pattern, text)

def get_dates(text):
  date_pattern = r"\d{2}-\d{2}-\d{4}"
  return re.findall(date_pattern, text)

def get_url(text):
  url_pattern = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
  return re.findall(url_pattern, str(text))
