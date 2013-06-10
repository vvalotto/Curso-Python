'''
Created on 09/06/2013

@author: voval
'''
from cmd import Cmd

class Switch:
    """ La clase INVOKER """
    def __init__(self,flipUpCmd, flipDownCmd):
        self.__flipUpCommand = flipUpCmd
        self.__flipDownCommand = flipDownCmd
    
    def flipUp(self):
        self.__flipUpCommand.execute()
        
    def flipDown(self):
        self.__flipDownCommand.execute()


class Ligth:
    """ La clase Receptora"""
    def turnOn(self):
        print('La luz esta prendida')
        
    def turnOff(self):
        print("la luz esta apagada")
        

class Command:
    """ la clase abstracta COMMAND"""
    def __int__(self):
        pass
    
    def execute(self):
        pass
    
class FlipUpCommand(Command):
    def __init__(self,ligth):
        self.__ligth = ligth
    
    def execute(self):
        self.__ligth.turnOn()
        
class FlipDownCommand(Command):
    def __init__(self,ligth):
        self.__ligth = ligth
    
    def execute(self):
        self.__ligth.turnOff()
        
class LigthSwitch:
    """ La clase cliente """
    def __init__(self):
        self.__lamp = Ligth()
        "self.__switchUp = FlipUpCommand(self.__lamp)"
        "self.__switchDown = FlipDownCommand(self.__lamp)"
        self.__switch = Switch(self.__switchUp, self.__switchDown)
        
    def switch(self,cmd):
        cmd = cmd.strip().upper()
        try:
            if cmd == "ON":
                self.__switch.flipUp()
            elif cmd == "OFF":
                self.__switch.flipDown()
            else:
                print("Argument \"ON\" or \"OFF\" is required.")
        except Exception as exc:
            print('"Exception occured: %s" % exc')
        
if __name__ == "__main__":
    
    lightSwitch = LigthSwitch()
    
    print("Switch ON test.")
    lightSwitch.switch("ON")

    print("Switch OFF test.")
    lightSwitch.switch("OFF")    
    
    print("Invalid Command test.")
    lightSwitch.switch("***")
    
        

        