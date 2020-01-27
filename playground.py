import tempfile
import os

tempfile.TemporaryFile()
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
f = open(storage_path, 'w')
f.close()
