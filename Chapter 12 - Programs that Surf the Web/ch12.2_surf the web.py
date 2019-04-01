print('chapter 12.2 Programs that Surf the Web')
print('***********part 1***********')
print('1. representing simple strings')
print('the "ord()" function tells the numeric value of a simple ASCII character')
# each character is represented by a number between 0 and 256 stored in 8 bits of memory
# we prefer '8 bits of memory' as 'a "byte" of memory'
print('H:', ord('H'))
print('h:', ord('h'))
print('e:', ord('e'))
print('#####################################################')
print('2. multi-byte characters')
# UTF-16: fixed length - 2 bytes
# UTF-32: fixed length - 4 bytes
# UTF-8: 1-4 bytes (recommended practice for exchange data between systems)
print('#####################################################')
print('3. Python strings to bytes')
# when send bytes to external resources like a network socket: encode Python 3 into given character encoding
# when read data from external resource, we decode it based on the character set so it represented in python 3 as string
# code:===========================
# while True:
#     data = mysock.recv(512)
#     if (len(data)<1):
#         break
#     mystring = data.decode() <-decode: bytes to unicode
#     print(mystring)
# =================================
print('#####################################################')
print('4. Using urllib in Python')
# urllib does all socket work and makes web paegs look like a  file
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip()) #strip() remove the newline between lines
print('#####################################################')
print('5. like a file...')
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
count = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        count[word] = count.get(word, 0) + 1
print(count)
print('#####################################################')
print('6. reading web pages')
# read HTML file
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand:
    print(line.decode().strip())
# output:==============
# <h1>The First Page</h1>
# <p>
# If you like, you can switch to the
# <a href="http://www.dr-chuck.com/page2.htm">
# Second Page</a>.
# </p>
# ======================
print('#####################################################')
print('7. web scraping')
# program / script pretends to be web browser and restrieves web pages, llok at those pages,
#  extracts info, and look at more web pages

print('web scrawling or spidering the web:','\n','search engines scrape web pages', sep='')
print('#####################################################')
print('8. beautiful soup')
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
# .read() read all lines include newline at end of each line, and all come into a big string
soup = BeautifulSoup(html, 'html.parser')
# parse: clean up nasty html into tree
# restrieve all of the anchor tags
tags = soup('a')
# find out all the tag <a xxxxxxxx </a>
for tag in tags:
    print(tag.get('href', None))
# input:
# Enter - >? http://www.dr-chuck.com/page1.htm
# output:
# http://www.dr-chuck.com/page2.htm

#  try more complex one: http://www.dr-chuck.com 
