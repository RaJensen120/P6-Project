# from app.whisperWorkload import whisperWorkload
# from app.monteCarlo import monteCarloAlgo
# from app.TSP import tspAlgorithm
from dotenv import load_dotenv
import requests
import os
import json
import pytest

def runTest():
    # whisperWorkload.startWorkload()
    # monteCarloAlgo.startWorkload()
    # tspAlgorithm.startWorkload()
    mins = "7d"

    get_loki_logs(mins)
    get_alloy_logs(mins)

def get_loki_logs(days):
    loki_url = "http://logs-prod-025.grafana.net/loki/api/v1/query_range"
    query = '{application="Workload"} |= ``'
    load_dotenv()
    params = {
        "query": query,
        "limit": 100,
        "direction": "backward",
        "since": days
    }

    auth = (
        os.environ['GRAFANACLOUD_USERNAME'],
        os.environ['GRAFANACLOUD_PASSWORD']
    )
    response = requests.get(loki_url, params=params,auth=auth)

    if response.status_code == 200:
        data = response.json()
        with open('test.json', 'w') as f:
            json.dump(data, f, indent=4)
        
        print("data has been written successfully!")
    else:
        print("Error:", response.status_code,";", response.content,";", response.reason)
    
def get_alloy_logs(days):
    loki_url = "http://pjenky.grafana.net/api/P6/P6-Dashboard"
    query = '{application="Workload"} |= ``'
    load_dotenv()
    params = {
        "query": query,
        "limit": 100,
        "direction": "backward",
        "since": days
    }

    auth = (
        os.environ['GRAFANACLOUD_USERNAME'],
        os.environ['GRAFANACLOUD_PASSWORD']
    )
    response = requests.get(loki_url, params=params,auth=auth)

    if response.status_code == 200:
        data = response.json()
        with open('test.json', 'w') as f:
            json.dump(data, f, indent=4)
        
        print("data has been written successfully!")
    else:
        print("Error:", response.status_code,";", response.content,";", response.reason)

if __name__ == "__main__":
    runTest()