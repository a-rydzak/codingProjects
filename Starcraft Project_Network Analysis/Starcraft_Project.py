import zen
import numpy
import math
import sys
import copy
sys.path.append('C:\Users\BroBoFett\Desktop\Starcraft Project\zend3js\zend3js')
import d3js
import randomnet
import numpy
import random
import matplotlib.pyplot as plt

#def cocitation(H):
#	G_cocitation = zen.Graph()
#	N=H.num_nodes
#	for i in range(0,N): # add nodes first... keep their names!
#		G_cocitation.add_node(H.node_object(i))
#	for i in range(0,N):
#		for j in range (i+1,N): 
#			nbrs_i = H.in_neighbors_(i)
#			nbrs_j = H.in_neighbors_(j) ##?  indicies here
#			x=set(nbrs_i).intersection(set(nbrs_j))# The total intersection amount between neighbors of i and j
#			if len(x) > 0:
#				cusum = 0
#				for k in x:
#					cusum += H.weight_(H.edge_idx_(k,i)) * H.weight_(H.edge_idx_(k,j))
#				G_cocitation.add_edge_(i,j, weight=cusum) ##?  indicies here
#	return G_cocitation



###=============================================Cocitation strength between nodes=======
#G = zen.io.edgelist.read('C:\Users\BroBoFett\Desktop\Starcraft Project\Starcraft.edgelist', directed=True)#
G = zen.io.gml.read('C:\Users\BroBoFett\Desktop\Starcraft Project\Starcraft_Graph.gml')
#
A=G.matrix().transpose()
C1 = numpy.dot(A,A.transpose())
Storage=[]
for a in range (0,G.num_nodes):
	for b in range (0,G.num_nodes):
		if not G.has_edge_(a,b) and not G.has_edge_(b,a) and (a != b) and (C1[a,b] > 0) :
			Storage.append([G.node_object(a),G.node_object(b),C1[a,b]])
			
			
###Sorting Function!!!!!!!!!!!!!!!!!!!!!!!!!!
for j in range (0,1000):
	empty=['e']
	for i in range (1, len(Storage)):
		if Storage[i-1][2] < Storage[i][2]:
			empty[0]=Storage[i]
			Storage[i] = Storage[i-1]
			Storage[i-1] = empty[0]





Top_10=[]
for i in range (0,20):
	Top_10.append(Storage[i])
	
print Top_10 ###Top Ten Rivals Rivals are repeated so 20 will produce 10 actual rivals


###======================Network Characteristics
 
#print zen.diameter(G)  #Diameter of the network
#print G.num_nodes      #Number of nodes in the network 
#print G.num_Edges      #Number of edges in the network

##Cocitation Loop
#A=G.matrix().transpose()
#C1 = numpy.dot(A,A.transpose())
#print C1[252,99]
#print C1[99,252]
#
#C2=numpy.dot(A.transpose(),A)
#print C2[252,99]
#print C2[99,252]
###============================================Network Visualizer
#d3 = d3js.D3jsRenderer(G,interactive=False)
#### d3.clear() - this removes the graph - you don't want to do this.
#d3.update() # when interactive=False, you need to call this to make the visualization update 
##
#d3.stop_server()
#print G.num_edges
#print G.num_nodes
#d = zen.diameter(G)
#print d
###=========================================Degree Distribution
#G=zen.DiGraph()
#G= zen.io.gml.read('C:\Users\BroBoFett\Desktop\Starcraft Project\Starcraft_Graph.gml')
#
#cddlist=zen.degree.cddist(G,inverse=True) #array that tells you the culmitative degree distribution of each degree k (0,1,2,3...)" 
#ddlist_true=zen.degree.ddist(G,normalize=True) #array that tells the fraction of nodes with degree of K (0,1,2,3...)" 
#ddlist_false=zen.degree.ddist(G,normalize=False)#"An array that tells how many nodes have a degree of K (0,1,2,3...)" 
#
#k = numpy.arange(len(ddlist_true))
#plt.figure(figsize=(8,12))
#plt.subplot(211)
#plt.title('Starcraft Network')
#plt.xlabel('Degrees')
#plt.ylabel('Fraction of degree distribution')
#plt.bar(k,ddlist_true, width=1, bottom=0, color='b')
#
#plt.subplot(212)
#plt.xlabel('Degrees')
#plt.ylabel('Cumulative degree distribution')
#plt.loglog(k,cddlist)
#plt.show()

####=========================================Power Law, does follow the power law

#cddlist=zen.degree.cddist(G,inverse=True) #array that tells you the culmitative degree distribution of each degree k (0,1,2,3...)" 
#ddlist_true=zen.degree.ddist(G,normalize=True) #array that tells the fraction of nodes with degree of K (0,1,2,3...)" 
#ddlist_false=zen.degree.ddist(G,normalize=False)#"An array that tells how many nodes have a degree of K (0,1,2,3...)" 
#
#aa = numpy.arange(len(ddlist_false)) ###
#def calc_aplha_val(ddlist_false,kmin):  
#    count = 0 #tracks the index that a degree larger than Kmin is found at
#    q= 0 #This is the sum of all ln(ki/(kmin-(.5)))
#    for i in range (0,len(ddlist_false)):
#        if aa[i] >= kmin: ############need to compare index here, changed 
#            count += ddlist_false[i] #turn the degree number corresponding to the index
#            q += ddlist_false[i]* (math.log((aa[i])/(kmin-0.5)))
#    print '\nNumber of nodes with degree greater than Kmin='
#    print count
#    print '\nAlpha='
#    print 1+count*(1/q)
#	
#calc_aplha_val(ddlist_false, 19)
#
#k = numpy.arange(len(ddlist_true))
#					 
#plt.figure(figsize=(8,12))
#plt.subplot(211)
#plt.title('Starcraft Network Degree Distribution')
#plt.xlabel('Degrees')
#plt.ylabel('Fraction of degree distribution')
#plt.bar(k,ddlist_true, width=1, bottom=0, color='b')
#
#plt.subplot(212)
#plt.xlabel('Degrees')
#plt.ylabel('Cumulative degree distribution')
#plt.loglog(k,cddlist)
#plt.show()
##+==============================================Network Motif  Two Node lines, there are 728
#Storage2=[]
#for a in range (0,G.num_nodes):
#	for b in range (0,G.num_nodes):
#		if G.has_edge_(a,b) and G.has_edge_(b,a) and (a!=b):
#			Storage2.append([G.node_object(a),G.node_object(b)])
#
#t=[]
#for x in range (0,len(Storage2)):
#	if int(len(set(Storage2[x]))) == 2:
#		t.append((Storage2[x]))
#tt= map(list, set(map(frozenset, t)))
#
#for i in range (0, len(tt)):
#	A=tt[i][0]
#	B=tt[i][1]
#	weight= G.weight(G.node_object(G.node_idx(A)),G.node_object(G.node_idx(B))) +  G.weight(G.node_object(G.node_idx(B)),G.node_object(G.node_idx(A)))	
#	tt[i].append(weight)
#
#	
#for j in range (0,5000):
#	empty=['e']
#	for i in range (1, len(tt)):
#		if tt[i-1][2] < tt[i][2]:
#			empty[0]=tt[i]
#			tt[i] = tt[i-1]
#			tt[i-1] = empty[0]
#
#
#Top_10=[]
#for i in range (0,10):
#	Top_10.append(tt[i])
#	
#print Top_10 ###Top Ten Rivals
###=============================================Network Motif, Three node lines, 737

#Storage2=[]
#score=0
#for a in range (0,G.num_nodes):
#	for b in range (0,G.num_nodes):
#		if (G.has_edge_(a,b) and G.has_edge_(b,a)) and (a!=b):
#			for c in range (0,G.num_nodes):
#				if G.has_edge_(b,c) and G.has_edge_(c,b) and not G.has_edge_(a,c) and not G.has_edge_(c,a) and (a!=b) and (b!=c) and (c!=a):
#					Storage2.append([G.node_object(a),G.node_object(b),G.node_object(c)])
#				
## Creatus unique sets 
#t=[]
#for x in range (0,len(Storage2)):
#	if int(len(set(Storage2[x]))) == 3:
#		t.append((Storage2[x]))
#tt= map(list, set(map(frozenset, t)))
#
#
#for i in range (0, len(tt)):
#	A=tt[i][0]
#	B=tt[i][1]
#	C=tt[i][2]
#	if not G.weight(G.node_object(G.node_idx(A)),G.node_object(G.node_idx(C))) or G.weight(G.node_object(G.node_idx(C)),G.node_object(G.node_idx(A))):
#		weight= G.weight(G.node_object(G.node_idx(A)),G.node_object(G.node_idx(B))) + G.weight(G.node_object(G.node_idx(B)),G.node_object(G.node_idx(A))) +G.weight(G.node_object(G.node_idx(B)),G.node_object(G.node_idx(C))) + G.weight(G.node_object(G.node_idx(C)),G.node_object(G.node_idx(B))) 	
#		tt[i].append(weight)
#
#
#for j in range (0,5000):
#	empty=['e']
#	for i in range (1, len(tt)):
#		if tt[i-1][3] < tt[i][3]:
#			empty[0]=tt[i]
#			tt[i] = tt[i-1]
#			tt[i-1] = empty[0]
#
#
#Top_10=[]
#for i in range (0,10):
#	Top_10.append(tt[i])
#	
#print Top_10 ###Top Ten Rivals



###====================================================Network Motif, Triangle there are 180
    
#Storage=[]
#score=0
#for a in range (0,G.num_nodes):
#	for b in range (0,G.num_nodes):
#		if G.has_edge_(a,b) and G.has_edge_(b,a) and (a!=b):
#			for c in range (0,G.num_nodes):
#				if G.has_edge_(a,b) and G.has_edge_(b,a) and G.has_edge_(b,c) and G.has_edge_(c,b) and G.has_edge_(a,c) and G.has_edge_(c,a) and (a!=b) and (b!=c) and (a!=c):
#					Storage.append([G.node_object(a),G.node_object(b),G.node_object(c)])
#t=[]
#for x in range (0,len(Storage)):
#	if int(len(set(Storage[x]))) == 3:
#		t.append((Storage[x]))
#tt= map(list, set(map(frozenset, t)))
#
#
#for i in range (0, len(tt)):
#	A=tt[i][0]
#	B=tt[i][1]
#	C=tt[i][2]
#	weight= G.weight(G.node_object(G.node_idx(A)),G.node_object(G.node_idx(B))) + G.weight(G.node_object(G.node_idx(B)),G.node_object(G.node_idx(A))) +G.weight(G.node_object(G.node_idx(B)),G.node_object(G.node_idx(C))) + G.weight(G.node_object(G.node_idx(C)),G.node_object(G.node_idx(B))) + G.weight(G.node_object(G.node_idx(A)),G.node_object(G.node_idx(C)))  + G.weight(G.node_object(G.node_idx(C)),G.node_object(G.node_idx(A)))
#	tt[i].append(weight)
#
#for j in range (0,5000):
#	empty=['e']
#	for i in range (1, len(tt)):
#		if tt[i-1][3] < tt[i][3]:
#			empty[0]=tt[i]
#			tt[i] = tt[i-1]
#			tt[i-1] = empty[0]
#
#
#Top_10=[]
#for i in range (0,10):
#	Top_10.append(tt[i])
#	
#print Top_10 ###Top Ten Rivals

##====================================================Network Motif Square, 4 nodes				
#Storage3=[]
#score=0
#for a in range (0,G.num_nodes):
#	for b in range (0,G.num_nodes):
#		if G.has_edge_(a,b) and G.has_edge_(b,a) and (a!=b):
#			for c in range (0,G.num_nodes):
#				if ((G.has_edge_(a,b) and G.has_edge_(b,a) and G.has_edge_(b,c) and G.has_edge_(c,b))) or ((G.has_edge_(a,b) and G.has_edge_(b,a) and G.has_edge_(a,c) and G.has_edge_(c,a))) and (a!=b) and (b!=c) and (a!=c):
#					for d in range (0,G.num_nodes):
#						if G.has_edge_(a,b) and G.has_edge_(b,a) and G.has_edge_(b,c) and G.has_edge_(c,b) and G.has_edge_(a,d) and G.has_edge_(d,a) and G.has_edge_(c,d) and G.has_edge_(d,c) and not G.has_edge_(a,c) and not G.has_edge_(c,a) and not G.has_edge_(d,b) and not G.has_edge_(b,d) and (a!=b) and (b!=c) and (a!=c) and (d!=a) and (d!=c) and (d!=b) :
#							Storage3.append([G.node_object(a),G.node_object(b),G.node_object(c),G.node_object(d)])
#
#t=[]
#for x in range (0,len(Storage3)):
#	if int(len(set(Storage3[x]))) == 4:
#		t.append((Storage3[x]))
#tt= map(list, set(map(frozenset, t)))
#
#
#for i in range (0, len(tt)):
#	A=tt[i][0]
#	B=tt[i][1]
#	C=tt[i][2]
#	D=tt[i][3]
#	weight= G.weight(G.node_object(G.node_idx(A)),G.node_object(G.node_idx(B))) + G.weight(G.node_object(G.node_idx(B)),G.node_object(G.node_idx(A))) +G.weight(G.node_object(G.node_idx(B)),G.node_object(G.node_idx(C))) + G.weight(G.node_object(G.node_idx(C)),G.node_object(G.node_idx(B))) + G.weight(G.node_object(G.node_idx(D)),G.node_object(G.node_idx(A)))  + G.weight(G.node_object(G.node_idx(A)),G.node_object(G.node_idx(D)))  + G.weight(G.node_object(G.node_idx(D)),G.node_object(G.node_idx(C)))  + G.weight(G.node_object(G.node_idx(C)),G.node_object(G.node_idx(D)))  
#	tt[i].append(weight)
#
#
#for j in range (0,5000):
#	empty=['e']
#	for i in range (1, len(tt)):
#		if tt[i-1][4] < tt[i][4]:
#			empty[0]=tt[i]
#			tt[i] = tt[i-1]
#			tt[i-1] = empty[0]
#
#
#Top_10=[]
#for i in range (0,10):
#	Top_10.append(tt[i])
#	
#print Top_10 ###Top Ten Rivals
####===================================Network Motif Square, 5 Node, rivaliry graph, where A and E are rivals, A and E count only have in Degrees,
#Storage4=[]
#score=0
#Score_store=[]
#for a in range (0,G.num_nodes):
#	for b in range (0,G.num_nodes):
#		if (G.has_edge_(a,b) or G.has_edge_(b,a)) and (a != b) :
#			for c in range (0,G.num_nodes):
#				if (G.has_edge_(a,b) or G.has_edge_(b,a)) and (G.has_edge_(a,c) or G.has_edge_(c,a)) and G.has_edge_(c,b) and G.has_edge_(b,c) and (a!=b) and (b!=c) and (a!=c): 
#					for d in range (0,G.num_nodes):
#						if (G.has_edge_(a,b) or G.has_edge_(b,a)) and (G.has_edge_(a,c) or G.has_edge_(c,a)) and (G.has_edge_(d,a) or G.has_edge_(a,d)) and G.has_edge_(c,b) and G.has_edge_(b,c) and G.has_edge_(b,d) and G.has_edge_(d,b) and G.has_edge_(d,c) and G.has_edge_(c,d) and (a!=b) and (b!=c) and (a!=c) and (d!=a) and (d!=c) and (d!=b):
#							for e in range (0,G.num_nodes):
#								if (G.has_edge_(a,b) or G.has_edge_(b,a)) and (G.has_edge_(a,c) or G.has_edge_(c,a)) and (G.has_edge_(d,a) or G.has_edge_(a,d)) and G.has_edge_(c,b) and G.has_edge_(b,c) and G.has_edge_(b,d) and G.has_edge_(d,b) and G.has_edge_(d,c) and G.has_edge_(c,d) and (G.has_edge_(e,b) or G.has_edge_(b,e)) and (G.has_edge_(e,c) or G.has_edge_(c,e)) and (G.has_edge_(d,e) or G.has_edge_(e,d)) and not G.has_edge_(a,e) and not G.has_edge_(e,a) and (a!=b) and (b!=c) and (a!=c) and (d!=a) and (d!=c) and (d!=b) and (e!=a) and (e!=b) and (e!=c) and (e!=d) :
#									Storage4.append(([G.node_object(a),G.node_object(b),G.node_object(c),G.node_object(d), G.node_object(e)]))
#t=[]
#for x in range (0,len(Storage4)):
#	if int(len(set(Storage4[x]))) == 5:
#		t.append(sorted(Storage4[x]))
#tt= map(list, set(map(frozenset, t)))
#
#for i in range (0, len(tt)):
#	A=tt[i][0]
#	B=tt[i][1]
#	C=tt[i][2]
#	D=tt[i][3]
#	E=tt[i][4]
#	
#	weight_triangle=G.weight(G.node_object(G.node_idx(B)),G.node_object(G.node_idx(C)))+ G.weight(G.node_object(G.node_idx(C)),G.node_object(G.node_idx(B))) +G.weight(G.node_object(G.node_idx(B)),G.node_object(G.node_idx(D))) +G.weight(G.node_object(G.node_idx(D)),G.node_object(G.node_idx(B))) +G.weight(G.node_object(G.node_idx(D)),G.node_object(G.node_idx(C))) +G.weight(G.node_object(G.node_idx(C)),G.node_object(G.node_idx(D))) 
#	
#	wins_a=G.weight(G.node_object(G.node_idx(B)),G.node_object(G.node_idx(A)))+ G.weight(G.node_object(G.node_idx(C)),G.node_object(G.node_idx(A)))+G.weight(G.node_object(G.node_idx(D)),G.node_object(G.node_idx(A)))
#	
#	win_b=G.weight(G.node_object(G.node_idx(B)),G.node_object(G.node_idx(E)))+ G.weight(G.node_object(G.node_idx(C)),G.node_object(G.node_idx(E)))+G.weight(G.node_object(G.node_idx(D)),G.node_object(G.node_idx(E)))
#	
#	weight= G.weight(G.node_object(G.node_idx(B)),G.node_object(G.node_idx(A))) + G.weight(G.node_object(G.node_idx(C)),G.node_object(G.node_idx(A))) + G.weight(G.node_object(G.node_idx(D)),G.node_object(G.node_idx(A)))+ G.weight(G.node_object(G.node_idx(B)),G.node_object(G.node_idx(E)))+ G.weight(G.node_object(G.node_idx(C)),G.node_object(G.node_idx(E)))+ G.weight(G.node_object(G.node_idx(D)),G.node_object(G.node_idx(E)))+ G.weight(G.node_object(G.node_idx(B)),G.node_object(G.node_idx(C)))+ G.weight(G.node_object(G.node_idx(C)),G.node_object(G.node_idx(B)))+ G.weight(G.node_object(G.node_idx(C)),G.node_object(G.node_idx(D)))+ G.weight(G.node_object(G.node_idx(D)),G.node_object(G.node_idx(C)))+ G.weight(G.node_object(G.node_idx(D)),G.node_object(G.node_idx(B)))+ G.weight(G.node_object(G.node_idx(B)),G.node_object(G.node_idx(D))) 	
#	
#	tt[i].append(weight)
#	tt[i].append(weight_triangle)
#	tt[i].append(wins_a)
#	tt[i].append(win_b)
#
#
#for j in range (0,5000):
#	empty=['e']
#	for i in range (1, len(tt)):
#		if tt[i-1][5] < tt[i][5]:
#			empty[0]=tt[i]
#			tt[i] = tt[i-1]
#			tt[i-1] = empty[0]
#
#
#Top_10=[]
#for i in range (0,10):
#	Top_10.append(tt[i])
#	
#print Top_10 ###Top Ten Rivals
##-----------------------------------------------------------------TEST CODE AND OTHER GRAPHLETS HERE!!!---------------------------------------------------------------
##print G.weight(G.node_object(G.node_idx('puCK')),G.node_object( G.node_idx('Bly')))
##print G.weight(G.node_object(G.node_idx('Bly')),G.node_object( G.node_idx('puCK')))
##print G.weight(G.node_object(G.node_idx('HuK')),G.node_object( G.node_idx('Snute')))
##print G.weight(G.node_object(G.node_idx(tt[0][0])),G.node_object(G.node_idx(tt[0][4])))
##G.has_edge_(b,c) and G.has_edge_(c,b) and G.has_edge_(c,d)  and G.has_edge_(d,c)  and G.has_edge_(d,b) and G.has_edge_(b,d) and G.has_edge_(b,a) and G.has_edge_(c,a) and G.has_edge_(d,a) and G.has_edge_(b,e) and G.has_edge_(c,e)  and G.has_edge_(d,e) and not G.has_edge_(a,b) and not G.has_edge_(a,c) and not G.has_edge_(a,d) and not G.has_edge_(a,e) and not G.has_edge_(e,a) and not G.has_edge_(e,b) and not G.has_edge_(e,c) and not G.has_edge_(e,d)

####===================================================================6 node pyramid, there are 0, Graphlet
#Storage=[]
#score=0
#for a in range (0,G.num_nodes):
#	for b in range (0,G.num_nodes):
#		for c in range (0,G.num_nodes):
#			if G.has_edge_(a,b) and G.has_edge_(b,a) and G.has_edge_(b,c) and G.has_edge_(c,b) and G.has_edge_(a,c) and G.has_edge_(c,a):
#				for d in range (0,G.num_nodes):
#					if G.has_edge_(a,b) and G.has_edge_(b,a) and G.has_edge_(b,c) and G.has_edge_(c,b) and G.has_edge_(a,c) and G.has_edge_(c,a) and G.has_edge_(a,d) and G.has_edge_(d,a) and G.has_edge_(d,b) and G.has_edge_(b,d) and G.has_edge_(d,c) and G.has_edge_(c,d):
#						for e in range (0,G.num_nodes):
#							if G.has_edge_(a,b) and G.has_edge_(b,a) and G.has_edge_(b,c) and G.has_edge_(c,b) and G.has_edge_(a,c) and G.has_edge_(c,a) and G.has_edge_(a,d) and G.has_edge_(d,a) and G.has_edge_(d,b) and G.has_edge_(b,d) and G.has_edge_(d,c) and G.has_edge_(c,d)  and G.has_edge_(a,e) and G.has_edge_(e,a) and G.has_edge_(b,e) and G.has_edge_(e,b) and G.has_edge_(e,c) and G.has_edge_(c,e) and G.has_edge_(e,d) and G.has_edge_(d,e):
#								for f in range (0,G.num_nodes):
#									if G.has_edge_(a,b) and G.has_edge_(b,a) and G.has_edge_(b,c) and G.has_edge_(c,b) and G.has_edge_(a,c) and G.has_edge_(c,a) and G.has_edge_(a,d) and G.has_edge_(d,a) and G.has_edge_(d,b) and G.has_edge_(b,d) and G.has_edge_(d,c) and G.has_edge_(c,d)  and G.has_edge_(a,e) and G.has_edge_(e,a) and G.has_edge_(b,e) and G.has_edge_(e,b) and G.has_edge_(e,c) and G.has_edge_(c,e) and G.has_edge_(e,d) and G.has_edge_(d,e) and G.has_edge_(a,f) and G.has_edge_(f,a) and G.has_edge_(b,f) and G.has_edge_(f,b) and G.has_edge_(f,c) and G.has_edge_(c,f) and G.has_edge_(f,d) and G.has_edge_(d,f):
#										Storage.append([G.node_object(e),G.node_object(a),G.node_object(b),G.node_object(c),G.node_object(d),G.node_object(f)])
#t=[]
#for x in range (0,len(Storage)):
#	if int(len(set(Storage[x]))) == 6:
#		t.append(sorted(Storage[x]))
#tt= map(list, set(map(frozenset, t)))
#print tt

####==============================================================5 node pyramid, there are 0, Graphlet
#Storage=[]
#score=0
#for a in range (0,G.num_nodes):
#	for b in range (0,G.num_nodes):
#		for c in range (0,G.num_nodes):
#			if G.has_edge_(a,b) and G.has_edge_(b,a) and G.has_edge_(b,c) and G.has_edge_(c,b) and G.has_edge_(a,c) and G.has_edge_(c,a):
#				for d in range (0,G.num_nodes):
#					if G.has_edge_(a,b) and G.has_edge_(b,a) and G.has_edge_(b,c) and G.has_edge_(c,b) and G.has_edge_(a,c) and G.has_edge_(c,a) and G.has_edge_(a,d) and G.has_edge_(d,a) and G.has_edge_(d,b) and G.has_edge_(b,d) and G.has_edge_(d,c) and G.has_edge_(c,d):
#						for e in range (0,G.num_nodes):
#							if G.has_edge_(a,b) and G.has_edge_(b,a) and G.has_edge_(b,c) and G.has_edge_(c,b) and G.has_edge_(a,c) and G.has_edge_(c,a) and G.has_edge_(a,d) and G.has_edge_(d,a) and G.has_edge_(d,b) and G.has_edge_(b,d) and G.has_edge_(d,c) and G.has_edge_(c,d)  and G.has_edge_(a,e) and G.has_edge_(e,a) and G.has_edge_(b,e) and G.has_edge_(e,b) and G.has_edge_(e,c) and G.has_edge_(c,e) and G.has_edge_(e,d) and G.has_edge_(d,e):
#								Storage.append([G.node_object(a),G.node_object(b),G.node_object(c),G.node_object(d),G.node_object(e)])
##						
#						
#t=[]
#for x in range (0,len(Storage)):
#	if int(len(set(Storage[x]))) == 5:
#		t.append(sorted(Storage[x]))
#tt= map(list, set(map(frozenset, t)))
#print tt

##====================================================Network Motif Square, 5 Node, planer
#Storage4=[]
#score=0
#for a in range (0,G.num_nodes):
#	for b in range (0,G.num_nodes):
#		for c in range (0,G.num_nodes):
#			if G.has_edge_(a,b) and G.has_edge_(b,a) and G.has_edge_(b,c) and G.has_edge_(c,b) and G.has_edge_(a,c) and G.has_edge_(c,a):
#				for d in range (0,G.num_nodes):
#					if G.has_edge_(a,b) and G.has_edge_(b,a) and G.has_edge_(b,c) and G.has_edge_(c,b) and G.has_edge_(a,c) and G.has_edge_(c,a) and G.has_edge_(a,d) and G.has_edge_(d,a) and G.has_edge_(d,b) and G.has_edge_(b,d) and G.has_edge_(d,c) and G.has_edge_(c,d):
#						for e in range (0,G.num_nodes):
#							if G.has_edge_(a,b) and G.has_edge_(b,a) and G.has_edge_(b,c) and G.has_edge_(c,b) and G.has_edge_(a,c) and G.has_edge_(c,a) and G.has_edge_(a,d) and G.has_edge_(d,a) and G.has_edge_(d,b) and G.has_edge_(b,d) and G.has_edge_(d,c) and G.has_edge_(c,d) and G.has_edge_(e,a) and G.has_edge_(a,e) and G.has_edge_(e,b) and G.has_edge_(b,e) and G.has_edge_(e,c) and G.has_edge_(c,e):
#								Storage4.append([G.node_object(d),G.node_object(a),G.node_object(b),G.node_object(c), G.node_object(e)])
#	
### Creatus unique sets of 5
#t=[]
#for x in range (0,len(Storage4)):
#	if int(len(set(Storage4[x]))) == 5:
#		t.append(sorted(Storage4[x]))
#tt= map(list, set(map(frozenset, t)))
#print tt
#
##====================================================Network Motif , 4 Node Pyramid,Planer, There are 2
#Storage=[]
#score=0
#for a in range (0,G.num_nodes):
#	for b in range (0,G.num_nodes):
#		for c in range (0,G.num_nodes):
#			if G.has_edge_(a,b) and G.has_edge_(b,a) and G.has_edge_(b,c) and G.has_edge_(c,b) and G.has_edge_(a,c) and G.has_edge_(c,a):
#				for d in range (0,G.num_nodes):
#					if G.has_edge_(a,b) and G.has_edge_(b,a) and G.has_edge_(b,c) and G.has_edge_(c,b) and G.has_edge_(a,c) and G.has_edge_(c,a) and G.has_edge_(a,d) and G.has_edge_(d,a) and G.has_edge_(d,b) and G.has_edge_(b,d) and G.has_edge_(d,c) and G.has_edge_(c,d):
#						score= G.weight(G.node_object(a),G.node_object(b)) +  G.weight(G.node_object(b),G.node_object(a)) + G.weight(G.node_object(b),G.node_object(c)) +G.weight(G.node_object(c),G.node_object(b)) +G.weight(G.node_object(c),G.node_object(a)) +G.weight(G.node_object(a),G.node_object(c)) +G.weight(G.node_object(d),G.node_object(a)) + G.weight(G.node_object(a),G.node_object(d)) + G.weight(G.node_object(d),G.node_object(b))+G.weight(G.node_object(b),G.node_object(d)) + G.weight(G.node_object(c),G.node_object(d)) +G.weight(G.node_object(d),G.node_object(c))
#						Storage.append(([G.node_object(a),G.node_object(b),G.node_object(c),G.node_object(d)]))
#t=[]
#for x in range (0,len(Storage)):
#	if int(len(set(Storage[x]))) == 4:
#		t.append(sorted(Storage[x]))
#tt= map(list, set(map(frozenset, t)))
#print tt
#
##==============================================Network Motif Square, 4 nodes, with two diagonal between (a and c) and (b and d), there are two
#Storage3=[]
#score=0
#for a in range (0,G.num_nodes):
#	for b in range (0,G.num_nodes):
#		if G.has_edge_(a,b) and G.has_edge_(b,a):
#			for c in range (0,G.num_nodes):
#				if ((G.has_edge_(a,b) and G.has_edge_(b,a) and G.has_edge_(b,c) and G.has_edge_(c,b))) or ((G.has_edge_(a,b) and G.has_edge_(b,a) and G.has_edge_(a,c) and G.has_edge_(c,a))):
#					for d in range (0,G.num_nodes):
#						if G.has_edge_(a,b) and G.has_edge_(b,a) and G.has_edge_(b,c) and G.has_edge_(c,b) and G.has_edge_(a,d) and G.has_edge_(d,a) and G.has_edge_(c,d) and G.has_edge_(d,c) and G.has_edge_(a,c) and G.has_edge_(c,a) and G.has_edge_(d,b)  and G.has_edge_(b,d):
#							score= G.weight(G.node_object(a),G.node_object(b)) +  G.weight(G.node_object(b),G.node_object(a)) + G.weight(G.node_object(b),G.node_object(c)) +  G.weight(G.node_object(c),G.node_object(b)) + G.weight(G.node_object(c),G.node_object(d)) +  G.weight(G.node_object(d),G.node_object(c)) + G.weight(G.node_object(a),G.node_object(d)) +  G.weight(G.node_object(d),G.node_object(a))+ G.weight(G.node_object(a),G.node_object(c))+ G.weight(G.node_object(c),G.node_object(a)) +G.weight(G.node_object(d),G.node_object(b)) + G.weight(G.node_object(b),G.node_object(d))
#							Storage3.append([G.node_object(a),G.node_object(b),G.node_object(c),G.node_object(d)])
#t=[]
#for x in range (0,len(Storage3)):
#	if int(len(set(Storage3[x]))) == 4:
#		t.append(sorted(Storage3[x]))
#tt= map(list, set(map(frozenset, t)))
#print tt
##====================================================Network Motif Square, 4 nodes, with one diagonal between a and c, there are 29, DO we want to display?????????
#Storage3=[]
#score=0
#for a in range (0,G.num_nodes):
#	for b in range (0,G.num_nodes):
#		if G.has_edge_(a,b) and G.has_edge_(b,a):
#			for c in range (0,G.num_nodes):
#				if ((G.has_edge_(a,b) and G.has_edge_(b,a) and G.has_edge_(b,c) and G.has_edge_(c,b))) or ((G.has_edge_(a,b) and G.has_edge_(b,a) and G.has_edge_(a,c) and G.has_edge_(c,a))):
#					for d in range (0,G.num_nodes):
#						if G.has_edge_(a,b) and G.has_edge_(b,a) and G.has_edge_(b,c) and G.has_edge_(c,b) and G.has_edge_(a,d) and G.has_edge_(d,a) and G.has_edge_(c,d) and G.has_edge_(d,c) and G.has_edge_(a,c) and G.has_edge_(c,a) :
#							score= G.weight(G.node_object(a),G.node_object(b)) +  G.weight(G.node_object(b),G.node_object(a)) + G.weight(G.node_object(b),G.node_object(c)) +  G.weight(G.node_object(c),G.node_object(b)) + G.weight(G.node_object(c),G.node_object(d)) +  G.weight(G.node_object(d),G.node_object(c)) + G.weight(G.node_object(a),G.node_object(d)) +  G.weight(G.node_object(d),G.node_object(a))+ G.weight(G.node_object(a),G.node_object(c))+ G.weight(G.node_object(c),G.node_object(a))
#							Storage3.append([G.node_object(a),G.node_object(b),G.node_object(c),G.node_object(d)])
#
#
### Creatus unique sets of 4
#t=[]
#for x in range (0,len(Storage3)):
#	if int(len(set(Storage3[x]))) == 4:
#		t.append(sorted(Storage3[x]))
#tt= map(list, set(map(frozenset, t)))
#print tt