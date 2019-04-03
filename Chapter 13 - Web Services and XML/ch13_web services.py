print('chapter 12 Python and Web Services')
print('***********part 1***********')
print('1. data on the web')

# with the HTTP Request/Response well understood and well suppported, there was a natural move
# towards exchanging data between programs using thes eptocols

# we nne to come up with an agreed way to represent data going between applications
# and across networks

# there are two commonly used formats: XML and JSON
print('#####################################################')

print('2. agreeing on a "wire format"')

# python data ->"serilize"  wire format: <person> <name>chuck</name>,<phone>303 4456</phone>...->"de-serialize"->Java HashMap

print('the two serilization formats we learnt: XML and JSON ')
print('#####################################################')

print('***********part 2***********')
print('3. XML:')
print('3.1 XML "Elements" or Nodes')
print('primary purpose: help information systems share structured data')
# It started as a simplified subset of the Standard Generalized Markup Language(SGML), and is designe to be relatively
# human-legible

# see note for details

# tags: indicate the beginning and ending of elements
# attributes: keywords/value pairs on the opening tags of XML
# serialize/de-serialize: convert data in one program into a common format that can be
# stored and/or transmitted between systems in a programming language-independent manner
print('#####################################################')
print('***********part 3***********')
print('4. XML Schema')
# description of the legal format of a XML document
# expressed in terms of constraints on the structure and content of documents
# often used to specify a "contract" between systems - "my system will only accept XML that
# conforms to this particular Schema"
# If a particular piece of XML meets the specofocatin of the Schema - it is said to "validate"

# Document Type Defination (DTD)
# Standard Generalized Markup Language (SGML)
# XML Schema from W3C (World Wide Web Consortium) - (XSD) <-important file name end in .xsd

# ISO 8601 Date/Time Format:
# 2002-05-30T09:30:10Z
# Z: timezone: UTC or GMT
print('#####################################################')
print('***********part 4***********')
print('5. Parsing XML')
print('\nexample1:\n')
import xml.etree.cElementTree as ET
data = '''<person>
    <name>Chuck</name>name>
    <phone type="intl">
        +1 734 303 4456
    </phone>>
    <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name'). text)
print('phone:', tree.find('phone'). text)
print('Attr:', tree.find('phone').get('type'))
print('Attr:', tree.find('email').get('hide'))
print('\nexample2:\n')
import xml.etree.cElementTree as ET
input = '''<stuff>
    <users>
            <user x ="2">
                <id>001</id>
                <name>Chuck</name>
            </user>
            <user x = "7">
                <id>009</id>
                <name>Brent</name>
            </user>
    </users>

</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('users count:', len(lst))
for item in lst:
    print('Name:', item.find('name').text)
    print('id:', item.find('id').text)
    print('Attribute:', item.get('x'))


print('#####################################################')
