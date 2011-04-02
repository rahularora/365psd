from BeautifulSoup import BeautifulSoup 
import re
import urllib
import os

url = "http://365psd.com/day/"
homedir = os.path.expanduser('~')
directory = homedir + "/Desktop/365/"
days = 3
day = 1

psd_directory = directory + "psd/"

def create_dir(dir):
	if not os.path.exists(dir):
		os.mkdir(dir)

create_dir(directory)
create_dir(psd_directory)
    
os.chdir(directory)

def remove_whitespace(data):
    'Function to remove white-space from text'
    p = re.compile(r'\s+')
    return p.sub('', data)
    
def get_webpage(url):
    result = urllib.urlopen(url)
    html = result.read()
    result.close()
    return html

def download_psd(psd_url, title):
    path = psd_directory + title + ".zip"
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
        
        div = soup.find('div', attrs={ 'id' : 'content' })
        div = str(div)
        divsoup = BeautifulSoup(div)
        
        title = divsoup.find('h1')
        title_text = title.text
        title_text = title_text.replace(" ","_")
        
        psd = divsoup.find('a', attrs={ 'class' : 'download' })
        download_psd(psd['href'], title_text)
        
        if(day != days):
            print "Moving on to a new day, fellas!"
    
    except:
        print "Unknown Exception while using soup on link", link
        
    day = day + 1