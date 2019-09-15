from django.shortcuts import render
import os
from pdf2jpg import pdf2jpg
def home(request):
    branch = 'CSE'
    year = '2'
    upload_dir = os.path.join('media',branch,year)
    ENV_PATH = os.path.abspath(os.path.dirname(__file__))[:-6]
    upload_dir = os.path.join(ENV_PATH,upload_dir)
    for filename in os.listdir(upload_dir):
        path = os.path.join(upload_dir, filename)
        newpath = os.path.join(upload_dir,filename[:-4]+'.jpg')
        if not os.path.exists(newpath):
            result = pdf2jpg.convert_pdf2jpg(path, upload_dir, pages="0")
            oldpath = os.path.join(path+'_dir','0_'+filename+'.jpg')
            print(result)
            os.rename(oldpath,newpath)
            os.rmdir(path+'_dir')
    return render(request,'home.html')

# Create your views here.
