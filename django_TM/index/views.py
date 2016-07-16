from django.shortcuts import render
from django.http import HttpResponse
from django import forms
import MySQLdb


def find_message(req):
    if req.method == 'POST':
        symptom={}
        disease={}
        drugs={}
        Manufac=[]
        conn=MySQLdb.connect(host="192.168.20.151",user="root",passwd="chendi1995",db="Medical_care",charset="utf8")
        cur=conn.cursor()
        keyword=req.POST['key']
        cur.execute("SELECT id from Behavior where name LIKE '%%%s%%'" %keyword)
        results=cur.fetall()
        if results!=None:
            for Bid in results: 
                cur.execute("SELECT name from Behavior where id = '%d'" %Bid[0])
                name=cur.fetchone()
                symptom[name[0]]=disease
                disease={}
                cur.execute("SELECT Did from Behavior_Disease where Bid = '%d'" % Bid[0])
                results=cur.fetchall()
                for Did in results:
                    cur.execute("SELECT name from Disease where id = '%d'" % Did[0])
                    disease_name=cur.fetchone()
                    disease[disease_name[0]]=drugs
                    drugs={}
                    cur.execute("SELECT drugs_id  from Treatment where disease_id = '%d'" % Did[0])
                    results=cur.fetchall()
                    for Mid in results:
                        cur.execute("SELECT name from Drugs where id = '%d'" % Mid[0])
                        Drugs_name=fetchone()
                        drugs[Drugs_name[0]]=Manufac
                        Manufac=[]
                        cur.execute("SELECT Mid from Produce where Did = '%d'" % Mid[0])
                        results=cur.fetchall()
                        for Oid in results:
                            cur.execute("SELECT name from Manufacturer where id ='%d'" %Oid[0])
                            Org_name=fetchone()
                            Manufac.append(Org_name)
            json_data1=symptom
        symptom=[]
        disease={}
        drugs={}
        Manufac=[]
        cur.execute("SELECT id from Disease where name LIKE '%%%s%%'" %keyword)
      	results=cur.fetall()
        if results!=None:
            for Did in results: 
                cur.execute("SELECT name from Disease where id = '%d'" %Did[0])
                name=cur.fetchone()
                disease[name[0]]=symptom
                disease[name[0]]=drugs
                drugs={}
                symptom=[]
                cur.execute("SELECT Bid from Behavior_Disease where Bid = '%d'" % Did[0])
                results=cur.fetchall()
                for Bid in results:
                    cur.execute("SELECT name from Behavior where id = '%d'" % Bid[0])
                    behavior_name=cur.fetchone()
                    symptom.append(behavior_name[0])  
                cur.execute("SELECT drugs_id  from Treatment where disease_id = '%d'" % Did[0])
                results=cur.fetchall()
                for Mid in results:
                	cur.execute("SELECT name from Drugs where id = '%d'" % Mid[0])
                	Drugs_name=fetchone()
                        drugs[Drugs_name[0]]=Manufac
                        Manufac=[]
                        cur.execute("SELECT Mid from Produce where Did = '%d'" % Mid[0])
                        results=cur.fetchall()
                        for Oid in results:
                            cur.execute("SELECT name from Manufacturer where id ='%d'" %Oid[0])
                            Org_name=fetchone()
                            Manufac.append(Org_name)	
            json_data2=disease
        symptom=[]
        disease={}
        drugs={}
        Manufac=[]
        cur.execute("SELECT id from Drugs where name LIKE'%%%s%%'" %keyword) ##medicine
        results=cur.fetall()
        if results!=None:
            for Mid in results: 
                cur.execute("SELECT name from Drugs where id = '%d'" %Mid[0])
                name=cur.fetchone()
                drugs[name[0]]=disease
                drugs[name[0]]=Manufac
                drugs={}
                Maufac=[]
                cur.execute("SELECT Mid from Produce where Did = '%d'" % Mid[0])
                results=cur.fetchall()
                for Oid in results:
                    cur.execute("SELECT name from Manufacturer where id ='%d'" %Oid[0])
               	    Org_name=fetchone()
                    Manufac.append(Org_name)	
                cur.execute("SELECT disease_id  from Treatment where drugs_id = '%d'" % Mid[0])
                results=cur.fetchall()
                for Did in results:
                    cur.execute("SELECT name from Disease where id = '%d'" %Did[0])
                    name=cur.fetchone()
                    disease[name[0]]=symptom
                    symptom=[]
                    cur.execute("SELECT Bid from Behavior_Disease where Bid = '%d'" % Did[0])
                    results=cur.fetchall()
                    for Bid in results:
                        cur.execute("SELECT name from Behavior where id = '%d'" % Bid[0])
                        behavior_name=cur.fetchone()
                        symptom.append(behavior_name[0])  
                
       
        if Mid != None:
            Mid[0]
        cur.execute("SELECT id from Manufactuer where name LIKE '%%%s%%'" %keyword) ##org
        Oid=cur.fetchone()
        if Oid != None:
            Oid[0]
       
        

# Create your views here.
