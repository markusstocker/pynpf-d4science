# -*- coding: utf-8 -*-
import requests
import csv
from rdflib import Graph
from rdflib.plugins.sparql.results.csvresults import CSVResultSerializer
from io import BytesIO, StringIO

globalvariables = None

with open('globalvariables.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    globalvariables = {rows[0]: rows[1] for rows in reader}

headers = {'Content-Type':'application/json',
           'Accept':'application/json',
           'gcube-token':globalvariables['gcube_token']}

res = requests.get('http://catalogue-ws.d4science.org/catalogue-ws/rest/api/items/show',
                   params={'id':'new_particle_formation_events_at_hyytiaelae'},
                   headers=headers)
json = res.json()

g = Graph()

for resource in json['result']['resources']:
    g.parse(data=requests.get(resource['url']).content.decode('utf-8'), format="turtle")

q = """
SELECT ?beginning ?end ?classification ?place ?latitude ?longitude
WHERE {
?event rdf:type lode:Event .
?event lode:atTime ?atTime .
?atTime time:hasBeginning ?hasBeginning .
?hasBeginning time:inXSDDateTime ?beginning .
?atTime time:hasEnd ?hasEnd .
?hasEnd time:inXSDDateTime ?end .
?event lode:atPlace ?atPlace .
?atPlace gn:name ?place .
?atPlace wgs84:lat ?latitude .
?atPlace wgs84:long ?longitude .
?event smear:hasClassification ?hasClassification .
?hasClassification rdfs:label ?classification .
}
ORDER BY ASC(?beginning)
"""

serializer = CSVResultSerializer(g.query(q))
output = BytesIO()
serializer.serialize(output)

file = open('output.csv', 'wb')
file.write(output.getvalue())
file.close()

