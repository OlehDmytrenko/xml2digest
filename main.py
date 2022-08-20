#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import io
import sys
import warnings
import traceback
import re
import vectorProcessing, clustering


xmlFile = sys.argv[1]
n_clusters = sys.argv[2]

warnings.filterwarnings("ignore", message=r"\[W033\]", category=UserWarning)

if __name__=='__main__':
    
    f = open(xmlFile, encoding='utf-8')
    doc = ""
    set_keywords = []
    for line in f:
        try:
            doc = doc + line
            if line[0:18] == "</sphinx:document>":
                try:
                    set_keywords = set_keywords+re.findall("<keyword>(.+?)</keyword>+?", doc)[0].split(" ")
                    doc = "" 
                except:
                    doc = ""
                    continue    
        except BaseException as ex:
            ex_type, ex_value, ex_traceback = sys.exc_info()            
            
            output = {"error": ''}           
            output['error'] += "Exception type : %s; \n" % ex_type.__name__
            output['error'] += "Exception message : %s\n" %ex_value
            output['error'] += "Exception traceback : %s\n" %"".join(traceback.TracebackException.from_exception(ex).format())
    f.close()
    
    f = open(xmlFile, encoding='utf-8')
    doc = ""
    docsID = []
    vectors = []
    set_keywords = set(set_keywords)
    for line in f:
        try:
            doc = doc + line
            if line[0:18] == "</sphinx:document>":
                try: 
                    vector = vectorProcessing.build(re.findall("<keyword>(.+?)</keyword>+?", doc)[0], set_keywords)
                    vectors, docsID = vectorProcessing.accumulate(re.findall("<sphinx:document id=(.+?)>+?", doc)[0][1:-1], vector, vectors, docsID)
                    doc = ""
                except:
                    doc = ""
                    continue
                
        except BaseException as ex:
            ex_type, ex_value, ex_traceback = sys.exc_info()            
            
            output = {"error": ''}           
            output['error'] += "Exception type : %s; \n" % ex_type.__name__
            output['error'] += "Exception message : %s\n" %ex_value
            output['error'] += "Exception traceback : %s\n" %"".join(traceback.TracebackException.from_exception(ex).format())
    f.close()
    
    try:
        output = clustering.cluster(n_clusters, vectors, docsID)
    except BaseException as ex:
        ex_type, ex_value, ex_traceback = sys.exc_info()            
        
        output = {"error": ''}           
        output['error'] += "Exception type : %s; \n" % ex_type.__name__
        output['error'] += "Exception message : %s\n" %ex_value
        output['error'] += "Exception traceback : %s\n" %"".join(traceback.TracebackException.from_exception(ex).format())
    
    output_json = json.dumps(output, ensure_ascii=False).encode('utf-8')
    sys.stdout.buffer.write(output_json)
    print()
