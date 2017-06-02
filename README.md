
<code>
<pre>
import urllib
import re
url="http://www.lofter.com/tag/%E6%91%84%E5%BD%B1?act=qbdashboardside_20121217_01"
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="http:\/\/imglf.+jpg"'
    # reg = r'src="(imgf).+(.+\.jpg)"'
    # reg = r'^(http:\/\/imgf).+.jpg'
    # ^(http:\/\/imgs).+.jpg
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x=0
    for imgurl in imglist:
        imgurl=imgurl[5:-2]
        urllib.urlretrieve(imgurl,'%s.jpg' % x)
        x+=1
    return imglist
response=getHtml(url)
print getImg(response)
<pre>
</code>
