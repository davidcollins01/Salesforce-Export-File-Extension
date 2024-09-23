# Salesforce-Export-File-Extension
Add the file extensions to a Salesforce export.

When you export an entire instance of salesforce, it loses all the file extensions. The data is still available in the files, however for a large export it is a pain to find the file types. This script works through all the export folders to add back most of the file types. Extract all your salesforce files to a folder and then place this in the root folder of the export (the folder which contains subfolders called ContentVersion, Attachments, Documents, and Other Uploaded Collateral). Run the script and it will rename all your important files.

Needs to have the magic library installed using pip install python-magic and pip install python-magic-bin
