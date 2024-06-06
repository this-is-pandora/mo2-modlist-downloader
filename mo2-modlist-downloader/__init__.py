from .mod_downloader import ModlistDownloader

def createPlugin() -> ModlistDownloader:
    return ModlistDownloader()
