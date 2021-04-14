import sys
import time
import random
import statistics
import re


#   Raja Faizan Nazir
#   F2018065101
#   Assignment 1
#   Opensource Development
#   Submitted to Dr.Ehtisham Ul haq Dar

def firstmethod(str1, str2):  # word to word comparison
    str1temp = str1.split(" ")
    str2temp = str2.split(" ")
    if (len(str1temp) != len(str2temp)) or (str1temp != str2temp):
        return False
    return True


def secondmethod(str1='', str2=''):  # chparing with interning
    if len(str1) != len(str2):
        return False
    str1temp = sys.intern(str1)
    str2temp = sys.intern(str2)
    if str1temp is str2temp:
        return True
    return False


def testfunctionstr(str1='', str2=''):  # automatic testing with random number of tests
    lst1 = []
    lst2 = []
    for i in range(random.randint(2, 100)):
        start = time.time()
        firstmethod(str1, str2)
        end = time.time()
        lst1.append(end - start)

        start = time.time()
        secondmethod(str1, str2)
        end = time.time()
        lst2.append(end - start)

    timedst = {"first": lst1, "second": lst2}
    comparetime(timedst)


def comparetime(times):  # helping function
    t1 = statistics.mean(times['first'])
    t2 = statistics.mean(times['second'])
    if t1 < t2:
        if t1:
            print("First Method (Word-by-word) is " + str(
                round(t2 / t1, 3)) + " times faster than Second Method(Interning)")
            print("-> This is average result based on " + str(len(times['first'])) + " tests <-")
        else:
            print("-> In time calculation, denominator is zero, skipping feature of average time in " + str(
                len(times['first'])) + " tests <-")
            print("First Method (Word-by-word) is " + str(
                "{:.2e}".format(t2 - t1)) + "s (scientific notation) faster than Second Method(Interning)")
    elif t2 < t1:
        if t2:
            print("Second Method (Interning) is " + str(
                round(t1 / t2, 3)) + " times faster than First Method(Word-by-word)")
            print("-> This is average result based on " + str(len(times['first'])) + " tests <-")
        else:
            print("-> In time calculation, denominator is zero, skipping feature of average time in " + str(
                len(times['first'])) + " tests <-")
            print("Second Method (Interning) is " + str(
                "{:.2e}".format(t1 - t2)) + "s (scientific notation) faster than First Method(Word-by-word)")


def removespecialchar(st=''):
    st = st.lower()

    replacewithspace = ['\t', '\n']
    for i in replacewithspace:
        st = st.replace(i, ' ')
    st = re.sub('[^a-z0-9(? /)]+', '', st)
    return st


def word_count(st=''):
    st = removespecialchar(st)
    dst = dict()
    st = st.split(' ')

    for i in st:
        if dst.__contains__(i):
            dst[i] = dst[i] + 1
        else:
            dst[i] = 1
    return dst


st1 = '''Most people are not very familiar with the concept of artificial intelligence (AI). As an illustration, when 1,500 senior business leaders in the United States in 2017 were asked about AI, only 17 percent said they were familiar with it.[1] A number of them were not sure what it was or how it would affect their particular companies. They understood there was considerable potential for altering business processes, but were not clear how AI could be deployed within their own organizations.
Darrell West, director and vice president of Governance Studies. 2/2017
Darrell M. West
Vice President and Director - Governance Studies	Senior Fellow - Center for Technology Innovation	
@DarrWest
John Allen
John R. Allen
President, The Brookings Institution

Despite its widespread lack of familiarity, AI is a technology that is transforming every walk of life. It is a wide-ranging tool that enables people to rethink how we integrate information, analyze data, and use the resulting insights to improve decision making. Our hope through this comprehensive overview is to explain AI to an audience of policymakers, opinion leaders, and interested observers, and demonstrate how AI already is altering the world and raising important questions for society, the economy, and governance.

In this paper, we discuss novel applications in finance, national security, health care, criminal justice, transportation, and smart cities, and address issues such as data access problems, algorithmic bias, AI ethics and transparency, and legal liability for AI decisions. We contrast the regulatory approaches of the U.S. and European Union, and close by making a number of recommendations for getting the most out of AI while still protecting important human values.[2]

In order to maximize AI benefits, we recommend nine steps for going forward:

    Encourage greater data access for researchers without compromising users’ personal privacy,
    invest more government funding in unclassified AI research,
    promote new models of digital education and AI workforce development so employees have the skills needed in the 21st-century economy,
    create a federal AI advisory committee to make policy recommendations,
    engage with state and local officials so they enact effective policies,
    regulate broad AI principles rather than specific algorithms,
    take bias complaints seriously so AI does not replicate historic injustice, unfairness, or discrimination in data or algorithms,
    maintain mechanisms for human oversight and control, and
    penalize malicious AI behavior and promote cybersecurity.'''

st2 = '''Most people are not very familiar with the concept of artificial intelligence (AI). As an illustration, when 1,500 senior business leaders in the United States in 2017 were asked about AI, only 17 percent said they were familiar with it.[1] A number of them were not sure what it was or how it would affect their particular companies. They understood there was considerable potential for altering business processes, but were not clear how AI could be deployed within their own organizations.
Darrell West, director and vice president of Governance Studies. 2/2017
Darrell M. West
Vice President and Director - Governance Studies	Senior Fellow - Center for Technology Innovation	
@DarrWest
John Allen
John R. Allen
President, The Brookings Institution

Despite its widespread lack of familiarity, AI is a technology that is transforming every walk of life. It is a wide-ranging tool that enables people to rethink how we integrate information, analyze data, and use the resulting insights to improve decision making. Our hope through this comprehensive overview is to explain AI to an audience of policymakers, opinion leaders, and interested observers, and demonstrate how AI already is altering the world and raising important questions for society, the economy, and governance.

In this paper, we discuss novel applications in finance, national security, health care, criminal justice, transportation, and smart cities, and address issues such as data access problems, algorithmic bias, AI ethics and transparency, and legal liability for AI decisions. We contrast the regulatory approaches of the U.S. and European Union, and close by making a number of recommendations for getting the most out of AI while still protecting important human values.[2]

In order to maximize AI benefits, we recommend nine steps for going forward:

    Encourage greater data access for researchers without compromising users’ personal privacy,
    invest more government funding in unclassified AI research,
    promote new models of digital education and AI workforce development so employees have the skills needed in the 21st-century economy,
    create a federal AI advisory committee to make policy recommendations,
    engage with state and local officials so they enact effective policies,
    regulate broad AI principles rather than specific algorithms,
    take bias complaints seriously so AI does not replicate historic injustice, unfairness, or discrimination in data or algorithms,
    maintain mechanisms for human oversight and control, and
    penalize malicious AI behavior and promote cybersecurity.'''

if firstmethod(st1, st2):
    print("Strings are equal")
else:
    print("Strings are not equal")
print("-> according to first method(Word-by-Word)")
if secondmethod(st1, st2):
    print("Strings are equal")
else:
    print("Strings are not equal")
print("-> according to second method(Interning)")
testfunctionstr(st1, st2)
if word_count(st1) == word_count(st2):
    print("Strings are equal")
else:
    print("Strings are not equal")
print("-> according to third method(word_count, dictionary)")