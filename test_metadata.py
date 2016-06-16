import argparse
import girder
from girder.utility.server import configureServer

# Load configuration. Note: plugin needs to be enabled.

configureServer()

# Now we can load the data
DEFAULT_PATH="/Volumes/data/aj/Developer/data/yt/acisf05356N003_evt2.fits"
DEFAULT_ITEMID="57631cb4e640ae56cbec1d5a"

from girder.plugins.metadata_extractor_plus import metadata_extractor_plus as mep
from girder.utility.model_importer import ModelImporter

def load_metadata(path, itemId):
    print "Loading metadata for %s with itemId %s" % (path, itemId)
    m = mep.MetadataExtractor(path, itemId)
    m.extractMetadata()
    return m

def load_item(itemId):
    return ModelImporter.model('item').load(itemId, force=True)

def set_metadata_for_item(item, meta):
    ModelImporter.model('item').setMetadata(item, meta.metadata)

def main(path, itemId):
    if path is None:
        path = DEFAULT_PATH
    if itemId is None:
        itemId = DEFAULT_ITEMID
    metadata = load_metadata(path, itemId)
    item = load_item(itemId)
    set_metadata_for_item(item, metadata)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", type=str)
    parser.add_argument("-i", "--item", type=str)
    args = parser.parse_args()
    main(args.path, args.item)
