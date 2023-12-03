#!/usr/bin/env python3
'''
Module that List all documents in a collection
'''


def list_all(mongo_collection):
    '''
    function that lists all documents in a collection
    '''
    documents = []
    cursor = mongo_collection.find()
    for document in cursor:
        documents.append(document)
    return documents
