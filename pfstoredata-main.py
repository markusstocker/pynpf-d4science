from hashlib import md5
from pytz import timezone
from datetime import datetime
from rdflib import Graph, URIRef, Literal
from rdflib.namespace import RDF, RDFS, XSD

configuration = {
    'Hyytiälä': {
        'identifier': URIRef('http://sws.geonames.org/656888/'),
        'name': 'Hyytiälä',
        'countryCode': 'FI',
        'locationMap': URIRef('http://www.geonames.org/656888/hyytiaelae.html'),
        'latitude': '61.84562',
        'longitude': '24.29077'
    },
    'Puijo': {
        'identifier': URIRef('http://sws.geonames.org/640784/'),
        'name': 'Puijo',
        'countryCode': 'FI',
        'locationMap': URIRef('http://www.geonames.org/640784/puijo.html'),
        'latitude': '62.91667',
        'longitude': '27.65'
    },
    'Värriö': {
        'identifier': URIRef('http://sws.geonames.org/828747/'),
        'name': 'Värriö',
        'countryCode': 'FI',
        'locationMap': URIRef('http://www.geonames.org/828747/vaerrioe.html'),
        'latitude': '67.46535',
        'longitude': '27.99231'
    },
    'Class Ia': {
        'identifier': URIRef('http://avaa.tdata.fi/web/smart/smear/ClassIa'),
        'label': 'Class Ia',
        'comment': 'Very clear and strong event'
    },
    'Class Ib': {
        'identifier': URIRef('http://avaa.tdata.fi/web/smart/smear/ClassIb'),
        'label': 'Class Ib',
        'comment': 'Unclear event'
    },
    'Class II': {
        'identifier': URIRef('http://avaa.tdata.fi/web/smart/smear/ClassII'),
        'label': 'Class II',
        'comment': 'Event with little confidence level'
    }
}

day = '2013-04-04'
place = 'Hyytiälä'
beginning = '11:00'
end = '12:00'
classification = 'Class Ia'
point = 'POINT ({} {})'.format(configuration[place]['longitude'], configuration[place]['latitude'])

ns = 'http://avaa.tdata.fi/web/smart/smear/'
tz = timezone('Europe/Helsinki')
beginning_datetime = tz.localize(datetime.strptime('{} {}'.format(day, beginning), '%Y-%m-%d %H:%M'))
end_datetime = tz.localize(datetime.strptime('{} {}'.format(day, end), '%Y-%m-%d %H:%M'))
beginning_isoformat = beginning_datetime.isoformat()
end_isoformat = end_datetime.isoformat()
time_isoformat = '{}/{}'.format(beginning_isoformat, end_isoformat)

event_uri = URIRef('{}{}'.format(ns, md5('{}{}'.format(day, place).encode()).hexdigest()))
geometry_uri = URIRef('{}{}'.format(ns, md5(point.encode()).hexdigest()))
time_uri = URIRef('{}{}'.format(ns, md5(time_isoformat.encode()).hexdigest()))
beginning_uri = URIRef('{}{}'.format(ns, md5(beginning_isoformat.encode()).hexdigest()))
end_uri = URIRef('{}{}'.format(ns, md5(end_isoformat.encode()).hexdigest()))
place_uri = configuration[place]['identifier']
classification_uri = configuration[classification]['identifier']

LODE = dict()
DUL = dict()
GeoNames = dict()
WGS84 = dict()
SMEAR = dict()
SimpleFeatures = dict()
GeoSPARQL = dict()
Time = dict()

LODE['Event'] = URIRef('http://linkedevents.org/ontology/Event')
LODE['atPlace'] = URIRef('http://linkedevents.org/ontology/atPlace')
LODE['atTime'] = URIRef('http://linkedevents.org/ontology/atTime')
LODE['inSpace'] = URIRef('http://linkedevents.org/ontology/inSpace')
LODE['involved'] = URIRef('http://linkedevents.org/ontology/involved')
DUL['Place'] = URIRef('http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Place')
GeoNames['Feature'] = URIRef('http://www.geonames.org/ontology#Feature')
GeoNames['name'] = URIRef('http://www.geonames.org/ontology#name')
GeoNames['countryCode'] = URIRef('http://www.geonames.org/ontology#countryCode')
GeoNames['locationMap'] = URIRef('http://www.geonames.org/ontology#locationMap')
WGS84['SpatialThing'] = URIRef('http://www.w3.org/2003/01/geo/wgs84_pos#SpatialThing')
WGS84['lat'] = URIRef('http://www.w3.org/2003/01/geo/wgs84_pos#lat')
WGS84['long'] = URIRef('http://www.w3.org/2003/01/geo/wgs84_pos#long')
SMEAR['Classification'] = URIRef('http://avaa.tdata.fi/web/smart/smear/Classification')
SMEAR['hasClassification'] = URIRef('http://avaa.tdata.fi/web/smart/smear/hasClassification')
SimpleFeatures['Point'] = URIRef('http://www.opengis.net/ont/sf#Point')
GeoSPARQL['asWKT'] = URIRef('http://www.opengis.net/ont/geosparql#asWKT')
GeoSPARQL['wktLiteral'] = URIRef('http://www.opengis.net/ont/geosparql#wktLiteral')
Time['Instant'] = URIRef('http://www.w3.org/2006/time#Instant')
Time['Interval'] = URIRef('http://www.w3.org/2006/time#Interval')
Time['Duration'] = URIRef('http://www.w3.org/2006/time#Duration')
Time['TemporalUnit'] = URIRef('http://www.w3.org/2006/time#TemporalUnit')
Time['hasTime'] = URIRef('http://www.w3.org/2006/time#hasTime')
Time['hasBeginning'] = URIRef('http://www.w3.org/2006/time#hasBeginning')
Time['hasEnd'] = URIRef('http://www.w3.org/2006/time#hasEnd')
Time['numericDuration'] = URIRef('http://www.w3.org/2006/time#numericDuration')
Time['unitType'] = URIRef('http://www.w3.org/2006/time#unitType')
Time['inXSDDateTime'] = URIRef('http://www.w3.org/2006/time#inXSDDateTime')
Time['unitHour'] = URIRef('http://www.w3.org/2006/time#unitHour')

g = Graph()

g.bind('lode', 'http://linkedevents.org/ontology/')
g.bind('dul', 'http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#')
g.bind('gn', 'http://www.geonames.org/ontology#')
g.bind('wgs84', 'http://www.w3.org/2003/01/geo/wgs84_pos#')
g.bind('smear', 'http://avaa.tdata.fi/web/smart/smear/')
g.bind('sf', 'http://www.opengis.net/ont/sf#')
g.bind('geosparql', 'http://www.opengis.net/ont/geosparql#')
g.bind('time', 'http://www.w3.org/2006/time#')

g.add((event_uri, RDF.type, LODE['Event']))
g.add((event_uri, LODE['atPlace'], place_uri))
g.add((event_uri, LODE['inSpace'], geometry_uri))
g.add((event_uri, LODE['atTime'], time_uri))
g.add((event_uri, SMEAR['hasClassification'], classification_uri))
g.add((place_uri, RDF.type, DUL['Place']))
g.add((place_uri, RDF.type, GeoNames['Feature']))
g.add((place_uri, GeoNames['name'], Literal(configuration[place]['name'], datatype=XSD.string)))
g.add((place_uri, GeoNames['countryCode'], Literal(configuration[place]['countryCode'], datatype=XSD.string)))
g.add((place_uri, GeoNames['locationMap'], configuration[place]['locationMap']))
g.add((place_uri, WGS84['lat'], Literal(configuration[place]['latitude'], datatype=XSD.double)))
g.add((place_uri, WGS84['long'], Literal(configuration[place]['longitude'], datatype=XSD.double)))
g.add((classification_uri, RDF.type, SMEAR['Classification']))
g.add((classification_uri, RDFS.label, Literal(configuration[classification]['label'], datatype=XSD.string)))
g.add((classification_uri, RDFS.comment, Literal(configuration[classification]['comment'], datatype=XSD.string)))
g.add((geometry_uri, RDF.type, SimpleFeatures['Point']))
g.add((geometry_uri, RDF.type, WGS84['SpatialThing']))
g.add((geometry_uri, GeoSPARQL['asWKT'], Literal(point, datatype=GeoSPARQL['wktLiteral'])))
g.add((time_uri, RDF.type, Time['Interval']))
g.add((time_uri, Time['hasBeginning'], beginning_uri))
g.add((time_uri, Time['hasEnd'], end_uri))
g.add((beginning_uri, RDF.type, Time['Instant']))
g.add((beginning_uri, Time['inXSDDateTime'], Literal(beginning_isoformat, datatype=XSD.dateTime)))
g.add((end_uri, RDF.type, Time['Instant']))
g.add((end_uri, Time['inXSDDateTime'], Literal(end_isoformat, datatype=XSD.dateTime)))

print(g.serialize(format='turtle').decode('utf-8'))
