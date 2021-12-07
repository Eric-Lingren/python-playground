

# for n in range(100):
#     print(n)

import wget

for n in range(100):
    try:
        root = "https://putricinta.nyc3.digitaloceanspaces.com/assets/"
        base = 'putri-cinta-130-photoset-'
        file = '0'
        
        int = str(n)
        new_int = file+'0'+int+'-1'
        
        name = base+new_int+'.jpg'
        url = root+name
        print(url)

        wget.download(url, name)
        new_int = file+int
    except:
        print('none')