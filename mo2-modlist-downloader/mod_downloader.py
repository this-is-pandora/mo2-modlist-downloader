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

    #TODO: installation methods go here. Placeholdrs for now
    def checkFOMod() -> bool:
        pass
    # reads json file into a dictionary object (called 'modlist')
    def getModlist():
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
