from .modlist-downloader import ModlistDownloader

def createPlugin() -> ModlistDownloader:
    return ModlistDownloader()
