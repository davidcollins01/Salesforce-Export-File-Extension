import magic
import os

salesforcedirnames = [r'/ContentVersion', r'/Attachments', r'/Documents', r'/Other Uploaded Collateral']
exportdirs = [os.getcwd() + x for x in salesforcedirnames]
extensionDict = {
    'PDF document': '.pdf', 
    'Microsoft Word': '.doc' , 
    'JPEG image data': '.jpg', 
    'PNG image data': '.png', 
    'Non-ISO extended-ASCII text': '.txt', 
    'ASCII text': '.txt', 
    'Microsoft PowerPoint': '.ppt', 
    'Microsoft Excel': '.xls',
    'Composite Document File V2 Document': '.msg', 
    'Zip archive data': '.zip', 
    'CDFV2 Microsoft Outlook Message': '.msg', 
    'ISO-8859 text': '.txt', 
    'GIF image data': '.gif', 
    'HTML document': '.html' 
    }

def getExtension(magicDetails):
    try:
        for key, value in extensionDict.items():
            if (magicDetails.startswith(key)):
                return value
    except:
        return ''

filelist = []
errorlist = []
for dir in exportdirs:
    for rawfile in os.listdir(dir):
        filelist.append(os.path.join(dir, rawfile))

for file in filelist:
    try:    
        magicfile = magic.from_file(file, mime=False)
    except Exception as error:
        errorlist.append('Failed to convert ' + file + ' with error ' + type(error).__name__)

    fileextension = getExtension(magicfile)
    if fileextension is not None and not file.endswith(fileextension):
        os.rename(file, file + fileextension)
    
for error in errorlist:
    print(error)