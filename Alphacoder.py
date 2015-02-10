from bs4 import BeautifulSoup
import urllib
import requests

def createFilename(url, name, folder):
    dotSplit = url.split('.')
    if name == None:
        # use the same as the url
        slashSplit = dotSplit[-2].split('/')
        name = slashSplit[-1]
    ext = dotSplit[-1]
    file = '{}{}.{}'.format(folder, name, ext)
    return file

def getImage(url, name=None, folder='./'):
    file = createFilename(url, name, folder)
    with open(file, 'wb') as f:
        r = requests.get(url, stream=True)
        for block in r.iter_content(1024):
            if not block:
                break
            f.write(block)

def main():
    print "Enter the Tag or Category :"
    tag=raw_input()
    
    
    for url_range in range(1,10):
        main_url = 'http://wall.alphacoders.com/search.php?search='+tag+'&page=' + str(url_range)
        print "Entered Page " + str(url_range)
        main_url_opener = urllib.urlopen(main_url)
        main_url_response = main_url_opener.read()
        main_url_soup = BeautifulSoup(main_url_response)
        mylist = []
        for wall_link in main_url_soup.find_all('a'):
            all_links = wall_link.get('href')
            try:
               if all_links.find('big.php?') >= 0:
                    if all_links not in mylist:
                        mylist.append(all_links)
            except:
                pass
        print mylist
        new_list = ['http://wall.alphacoders.com/' + suit for suit in mylist]#[x+'http://wall.alphacoders.com/' for x in my_list]
        print new_list
        source_list=[]
        for element in new_list:
            print element
            opener = urllib.urlopen(element)
            response = opener.read()
            soupedversion = BeautifulSoup(response)
            for imglink in soupedversion.find_all('img' , {'id' : 'main_wallpaper'}):
                mylink =  imglink.get('src')
                print mylink
                source_list.append(mylink)
        print source_list
        for i in range(0,len(source_list)):
                a=source_list[i]
                print a
                getImage(a)    

if __name__ == "__main__":
    main()


