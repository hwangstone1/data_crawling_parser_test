import os
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

def fetch_clien_latest_data():
    result = []