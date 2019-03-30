#!/usr/bin/env python3
from os import listdir
from os.path import isfile, join
import os, json

from . node import Node
from . strip import Strip
from . plug import Plug

nodes = {}
strips = {}
plugs = {}

def destroyObjects():
    nodes = {}
    strips = {}
    plugs = {}

def load_definition_file(file):
    with open(file, 'r') as readFile:
        json_data = json.load(readFile)

    for node_data in json_data["nodes"]:
        nodes[node_data["id"]] = Node(node_data)

    for strip_data in json_data["strips"]:
        strip = strips[strip_data["id"]] = Strip(strip_data)

        node_id = strip.getNodeId()
        nodes[node_id].addStrip(strip)


    for plug_data in json_data["plugs"]:
        plugs[plug_data["id"]] = Plug(plug_data)

    for plug_name in plugs:
        strip_name = plugs[plug_name].getStripId()
        strips[strip_name].addPlug(plugs[plug_name])



def get_plug_id_by_adress(plug_address, strip_address, node_address):
    #print(plug,strip,node)
    for plug_id in plugs:
        plug = plugs[plug_id]
        plug_strip = strips[plug.getStripId()]
        plug_node = nodes[plug_strip.getNodeId()]
        if plug.getAddress() == plug_address \
            and plug_strip.getAddress() == strip_address \
            and plug_node.getAddress() == node_address:
            return plug.getId()
    return False

def get_strip_id_by_adress(strip, node):
    for s in strips:
        sid = strips[s].getId()
        nid = nodes[strips[s].getNodeId()].getId()
        if sid == strip and nid == node:
            return s
    return False

def get_strip_address_by_id(strip_id):
    return strips[strip_id].getAddress()

def get_node_address_by_id(node_id):
    return nodes[node_id].getAddress()

def get_plug_adress_by_id(id):
    plug = plugs[id]
    node_id = strips[plug.getStripId()].getNodeId()
    return {
        "nodeAddress": get_node_address_by_id(node_id),
        "stripAddress": get_strip_address_by_id(plug.getStripId()),
        "plugAddress": plug.getAddress()
    }

def getOnlyActiveStripNamesSortedJson():
    data = {}
    for plug_id in plugs:
        if not plugs[plug_id].getStripId() in data.keys():
            #pass
            id = plugs[plug_id].getStripId()
            data[id] = {}
            data[id]["stripId"] = strips[id].getId()
            data[id]["displayText"] = strips[id].getData()["displayText"]  
            data[id]["location"] = strips[id].getData()["location"]  
    return data

def getOnlyActiveStripNamesSorted():
    st = []
    for plug_id in plugs:
        if not plugs[plug_id].getStripId() in st:
            #pass
            st.append(plugs[plug_id].getStripId())
    return st

def getStripNamesSortedJson():
    data = {}
    for n in nodes:
        strip_list = nodes[n].getStripNames()
        for s in strip_list:
            if not s in data.keys():
                data[s] = {}
                data[s]["stripId"] = strips[s].getId()
                data[s]["displayText"] = strips[s].getData()["displayText"]
                data[s]["location"] = strips[s].getData()["location"]
    return data 

def getStripNamesSorted():
    list_of_strips = []
    for n in nodes:
        strip_list = nodes[n].getStripNames()
        for s in strip_list:
            list_of_strips.append(s)
    list_of_strips.sort()
    return list_of_strips

def getAllPlugsJson():
    data = {}
    for plug_id in plugs:
        strip_id = plugs[plug_id].getStripId()
        if not strip_id in data.keys():
            data[strip_id] = []
            #plugs[plugId].getData()
        data[strip_id].append(plugs[plug_id].getData())
        sorted(data[strip_id], key=lambda x:sorted(x.keys()))
    return data


def cleanUpObjects():
    strips.clear()
    nodes.clear()
    plugs.clear()


def loadConfig():
    print("loadConfig: destroyObjects()")
    destroyObjects()
    print("loadConfig: load_definition_file(\"nodeConfig/mainv2.json\")")
    load_definition_file("nodeConfig/mainv2.json")