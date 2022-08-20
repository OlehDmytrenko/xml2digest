#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def accumulate(ID, vector, vectors, docsID):
        docsID.append(ID)
        vectors.append([int(v) for v in vector.split(" ")])
        return vectors, docsID

def build(keywords, set_keywords):
    vector = ""
    for keyword in set_keywords:
        if keyword in keywords.split(" "):
            vector += "1 "
        else:
            vector += "0 "
    return str(vector[:-1])