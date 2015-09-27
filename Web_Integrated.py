#developed by Saghan Mudbhari 2015
import re
import urllib
positive_count=0
negative_count=0
pos_adj_list=[]
neg_adj_list=[]
op_list=[]
pos_found_adj=[]
neg_found_adj=[]

urlName=raw_input("enter url")
filehandle=urllib.urlopen(urlName,'r')
web_op_file=filehandle.read()
print type(web_op_file)
with open('positive_words.txt','r') as pos_file:
	for line in pos_file:
		#if(line[len(line)-1
		pos_adj_list.append(line[:len(line)-1])


with open('negative_words.txt','r') as neg_file:
	for line in neg_file:
		neg_adj_list.append(line[:len(line)-1])

for line in web_op_file:
		for word in line:
			op_list.append(word)


#print "op string=%s"% op_string
if('' in pos_adj_list):
	 pos_adj_list.remove('')
if('' in neg_adj_list):
	 neg_adj_list.remove('')
if("\n" in pos_adj_list):
	pos_adj_list.remove('\n')
if('\n' in neg_adj_list):
	neg_adj_list.remove('\n')


op_string=''.join(op_list)
op_string=op_string.lower()

for adj in pos_adj_list:
	adj=adj.lower()
	m=re.search(adj,op_string)
	pos_adj_count=op_string.count(adj)
	#print "pos_adj_count=%s for word %s"%(pos_adj_count,adj)
	if( m is not None):
		pos_found_adj.append(adj)
		positive_count+=pos_adj_count


print "these are the positive words found"
print pos_found_adj

for adj in neg_adj_list:
	adj=adj.lower()
	m=re.search(adj,op_string)
	neg_adj_count=op_string.count(adj)
	#print "neg_adj_count=%s for word %s"%(neg_adj_count,adj)
	if( m is not None):
		neg_found_adj.append(adj)
		negative_count+=neg_adj_count

print "these are the negative words found"
print neg_found_adj
print "number of times negative word occurs is"
print negative_count
print "number of times positiive word occurs is"
print positive_count
