#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist

def cluster(n_clusters, vectors, docsID):
    n_clusters = int(n_clusters)
    digest = []
    for i in range(n_clusters):
        digest.append({})
        
    M = numpy.array(vectors)

    kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(M)
    clusters = kmeans.predict(M)
    centers = kmeans.cluster_centers_
    for index in range(len(docsID)):
        digest[clusters[index]][docsID[index]] = cdist([M[index]], [centers[clusters[index]]])[0][0]
    sortdigest = {}
    for index in range(n_clusters):
        sortdigest[index] = {k: v for k, v in sorted(digest[index].items(), key=lambda item: item[1])}
    return sortdigest
    