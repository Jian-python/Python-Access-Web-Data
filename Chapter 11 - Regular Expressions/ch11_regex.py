import pprint
print('chapter 10 regex')
print('***********part 1***********')
print('1. regular expressions')
pprint.pprint('In computing, a regular expression, also referred as "regex" or "regexp",'
      'provides concise and flexible means for matching strings of text.'
      'for example, particular expression is writen in a formal language that can be '
      'interpreted by regular expression processor ')
print('#####################################################')
print('2. understanding regular expressions')
print('powerful, cryptic','\n','Fun','\n', 'rugular expressions are a language unto themselve','\n',
      'a language of "marker characters" - programming with characters','\n', 'compact and kind of "old school"', sep='')
print('#####################################################')
print('3. The regular expression module')
# import the library by "import re"
print('3.1 use "re.search()" like "find()"')
print('find():')
hand = open('mbox_short.txt')
count = 0
for line in hand:
      line.rstrip()
      if line.find('From:') >=0 :
            print('use find():', line)
            count = count + 1
print(count)
print('re.search():')
import re
hand = open('mbox_short.txt')
count = 0
for line in hand:
      line.rstrip()
      if re.search('From:', line):
            print('use re.search():', line)
            count = count + 1
print(count)
print('#####################################################')
print('3.2 use "re.search()" like "startswith()"')
print('startswith():')
hand = open('mbox_short.txt')
count = 0
for line in hand:
      line.rstrip()
      if line.startswith('From:'):
            print('use startswith():', line)
            count = count + 1
print(count)
import re
hand = open('mbox_short.txt')
count = 0
for line in hand:
      line.rstrip()
      if re.search('^From:', line):
            print('use re.search(^From:):', line)
            count = count + 1
print(count)
print('#####################################################')
print('4. wild-card characters')
print('" ^"：match the start of line')
print('" ."：dot character matches any character')
print('"*"：asterisk character, the character is "any numbers of times"')
import re
hand = open('mbox_short.txt')
for line in hand:
      line.rstrip()
      if re.search('^X.*:',line):
            print(line)
print('#####################################################')
print('5. fine-tuning your match')
print('" ^"：match the start of line')
print('" \S": match any non-whitespace character')
print('" +"：one or more times')
print('"*"：asterisk character, the character is "any numbers of times"')
import re
hand = open('mbox_short.txt')
for line in hand:
      line.rstrip()
      if re.search('^X-\S+:',line):
            print(line)
print('***********part 2***********')
print('6. matching and extracting data')
print('re.search() returns True/False depending on whether the string matches the rs')
print('re.findall(): extracted the matching string')
print('"[0-9]+": one or more digits ')
print('"[AEIOU]+":Are there any uppercase vowels in here?')
import re
x = 'my 2 fAvoritE numbers Are 19 and 42'
y = re.findall('[0-9]+', x)
print(y)
z = re.findall('[AEIOU]+', x)
print(z)
# output: ['A', 'E', 'A']
print('#####################################################')
print('7. greedy matching')
print('* and + push outwars in both directions (greedy)')
# will get "From: Using the:" rather than "From:"
x = 'From: Using the: character'
y = re.findall('^F.+:', x)
print(y)
print('7.1. non-greedy matching')
print('not all regular expression repeat codes are greedy')
print('add "?", * and + non-greedy')
x = 'From: Using the: character'
y = re.findall('^F.+?:', x)
print(y)
print('#####################################################')
print('8. fine-turing string extraction')
import re
x ='From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+@\S+', x)
print('greedy:', x, '\n', y, sep="")
z = re.findall('\S+(\S+?@\S+?)', x)
print('non-greedy:', x, '\n', z, sep="")
print('"()" are not part of the match, the ytll where to start and stop what string to extract')
print('[^ ]: match non-blank chracter')
x ='From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
print('8.1 dual split pattern')
# use re
y = re.findall('@[^ ]*', x)
print(y)
y = re.findall('^From .*@([^ ]*)', x)
print(y)
#  use split
words = x.split()
word = words[1]
z = word.split("@")
print(z[1])
print('#####################################################')
print('9. spam confidence')
import re
hand = open('mbox_short.txt')
numlist = list()
for line in hand:
      line = line.rstrip()
      stuff = re.findall('X-DSPAM-Confidence: ([0-9.]+)', line)
      if len(stuff) != 1: continue
      num = float(stuff[0])
      numlist.append(num)
print('Maximum:', max(numlist))
print('#####################################################')
print('10. Escape character')
print('you want a special regular expression character to just behave normally (most of the time) '
      'you prefix it with " \ " ')
import re
x = ' we want \$10.00 for cookies'
y = re.findall('\$[0-9.]+', x)
print(y)
# ['$10.00']
print('#####################################################')
print('#####################################################')
# =========================summary=========================
print('"^ " Matches the "beginning" of the line.')
#
print('"$" Matches the "end" of the line.')
#
print('"." Matches any character (a wildcard).')
#
print('"\s" Matches a "whitespace" character.')
#
print('"\S" Matches a "non-whitespace" character (opposite of \s).')
#
print('"*" Repeats a character zero or more times.')
#
print('"*?" Repeats a character zero or more times.("non-greedy)')
#
print('"+" Repeats a character one or more times.')
#
print('"+?" Repeats a character one or more times.("non-greedy)')
#
print('"[aeiou]" Matches a single character in the listed set. see section 6')
# import re
# x = 'my 2 fAvoritE numbers Are 19 and 42'
# y = re.findall('[0-9]+', x) means one or more digits
# print(y)
# >>> output: ['2', '19', '42']
# z = re.findall('[AEIOU]+', x) means one or more "A" "E" "I" "O" "U"
# print(z)
# >>>output: ['A', 'E', 'A']
#
print('"[a-z0-9]" You can specify ranges of characters using the minus sign "-".')
# This example is a single character that must be a lowercase letter or a digit.
#
print('"[^XYZ] matches a single character "not in" the listed set.')
# [^A-Za-z]:This example matches a single character that is anything other than an uppercase or lowercase letter.
#
print('"(" Indicates where "string extraction" is to start. ')
#
print('")" Indicates where "string extraction" is to end. ')
# \b Matches the empty string, but only at the start or end of a word.
#
# \B Matches the empty string, but not at the start or end of a word.
#
# \d Matches any decimal digit; equivalent to the set [0-9].
#
# \D Matches any non-digit character; equivalent to the set [^0-9].
# ==================================================