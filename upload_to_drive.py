from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

for filename in os.listdir("runs"):
    f = drive.CreateFile({'title': filename})
    f.SetContentFile(os.path.join("runs", filename))
    f.Upload()
    print(f"Uploaded {filename}")
