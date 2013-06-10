'''
Created on 09/06/2013

@author: voval
'''

import sqlite3
import types
from multiprocessing.dummy import list

class DefectModel:
    def getDefectList(self, component):
        print('Metodo del Model')
        query ='''select ID, Component from defects where Component ='%s' ''' % component
        print(query)
        defectlist = self._dbselect(query)
        return defectlist

    def _dbselect(self,query):
        print('Acceso a Datos')
        print(query)
        connection = sqlite3.connect('TMS')
        cursorObj = connection.cursor()
        results = cursorObj.execute(query)
        list = []
        for row in results:
            list.append(row[0])
        connection.commit()
        cursorObj.close()
        return list
    

class DefectView:
    def defectList(self, list, category):
        print("### Defect List for %s ###\n" %category)
        for defect in list:
            print(defect)
            

class Controller:
    def __init__(self):
        pass
    
    def getDefectList(self,component):
        print('Metodo del Controler')
        model = DefectModel()
        view = DefectView()
        defectlist_data = model.getDefectList(component)
        return view.defectList(defectlist_data,component)
    
controller = Controller()
print(controller.getDefectList('XYZ'))

