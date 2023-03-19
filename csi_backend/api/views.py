from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Sig,Team,Event
import json
from .serializers import Sigserializer,Teamserializer,Eventserializer

#write your views from here 
class Sigcontrol(APIView):
    '''
    GET request displaying all SIG and if it will recieve a name then it will return a deatil response
    '''
    def get(self,request,name=None,format=None):
        try:
            if name is None:
                sig_all = Sig.objects.all()
                # retrieving all the sigs from database
                serializer = Sigserializer(sig_all,many = True)
                # serializing all SIGs from data base to JSON
                return Response(serializer.data)
            else:
                # if name is empty then try to fetch SIG with name same as name from urls
                try:
                    sig = Sig.objects.get(name=name)
                    # fetching SIG with same name as given name from url
                except:
                    # if name is not found then show message 'name not found'
                    return Response(json.dumps({'message':'name not found'}),status = status.HTTP_404_NOT_FOUND)
                serializer = Sigserializer(sig)
                # putting data from client to serializer
                # sending message SIG object detail for given name 
                return Response(serializer.data)
        except Exception as e:
            print(e)
        
        
class Teamcontrol(APIView):
    '''
    GET request displaying all members if id is given then it will retuen a detail response
    '''
    def get(self,request,id=None,format=None):
        try:
            if id is None:
                members = Team.objects.all()
                # retrieving all the members from database
                serializer = Teamserializer(members,many = True)
                # serializing all SIGs from data base to JSON
                return Response(serializer.data)
            else:
                # if name is empty then try to fetch SIG with name same as name from urls
                try:
                  member = Team.objects.get(id = id)
                  # fetching member with same name as given id from url
                except:
                    # if name is not found then show message 'id not found'
                    return Response(json.dumps({'message':'id not found'}),status = status.HTTP_404_NOT_FOUND)
                
                serializer = Teamserializer(member)
                # putting data from client to serializer
                # sending message SIG object detail for given name 
                return Response(serializer.data)
        except Exception as e:
            print(e)

class Eventcontrol(APIView):
    '''
    GET request displaying all members if id is given then it will retuen a detail response
    '''
    def get(self,request,id=None,format=None):
        try:
                if id is None:  
                    events = Event.objects.all()
                    print(events)
                    # retrieving all the members from database
                    serializer = Eventserializer(events, many = True)
                    print(serializer.data)
                    # serializing all SIGs from data base to JSON
                    return Response(serializer.data)
                else:
                    # if name is empty then try to fetch SIG with name same as name from urls
                    try:

                        event = Event.objects.get(id = id)
                        print(event)
                        serializer = Eventserializer(event)
                        # fetching member with same name as given id from url
                    except:
                        # if name is not found then show message 'id not found'
                        return Response(json.dumps({'message':'id not found'}),status = status.HTTP_404_NOT_FOUND)
                    # putting data from client to serializer
                    # sending message SIG object detail for given name 
                    return Response(serializer.data)
        except Exception as e:
            print(e)       