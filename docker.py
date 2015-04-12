import os
import json
import requests
def getContainers(host):
    api="http://%s:2375/containers/json" % host
    res=requests.get(api)
    containers=json.loads(res.text)
    entrys=[]
    data={}
    data["host"]=host
    data["containers"]=containers
    entrys.append(data)
    return entrys
def getAllHostContainers():
    containers=[]
    containers.extend(getContainers("192.168.253.150"))
    containers.extend(getContainers("192.168.253.151"))
    containers.extend(getContainers("192.168.253.152"))
    return containers
print getAllHostContainers()
    
