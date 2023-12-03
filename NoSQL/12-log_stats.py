#!/usr/bin/env python3
'''
Module that provides some stats about Nginx logs stored in MongoDB
'''
from pymongo import MongoClient


if __name__ == '__main__':
    client = MongoClient()
    nginx_collection = client.logs.nginx
    all_logs = nginx_collection.count_documents({})
    print(f'{all_logs} logs')

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        method_count = nginx_collection.count_documents({"method": method})
        print(f'\tmethod {method}: {method_count}')

    status_checks = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f'{status_checks} status check')
