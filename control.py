import l1cache as l1c

import random
import time

class Control:
    def __init__(self, l1cacheDataHolder, memory, instructionsHolder):
        self.l1cache = l1c.L1Cache()
        self.l1cacheDataHolder = l1cacheDataHolder
        self.memory = memory
        self.instructionsHolder = instructionsHolder

        # Coherence for P0 cache L1 
        self.l1getCoherenceDictionaryP0 = {
            0: self.l1cacheDataHolder.getCoherence00,
            1: self.l1cacheDataHolder.getCoherence01,
            2: self.l1cacheDataHolder.getCoherence02,
            3: self.l1cacheDataHolder.getCoherence03}                             
        self.l1setCoherenceDictionaryP0 = {
            0: self.l1cacheDataHolder.setCoherence00,
            1: self.l1cacheDataHolder.setCoherence01,
            2: self.l1cacheDataHolder.setCoherence02,
            3: self.l1cacheDataHolder.setCoherence03}
        # Coherence for P1 cache L1 
        self.l1getCoherenceDictionaryP0 = {
            0: self.l1cacheDataHolder.getCoherence10,
            1: self.l1cacheDataHolder.getCoherence11,
            2: self.l1cacheDataHolder.getCoherence12,
            3: self.l1cacheDataHolder.getCoherence13}                             
        self.l1setCoherenceDictionaryP0 = {
            0: self.l1cacheDataHolder.setCoherence10,
            1: self.l1cacheDataHolder.setCoherence11,
            2: self.l1cacheDataHolder.setCoherence12,
            3: self.l1cacheDataHolder.setCoherence13}
        # Coherence for P2 cache L1 
        self.l1getCoherenceDictionaryP0 = {
            0: self.l1cacheDataHolder.getCoherence20,
            1: self.l1cacheDataHolder.getCoherence21,
            2: self.l1cacheDataHolder.getCoherence22,
            3: self.l1cacheDataHolder.getCoherence23}                             
        self.l1setCoherenceDictionaryP0 = {
            0: self.l1cacheDataHolder.setCoherence20,
            1: self.l1cacheDataHolder.setCoherence21,
            2: self.l1cacheDataHolder.setCoherence22,
            3: self.l1cacheDataHolder.setCoherence23}
        # Coherence for P3 cache L1 
        self.l1getCoherenceDictionaryP0 = {
            0: self.l1cacheDataHolder.getCoherence30,
            1: self.l1cacheDataHolder.getCoherence31,
            2: self.l1cacheDataHolder.getCoherence32,
            3: self.l1cacheDataHolder.getCoherence33}                             
        self.l1setCoherenceDictionaryP0 = {
            0: self.l1cacheDataHolder.setCoherence30,
            1: self.l1cacheDataHolder.setCoherence31,
            2: self.l1cacheDataHolder.setCoherence32,
            3: self.l1cacheDataHolder.setCoherence33}

        # Adress for P0 cache L1                  
        self.l1getAddressDictionary = {
            0: self.l1cacheDataHolder.getAddress00,
            1: self.l1cacheDataHolder.getAddress01,
            2: self.l1cacheDataHolder.getAddress02,
            3: self.l1cacheDataHolder.getAddress03}                          
        self.l1setAddressDictionary = {
            0: self.l1cacheDataHolder.setAddress00,
            1: self.l1cacheDataHolder.setAddress01,
            2: self.l1cacheDataHolder.setAddress02,
            3: self.l1cacheDataHolder.setAddress03}
        # Adress for P1 cache L1                  
        self.l1getAddressDictionary = {
            0: self.l1cacheDataHolder.getAddress10,
            1: self.l1cacheDataHolder.getAddress11,
            2: self.l1cacheDataHolder.getAddress12,
            3: self.l1cacheDataHolder.getAddress13}                          
        self.l1setAddressDictionary = {
            0: self.l1cacheDataHolder.setAddress10,
            1: self.l1cacheDataHolder.setAddress11,
            2: self.l1cacheDataHolder.setAddress12,
            3: self.l1cacheDataHolder.setAddress13}
        # Adress for P2 cache L1                  
        self.l1getAddressDictionary = {
            0: self.l1cacheDataHolder.getAddress20,
            1: self.l1cacheDataHolder.getAddress21,
            2: self.l1cacheDataHolder.getAddress22,
            3: self.l1cacheDataHolder.getAddress23}                          
        self.l1setAddressDictionary = {
            0: self.l1cacheDataHolder.setAddress20,
            1: self.l1cacheDataHolder.setAddress21,
            2: self.l1cacheDataHolder.setAddress22,
            3: self.l1cacheDataHolder.setAddress23}
        # Adress for P3 cache L1                  
        self.l1getAddressDictionary = {
            0: self.l1cacheDataHolder.getAddress30,
            1: self.l1cacheDataHolder.getAddress31,
            2: self.l1cacheDataHolder.getAddress32,
            3: self.l1cacheDataHolder.getAddress33}                          
        self.l1setAddressDictionary = {
            0: self.l1cacheDataHolder.setAddress30,
            1: self.l1cacheDataHolder.setAddress31,
            2: self.l1cacheDataHolder.setAddress32,
            3: self.l1cacheDataHolder.setAddress33}

        # Data for P0 cache L1
        self.l1getDataDictionary = {
            0: self.l1cacheDataHolder.getData00,
            1: self.l1cacheDataHolder.getData01,
            2: self.l1cacheDataHolder.getData02,
            3: self.l1cacheDataHolder.getData03}                        
        self.l1setDataDictionary = {
            0: self.l1cacheDataHolder.setData00,
            1: self.l1cacheDataHolder.setData01,
            2: self.l1cacheDataHolder.setData02,
            3: self.l1cacheDataHolder.setData03}
        # Data for P1 cache L1
        self.l1getDataDictionary = {
            0: self.l1cacheDataHolder.getData10,
            1: self.l1cacheDataHolder.getData11,
            2: self.l1cacheDataHolder.getData12,
            3: self.l1cacheDataHolder.getData13}                        
        self.l1setDataDictionary = {
            0: self.l1cacheDataHolder.setData10,
            1: self.l1cacheDataHolder.setData11,
            2: self.l1cacheDataHolder.setData12,
            3: self.l1cacheDataHolder.setData13}
        # Data for P2 cache L1
        self.l1getDataDictionary = {
            0: self.l1cacheDataHolder.getData20,
            1: self.l1cacheDataHolder.getData21,
            2: self.l1cacheDataHolder.getData22,
            3: self.l1cacheDataHolder.getData23}                        
        self.l1setDataDictionary = {
            0: self.l1cacheDataHolder.setData20,
            1: self.l1cacheDataHolder.setData21,
            2: self.l1cacheDataHolder.setData22,
            3: self.l1cacheDataHolder.setData23}
        # Data for P3 cache L1
        self.l1getDataDictionary = {
            0: self.l1cacheDataHolder.getData30,
            1: self.l1cacheDataHolder.getData31,
            2: self.l1cacheDataHolder.getData32,
            3: self.l1cacheDataHolder.getData33}                        
        self.l1setDataDictionary = {
            0: self.l1cacheDataHolder.setData30,
            1: self.l1cacheDataHolder.setData31,
            2: self.l1cacheDataHolder.setData32,
            3: self.l1cacheDataHolder.setData33}
                                    
    def handleOperation(self, operation, procNumber, address, data):
        self.updateLocalCache(procNumber)
        l1block = self.l1cache
        return self.handleOperationAux(l1block, operation, procNumber, address, data)

    def handleOperationAux(self, l1block, operation, procNumber, address, data):
        if (operation == "R"):
            return self.handleRead(procNumber, address, l1block)
        else:
            return self.handleWrite(procNumber, address, data, l1block)

    def updateLocalCache(self, procNumber): 
        l1blocks = self.l1cache.getAllBlocks()
        l1blocks[0].setCoherence(self.l1getCoherenceDictionary.get(procNumber)())
        l1blocks[1].setCoherence(self.l1getCoherenceDictionary.get(procNumber)())

        l1blocks[0].setAddress(self.l1getAddress0Dictionary.get(procNumber)())
        l1blocks[1].setAddress(self.l1getAddress1Dictionary.get(procNumber)())

        l1blocks[0].setData(self.l1getData0Dictionary.get(procNumber)())
        l1blocks[1].setData(self.l1getData1Dictionary.get(procNumber)())
        return
