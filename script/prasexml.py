#/usr/bin/env python
# -*- coding: cp936 -*
# encoding=utf8 
import sys  
reload(sys) 
from dircache import listdir
import datetime
start=datetime.datetime.now()
sys.setdefaultencoding('utf8')
try:
        import xml.etree.cElementTree as ET
except ImportError:
        import xml.etree.ElementTree as ET
sql_path='../sql/'

Me_Di_path='../dataxml/'

Me_di_list=listdir(Me_Di_path)
num=len(Me_di_list)
for name in Me_di_list:
	sql=open(sql_path+'operation.sql','a+')
	name=Me_Di_path+name
	medicine=''
	Ditemp=''
	location=''
	Org=''
	Disease=[]
	tree=ET.parse(name)
	root=tree.getroot()
	for token in tree.iter(tag='tok'):
		feature=token.find('fea')
		for f in feature.findall('f'):
		    if f.text=='NeMedicament':
		        for w in token.iter('tok'):
		            if w.get('type')=='atom':
		                medicine+=w.text;
		    if f.text=='NeDisease':
		        for w in token.iter('tok'):
		            if w.get('type')=='atom':
		                Ditemp+=w.text
		        Disease.append(Ditemp)
		        Ditemp=''
		    if f.text=='NeOrg':
		    	for w in token.iter('tok'):
		            if w.get('type')=='atom':
		                Org+=w.text
		    if f.text=='NeLoc':
		        for w in token.iter('tok'):
		            if w.get('type')=='atom':
		                location+=w.text
	for d in Disease:
	    relation="INSERT INTO Treatment SELECT Disease.Did, Drugs.id FROM Disease cross join Drugs WHERE Disease.name=='%s' AND Drugs.name=='%s'\n" %(d,medicine)
	    sql.write(relation)
	sql.close()
        print 'there are %d files to complete'%num
        num=num-1
end=datetime.datetime.now()
print 'all completed'
print 'total time:%ds'%(end-start).seconds
