import mobase
import json

class ModlistDownloader(mobase.IPluginTool):
    _organizer: mobase.IOrganizer

    def __init__(self):
        super().__init__()
    def init(self, organizer: mobase.IOrganizer) -> bool:
        self._organizer = organizer
        return True
    def name(self) -> str:
        return "Modlist Downloader"
    def description(self) -> str:
        return self._tr("Downloads mods from \
        a modlist")
    def version(self) -> mobase.VersionInfo:
        return mobase.VersionInfo(1,0,0,mobase.ReleaseType.FINAL)
    def _tr(): # stub fxn for now
        pass

    #TODO: installation methods go here. Placeholdrs for now
    def checkFOMod() -> bool:
        pass
    # retrieve list of mods currently installed
    def getModlist():
        pass
    # stores a mod's info as a dictionary
    def storeMod(name='', author='', version='', link='') -> dict:
        mod = {'name': name, 'author': author, 'version': version, 'link':link}
        return mod
    # creates a dictionary of various of mods, indexed by number/priority
    def createModlist(): # perhaps as a json file
        modlist = {}    # TODO: make this code more elegant
        mod = storeMod()
        modlist.fromkeys(range(0, 4))
        modlist.update({0:mod})
    # store the modlist as a json file
    def storeModlist():
        pass
    # reads json file into a dictionary object (called 'modlist')
    def readModlist():
        pass
    # download a mod via Nexus API
    def downloadMod():
        pass
    # loop through and download each mod in the modlist
    # option to limit how many mods to download at once
    # default is 4 mods at once
    def downloadModlist():
        pass
    # install a mod from the modlist dictionary
    def installMod():
        pass
    # loop through the dictionary, installing each mod individually
    def installModlist():
        pass
