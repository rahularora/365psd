from BeautifulSoup import BeautifulSoup 
import re
import urllib
import os

url = "http://365psd.com/day/"
homedir = os.path.expanduser('~')
directory = homedir + "/Desktop/365/"
days = 364
day = 1

if not os.path.exists(directory):
    os.mkdir(directory)
    
os.chdir(directory)

def get_webpage(url):
    result = urllib.urlopen(url)
    html = result.read()
    result.close()
    return html

def download_psd(psd_url):
    splits = re.split("/",psd_url)
    path = directory + splits[7]
    print "Downloading psd to " + path
    try:
        urllib.urlretrieve (psd_url,path)
    except:
        print "download_psd function : Error while downloading psd"

while (day != (days+1)):
    link = url + str(day) + "/"
    print "\nDay:" + str(day)
    try:
        html = get_webpage(link)
        soup = BeautifulSoup(html)
        psd = soup.find('a', attrs={ 'class' : 'download' })
        download_psd(psd['href'])
        
        if(day != days):
            print "Moving on to a new day, fellas!"
    
    except:
        print "Unknown Exception while using soup on link", link
        
    day = day + 1