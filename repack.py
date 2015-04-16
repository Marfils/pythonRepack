import os
import win32file
import shutil
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('user.ini')
#apkName = 'bzzj_020_0407_aio_360.apk'
keystor = config.get('signInfo','keyfile')
storpass = config.get('signInfo','storepassword')
keypass = config.get('signInfo','keypass')
alianame = config.get('signInfo','alias')
dirname = 'bzzj'
removeSo = config.get('removeSo','file1')


def redofile(filename):
    #decode
    cmdExtract = r'java -jar apktool2.jar  d %s -o %s'% (filename,dirname)  
    os.system(cmdExtract)
    #copy
    for root, dirs, files in os.walk(os.path.join(r'./', 'jni')):
        for f in files:
            sourceFile = os.path.join(r'./jni',  f) 
            print(sourceFile)
            targetFile = os.path.join(r'./%s/lib/armeabi'%(dirname),  f) 
            win32file.CopyFile(sourceFile,targetFile,0)
    #remove
    if os.path.exists(os.path.join(r'./%s/lib/armeabi'%(dirname), removeSo)):
        os.remove(os.path.join(r'./%s/lib/armeabi'%(dirname), removeSo))
        
    rebapkname = 'reapk.apk'
    cmdExtract = r'java -jar apktool2.jar  b %s -o %s'%(dirname,rebapkname)  
    os.system(cmdExtract)

    resignapkname = filename.split('\\')[-1]
    cmdExtract = 'jarsigner -verbose -keystore %s \
    -signedjar %s -digestalg SHA1 -sigalg MD5withRSA %s  \
    -storepass %s -keypass %s %s'%(keystor,resignapkname,rebapkname,storpass,keypass,alianame)  
    print cmdExtract
    os.system(cmdExtract)

    #if path isn't exists,mkdir
    isExists=os.path.exists('./redo/')
    if not isExists:
        os.makedirs('./redo/')

    sourceFile = os.path.join(r'./',  resignapkname)
    targetFile = os.path.join(r'./redo',resignapkname) 
    win32file.CopyFile(sourceFile,targetFile,0)

    os.remove(os.path.join(r'./', rebapkname))
    os.remove(os.path.join(r'./', resignapkname))
    os.remove(os.path.join(filename))
    #os.rmdir(os.path.join(r'./', dirname))
    shutil.rmtree(os.path.join(r'./', dirname))


#redofile(r'./apks/bzzj_020_0407_aio_360.apk')
#os.removedirs(os.path.join(r'./', 'bzzj'))
#shutil.rmtree(os.path.join(r'./', dirname))

for root, dirs, files in os.walk(os.path.join(r'./', 'apks')):
    for f in files:
        redofile(os.path.join(root, f))
        #print os.path.join(root, f)
