#!/usr/bin/env python3
from os import listdir
from os.path import isfile, join
import os, json

from nodeConfig import node
from nodeConfig import strip
from nodeConfig import plug

nodes = {}
strips = {}
plugs = {}

def buildUpObjects(file):
    with open(file, 'r') as readFile:
        jsonData = json.load(readFile)

    for nodeName in jsonData["nodes"][0]:
        obj = jsonData['nodes'][0][nodeName]
        nodes[nodeName] = node.Node(obj)

    for stripName in jsonData["strips"][0]:
        obj = jsonData['strips'][0][stripName]
        strips[stripName] = strip.Strip(obj)

    for plugName in jsonData["plugs"][0]:
        obj = jsonData['plugs'][0][plugName]
        plugs[plugName] = plug.Plug(obj)

    for stripName in strips:
        nodeName = strips[stripName].getNode()
        nodes[nodeName].addStrip(strips[stripName])

    for plugName in plugs:
        stripName = plugs[plugName].getStrip()
        strips[stripName].addPlug(plugs[plugName])

def getPlugNameByAdress(plug,strip,node):
    #print(plug,strip,node)
    for p in plugs:
        pid = plugs[p].getId()
        sid = strips[plugs[p].getStrip()].getId()
        nid = nodes[strips[plugs[p].getStrip()].getNode()].getId()
        if pid == plug and sid == strip and nid == node:
            return p
    return False

def getStripNameByAdress(strip,node):
    for s in strips:
        sid = strips[s].getId()
        nid = nodes[strips[s].getNode()].getId()
        if sid == strip and nid == node:
            return s 
    return False



def getPlugAdressByName(name):
    pid = plugs[name].getId()
    sid = strips[plugs[name].getStrip()].getId()
    nid = nodes[strips[plugs[name].getStrip()].getNode()].getId()
    return {"node":nid, "strip":sid, "plug":pid}

def cleanUpObjects():
    strips.clear()
    nodes.clear()
    plugs.clear()

buildUpObjects("nodeConfig/main.json")