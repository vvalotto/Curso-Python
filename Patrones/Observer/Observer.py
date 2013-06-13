'''
Created on 12/06/2013

@author: voval
'''


class Publisher:
    def __init__(self):
        pass
    
    def register(self):
        #override
        pass
    
    def unregister(self):
        #override
        pass
    
    def notifyAll(self):
        #override
        pass
    
class TechForum(Publisher):
    def __init__(self):
        self.__listOfUsers = []
        self.postname = None
        
    def register(self, userObj):
        if userObj not in self.__listOfUsers:
            self.__listOfUsers.append(userObj)
    
    def unregister(self,userObj):
        self.__listOfUsers.remove(userObj)
        
    
    
        