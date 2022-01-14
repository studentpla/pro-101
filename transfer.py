import dropbox
import os
from dropbox.files import WriteMode
class Transfer:
    def __init__(self,access_token):
        self.access_token = access_token
    
    def uploadfile(self, filefrom, fileto):
        dbx = dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(filefrom):
            for filename in files:
                local_path = os.path.join(root,filename)
                relative_path = os.path.relpath(local_path, filefrom) 
                dropbox_path = os.path.join(fileto, relative_path)
                with open(local_path, 'rb') as f: 
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
        access_token = "_G_QanegY3AAAAAAAAAAAe6e0X-qH3ZhLrtXV_2SIkVo1Iwt0ZsuKo0scLTPrcjx"
        transferdata = Transfer(access_token)
        filefrom = input("enter the file path to transfer:")
        fileto = input ("enter the path to upload to drop box")
        transferdata.uploadfile(filefrom,fileto)

        print("file has been moved")

main()