import mobase
import json

class storeModsButton(mobase.IPluginTool):
    def __init__(self):
        super().__init__()
    # stores a mod's info as a dictionary
    def storeMod(id=0, name='', author='', version='', link='') -> dict:
        mod = {id:{'name': name, 'author': author, 'version': version, 'link':link}}
        return mod
    # creates a dictionary of various of mods, indexed by number/priority
    def createModlist(): # perhaps as a json file
        modlist = {}    
        mod = storeMod()
        modlist.update(mod)
        return modlist
    # store the modlist as a json file
    def storeModlist(modlist):
        with open("modlist.json", "w") as json_file:
            json.dump(modlist, json_file)