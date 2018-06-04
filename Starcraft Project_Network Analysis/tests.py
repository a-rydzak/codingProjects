# Swanand Kulkarni, smk160830
# Andrew Rydzak, axr163231
## SYSM6302 Project centrality tests


from __future__ import division
import zen
import matplotlib.pyplot as plt
plt.ioff()
from numpy import *
from numpy.linalg import eig,norm
import sys
#sys.path.append('C:\Users\Sony_owner\Desktop\Lab6\zend3js\zend3js')
#import d3js
from time import sleep
import colorsys
import numpy
import numpy.linalg as la
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pylab
import numpy
import math
import random

#sys.path.append('C:\Users\Sony_owner\Desktop\project\Starcraft Project\zend3js\zend3js')
#import d3js
#import randomnet

G = zen.io.gml.read('C:\Users\BroBoFett\Desktop\Starcraft Project\Starcraft_Graph.gml')
#G = zen.io.edgelist.read('C:\Users\Sony_owner\Desktop\project\Starcraft Project\Starcraft.edgelist', ignore_duplicate_edges=True) ####Used JUST ##########FOR Diffusion ########

N = G.num_nodes
print '\nTotal number of nodes in the graph is:'
print N

M = G.num_edges
print '\nTotal number of edges in the graph is:'
print M

A=G.matrix().transpose()

# prints the top ten (num) nodes according to the centrality vector v
def print_top(G,v, num=10):
	idx_list = [(i,v[i]) for i in range(len(v))]
	idx_list = sorted(idx_list, key = lambda x: x[1], reverse=True)
	for i in range(min(num,len(idx_list))):
		nidx, score = idx_list[i]
		print '  %i. %s (%1.4f)' % (i+1,G.node_object(nidx),score)
		#print '  %i. %s' % (i+1,G.node_object(idx))

# prints the bottom ten (num) nodes according to the centrality vector v
def print_bottom(G,v, num=10):
	idx_list = [(i,v[i]) for i in range(len(v))]
	idx_list = sorted(idx_list, key = lambda x: x[1], reverse=False)
	for i in range(min(num,len(idx_list))):
		nidx, score = idx_list[i]
		print '  %i. %s (%1.4f)' % (i+1,G.node_object(nidx),score)
		#print '  %i. %s' % (i+1,G.node_object(idx))
        
def index_of_max(v):
    return numpy.where(v == max(v))[0]
        
### DEGREE CENTRALITY(((((M1)))))--------------MOST WINS
#M1 = numpy.zeros( (N,) )
#for i in range(N):
#	for j in range(N):
#		M1[i] += A[i,j]
##print '\nDegree Centrality vector:'
##print M1
#print '\nTop ten characters in Degree centrality vector:'
#print_top(G,M1)
#
#print '\nBottom ten characters in Degree centrality vector:'
#print_bottom(G,M1)

##############################---------MOST LOSSES------###########

#M111 = numpy.zeros( (N,) )
#for i in range(N):
#	for j in range(N):
#		M111[i] += A[j,i]
##print '\nDegree Centrality vector:'
##print M1
#print '\nTop ten characters in Degree centrality vector:'
#print_top(G,M111)
#
#print '\nBottom ten characters in Degree centrality vector:'
#print_bottom(G,M111)

##############################---------MOST SUCCESSFULL PLAYERS------###########

M1 = numpy.zeros( (N,) )
M111 = numpy.zeros( (N,) )
M222 = numpy.zeros( (N,) )
for i in range(N):
    for j in range(N):
        M1[i] += A[i,j]    ####Number of wins
        M111[i] += A[j,i]   ###Number of losses
        
M333 = M1 + M111
#for i in range (N):
#    if M333[i]>50:
#        M222[i] = M1[i]/ M333[i]
#    else:
#        M222[i] = 0
##print '\nDegree Centrality vector:'
##print M1
#print M222
#print '\nTop ten successful players:'
#print_top(G,M222)

###Return Node indice of the maximum centrality score:
##
##
##print '\nMax value in an array:'
##print numpy.where(M1 == max(M1))[0]


## EIGENVECTOR CENTRALITY(((((M2,M3)))))

#M2 = zen.algorithms.centrality.eigenvector_centrality_(G,weighted=True)
#
##print '\nEigenvector Centrality (by Zen):'
##print M2
#print '\nTop ten characters in Eigenvector centrality(by Zen):'
#print_top(G,M2)
#
#print '\nBottom ten characters in Eigenvector centrality(by Zen):'
#print_bottom(G,M2)
#
#
#k, v = la.eig(A)
#k1_idx = index_of_max(k) # find the index of the largest eigenvalue
#
#Eigenvmax = k[k1_idx]
#
#print '\nLargest Eigenvalue:'
#Eigenvreal = numpy.abs(Eigenvmax)
#print Eigenvreal
#
#z = v[:,k1_idx]
#
#M3 = numpy.abs(z)
##print '\nEigenvector Centrality (by linear algebra):'
##print M3
#print '\nTop ten characters in Eigenvector centrality(by algebra):'
#print_top(G,M3)
#print '\nBottom ten characters in Eigenvector centrality(by algebra):'
#print_bottom(G,M3)


#### KATZ CENTRALITY (((((M4,M5,M6)))))
###### Blows off at alpha =1, since f1 is a singular matrix- Demerit of Katz centrality. works right even with alpha= 0.9999 or 1.0001.
#alpha1 = 1
#f1 = numpy.eye(N) - alpha1*A
#f2 = la.inv(f1)
#f3 = numpy.ones((N,1))
#M4 = numpy.dot(f2,f3)
##print'\nKatz centrality at alpha=1:'
##print M4
#print'\nTop ten characters in Katz centrality at alpha=1:'
#print_top(G,M4)
#print'\nBottom ten characters in Katz centrality at alpha=1:'
#print_bottom(G,M4)

#alpha20 = 20
#f7 = numpy.eye(N) - alpha20*A
#f8 = la.inv(f7)
#f9 = numpy.ones((N,1))
#M5 = numpy.dot(f8,f9)
##print'\nKatz centrality at alpha=20:'
##print M5
#print'\nTop ten characters in Katz centrality at alpha=20:'
#print_top(G,M5)
#print'\nBottom ten characters in Katz centrality at alpha=20:'
#print_bottom(G,M5)
#
#alpha39 = 39
#f16 = numpy.eye(N) - alpha39*A
#f17 = la.inv(f16)
#f18 = numpy.ones((N,1))
#M6 = numpy.dot(f17,f18)
##print'\nKatz centrality at alpha=39:'
##print M6
#print'\nTop ten characters in Katz centrality at alpha=39:'
#print_top(G,M6)
#print'\nBottom ten characters in Katz centrality at alpha=39:'
#print_bottom(G,M6)

#### PAGERANK CENTRALITY (((((M7,M8,M9)))))
#k = numpy.zeros( (N,) )
#for j in range(N):
#    for i in range(N):
#        k[j] += A[i,j]
#
#s = numpy.zeros( (N,N) )
#for i in range(N):
#    s[i,i] = max(k[i],1)
#
#d = la.inv(s)
#h = numpy.dot(A,d) ######This is AD-1

#alpha01 = 0.1
#h1 = alpha01*h
#h2 = numpy.eye(N)-h1
#h3 = la.inv(h2)
#h4 = numpy.ones((N,1))
#M7 = numpy.dot(h3,h4)
##print'\nPageRank centrality at alpha=0.1:'
##print M7
#print'\nTop ten PageRank centrality characters at alpha=0.1:'
#print_top(G,M7)
#print'\nBottom ten PageRank centrality characters at alpha=0.1:'
#print_bottom(G,M7)
#
#alpha085 = 0.85
#h5 = alpha085*h
#h6 = numpy.eye(N)-h5
#h7 = la.inv(h6)
#h8 = numpy.ones((N,1))
#M8 = numpy.dot(h7,h8)
##print'\nPageRank centrality at alpha=0.85:'
##print M8
#print'\nTop ten PageRank centrality characters at alpha=0.85:'
#print_top(G,M8)
#print'\nBottom ten PageRank centrality characters at alpha=0.85:'
#print_bottom(G,M8)
#
#alpha1 = 0.99
#h9 = alpha1*h
#h10 = numpy.eye(N)-h9
#h11 = la.inv(h10)
#h12 = numpy.ones((N,1))
#M9 = numpy.dot(h11,h12)
##print'\nPageRank centrality at alpha=0.99:'
##print M9
#print'\nTop ten PageRank centrality characters at alpha=0.99:'
#print_top(G,M9)
#print'\nBottom ten PageRank centrality characters at alpha=0.99:'
#print_bottom(G,M9)

##### BETWEENNESS CENTRALITY (((((M10)))))
#M10 = zen.algorithms.centrality.betweenness_centrality_(G,True)
##print '\nBetweenness Centrality:'
##print M10
#print '\nTop ten characters in Betweenness Centrality:'
#print_top(G,M10)
#print '\nBottom ten characters in Betweenness Centrality:'
#print_bottom(G,M10)

####POWER LAW EXPONENT
#
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
#calc_aplha_val(ddlist_false, 6)# look above to see the function created.
#
#k = numpy.arange(len(ddlist_true))
#plt.figure(figsize=(8,12))
#plt.subplot(211)
#plt.title('StarCraft Network')
#plt.xlabel('Degrees')
#plt.ylabel('Fraction of degree distribution')
#plt.bar(k,ddlist_true, width=1, bottom=0, color='b')
#
#plt.subplot(212)
#plt.xlabel('Degrees')
#plt.ylabel('Cumulative degree distribution')
#plt.loglog(k,cddlist)
#plt.show()

####Friendship paradox

#Avg_Deg=2*M/N
#ddlist_false=zen.degree.ddist(G,normalize=False)
#ddlist_true=zen.degree.ddist(G,normalize=True)
#
#q=0
#aa = numpy.arange(len(ddlist_false))
#for i in range(0,len(ddlist_false)):
#	q+=ddlist_false[i]*aa[i]**2
#
#x=q/N
#a=x/Avg_Deg
#print "This is the average degree of a node"
#print Avg_Deg
#print "This is the average degree of a node's neighbors"
#print a


###BA GRAPH COMPARISON

#G=zen.Graph()
#G=randomnet.barabasi_albert(752,3,graph=G)
#
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
#calc_aplha_val(ddlist_false, 26)
#
#
#k = numpy.arange(len(ddlist_true))
#plt.figure(figsize=(8,12))
#plt.subplot(211)
#plt.title('G=randomnet.barabasi_albert(10000,4,graph=G)')
#plt.xlabel('Degrees')
#plt.ylabel('Fraction of degree distribution')
#plt.bar(k,ddlist_true, width=1, bottom=0, color='b')
#
#plt.subplot(212)
#plt.xlabel('Degrees')
#plt.ylabel('Cumulative degree distribution')
#plt.loglog(k,cddlist)
#plt.show()


###########MODULARITY

def modularity(G,c):
	d = dict()
	for k,v in c.iteritems():
		for n in v:
			d[n] = k
	Q, Qmax = 0,1
	for u in G.nodes_iter():
		for v in G.nodes_iter():
			if d[u] == d[v]:
				Q += ( int(G.has_edge(v,u)) - G.in_degree(u)*G.out_degree(v)/float(G.num_edges) )/float(G.num_edges)
				Qmax -= ( G.in_degree(u)*G.out_degree(v)/float(G.num_edges) )/float(G.num_edges)
	return Q, Qmax

#c = {
# 	'group1': ['Argentina','Brazil','Chile','Mexico','Colombia','Jamaica','Paraguay'],
# 	'group2': ['Japan','SouthKorea'],
# 	'group3': ['UnitedStates'],
# 	'group4': ['Nigeria','Morocco','SouthAfrica','Cameroon','Tunisia','Iran','Turkey'],
# 	'group5': ['Scotland','Belgium','Austria','Germany','Denmark','Spain','France','GreatBritain','Greece','Netherlands','Norway','Portugal','Italy','Yugoslavia','Romania','Bulgaria','Croatia','Switzerland']
# 	}
#Q, Qmax = modularity(G,c)
#print '\nModularity for groups based on geography:'
#print 'Modularity: %1.4f / %1.4f' % (Q,Qmax)

abc1 = []
xyz1 =[]

for i in range (N):
    if M333[i]>50:
        abc1.append(i)
    else:
        xyz1.append(i)

abc2 = []
xyz2 =[]

#print abc
for i in range (len(abc1)):
    abc2.append(G.node_object(abc1[i]))
    
#print abc2
        
for i in range (len(xyz1)):
    xyz2.append(G.node_object(xyz1[i]))
    
print xyz2

c = {
 	'group1': ['Reynor', 'Strange', 'Snute', 'MaNa', 'Bly', 'Cham', 'Scarlett', 'JonSnow', 'MaSa', 'Guru', 'GuMiho', 'uThermal', 'aLive', 'Nerchio', 'Solar', 'puCK', 'DemiLove', 'Semper', 'Creature', 'MarineLorD', 'Dayshi', 'DnS', 'ShaDoWn', 'PtitDrogo', 'Ryung', 'Neeb', 'Kelazhur', 'PiLiPiLi', 'Indy', 'Basior', 'Seither', 'Welmu','Elazer', 'ByuN', 'Bunny', 'Lillekanin', 'Harstem', 'TRUE', 'Polt', 'ArT', 'souL', 'Rodzyn', 'FireCake', 'Lilbow', 'Namshar', 'Beastyqt', 'ZhuGeLiang', 'DaNa','Tefel', 'HuK', 'Serral', 'Mix', 'Cladorhiza', 'Aicy', 'Petraeus', 'PiG', 'iaguz'],
 	'group2': ['Maker', 'Ryu', 'Veterans', 'Stareagle', 'Purce', 'Exehn', 'SuperHofmann', 'Helt', 'RuinBlaster', 'MiaNonna', 'Azarot', 'Ryosis', 'VeniVidiVins', 'Sheva', 'Mark', 'MovieMaker', 'Proch', 'Asura', 'Dregon', 'GodOfSfaccim', 'BYE', 'Xados', 'Suall', 'MMY', 'Monta', 'Aranoch', 'Parsa', 'Gua', 'Bigbogia', 'Horus', 'Blooddrop', 'BabyMarine', 'BigBogia', 'Huayra', 'Lobo', 'StriKE', 'ThuocLao', 'Parkson', 'Uply', 'Kim', 'Oracle', 'Red', 'hunterxx', 'ShiOne', 'SoK', 'Elusory', 'JusticeSimon', 'RPGAAT', 'MeomaikA', 'GuardianWisp', 'eagle','Arnovic', 'Snowdrum','ForeSt', 'Judicator', 'Guillemot', 'Veryn', 'AdmiralMer', 'Thalandros', 'DalaiLameR', 'NukeLar', 'Voyager', 'SexyDrone', 'Skimer', 'Ditrih', 'Azunyashka', 'VeNTuRe', 'LtDan', 'Sunokasuri', 'xd6ssy', 'Pyloss', 'Ceonsamea', 'MisterL', 'LuckRussian', 'Doctor', 'Sevnin', 'Janus', 'MrTea', 'Mraptor', 'CrazyJack', 'Cereal', 'Couguar', 'Krr', 'DIMAGA', 'Brat_OK', 'Kas', 'KeeN', 'Impact', 'SortOf', 'wiNgiAN', 'Winter', 'Dream', 'MajOr', 'ShoWTimE', 'BLord', 'viOLet', 'WarreN', 'Tesla', 'Raze', 'CalebAracous', 'xKawaiian', 'RuFF', 'Towelie', 'Clem', 'Uzikoti', 'hinO', 'Minato', 'Friend', 'SKillous', 'Arctur', 'INnoVation', 'Creator', 'Classic', 'Losira', 'herO', 'GAMETIME', 'Matiz', 'Ziggy', 'vaisravana', 'Myuu', 'EnDerr', 'Probe', 'Pox', 'PSiArc', 'GuchoiBoi', 'Early', 'Greg', 'starkiller', 'Voltz', 'Pokebunny', 'Paperboat', 'DisReSpeCT', 'SyberCat', 'Suppy', 'Hjax', 'TLO','Super', 'Trust', 'Patience', 'TICTAC', 'OdiN', 'MegaXyloN', 'DarkDaniel', 'Zlatan', 'Jhonny', 'ObEliZkO', 'Razza', 'TheDogDream', 'Verytoss', 'Blick', 'Gosudark', 'MeTabee', 'AZULSTAR', 'CealeR', 'Denver', 'FunK', 'MygraiN', 'Sugar', 'MarineLord', 'Optimus', 'Nefaste', 'alluton', 'Malcolm', 'DiamondPolt', 'Daffe', 'jympara', 'Gator', 'Vader', 'ShadowSeeker', 'MasterNoodle', 'Zode', 'Beast', 'FOXTocon', 'Icy', 'Gremory', 'Rhoust', 'Andromeda', 'damrud', 'quaZa', 'FightingFrog', 'DropMsZ', 'Storm', 'Annihilator', 'PikA', 'Exactly', 'Dystopia', 'Tocon', 'goblin', 'TOP', 'PappiJoe', 'MythiC', 'Orion', 'ArchangeL', 'Prime', 'Captnfingers', 'Liqht', 'Crowbar', 'MperorM', 'Astrea', 'JimRising', 'WoodedMicrob', 'Starbuck', 'Light', 'Marsman', 'SpaceMarine', 'InZaNe', 'Bails', 'Soulspirit', 'ExE', 'EnigmA', 'HellRaiser', 'Hellraiser', 'MouLou', 'Scythe', 'SolO', 'u65b0\\u624b\\u4e2d\\u7684\\u65b0\\u624b', 'iAsonu', 'u8299\\u5170\\u8fbe', 'Quas', 'u96ea\\u4e4b\\u4e0b\\u96ea\\u4e43', 'Psmoonsun', 'u9e21\\u513f\\u76d2\\u996d', 'coffee', 'ZKO', 'XiGua', 'YHY', 'EVAnelAZon', 'Route', 'temporarg', 'E.knife', 'ZZzz','Lambo', 'Immortality', 'Gamja', 'Jim', 'TIME', 'Hydra', 'XY', 'TAiLS', 'BreakingGG', 'u9648\\u660e\\u6d9b', 'Uaifeng', 'MacsSed', 'u82e5\\u8c37', 'u749e\\u9038', 'Yink', 'Lieben', 'u5362\\u5b50\\u541b', 'zine', 'Byhnewbee', 'luna', 'u6218\\u65e0\\u4e0d\\u80dc', 'u5b5f\\u5a46\\u6c64', 'Cyan', 'u79fd\\u7ffc', 'hidegoshi', 'AlisoN', 'Erik', 'nLghost', 'Promathos', 'wizardgamer', 'Tonho', 'Zinho', 'Tunico', 'RiSky', 'Zervas', 'POX', 'HateMe', 'PengWin', 'Ray', 'DyyS', 'Protosschen', 'Auuroa', 'TooDming', 'Hickok', 'DHcsyler', 'EndOfLine', 'Walkuere', 'u9c7c\\u8089\\u5305\\u5b50', 'u795e\\u4e4b\\u957f\\u8005', 'Asuna', 'Aloha', 'u79d1\\u6280\\u5927\\u5b66\\u5bbf\\u820d\\u6ca1\\u7f51', 'u82b1\\u82b1\\u7684\\u5c0f\\u571f\\u72d7', 'Theo', 'Miszu', 'Senin', 'AndreJOO', 'Dexter', 'Prabuty', 'Tetris', 'Gerald', 'ParanOid', 'BluE', 'Geralt', 'FuriOus', 'HaPe', 'sevnin', 'LaussPompka', 'Szachu', 'JieShi', 'u82b1\\u751f\\u5c41\\u80a1\\u597d\\u767d\\u767d', 'XiaoC', 'EFFEL', 'Shana', 'u738b\\u4f1a\\u6c11', 'Yocking', 'u7530\\u541b\\u6cfd', 'Sky Walker', 'u6c38\\u6052\\u4e4b\\u96f6', 'CloudAtlas', 'Savior', 'u4e9a\\u57ce\\u6728\\u68a6\\u53f6', 'u65e0\\u9650\\u5927\\u7684\\u68a6\\u60f3\\u80cc\\u540e', 'u751f\\u65e0\\u53ef\\u604b', 'Drunkenboi', 'Diord', 'gropheR', 'JeaL', 'Jeal', 'ByuL', 'Reality', 'MC', 'Sacrilege', 'Graphix', 'Seigifried', 'mykohchoo', 'Neuro', 'BamBam', 'HeltEn', 'Eddie', 'Amane', 'FireFlyHugs', 'PuPu', 'Jagelius', 'Haspe', 'Erakko', 'TheMusZero', 'Calt', 'Fagballs', 'Luolis', 'Hymy', 'Protosser', 'Alluton', 'Stats', 'Wolfhoundx', 'FerouCyril', 'LeKiL', 'Nyroc', 'Neverdie', 'Garitos', 'Jelin', 'DreinarK', 'Yggdrasil', 'StratoS', 'Pandalord', 'FurY', 'Davbond', 'Okaneby', 'LeKil', 'NeverDie', 'Tystic', 'Davdou', 'yukimurahh', 'skuly', 'SaNtaSaN', 'Emizo', 'Raskolnikoff', 'imData', 'TKL', 'LhornyTorynk', 'Raphi', 'Onigami', 'Hyperion', 'YellowFox', 'FlynUP', 'Arkafrost', 'yukimurahhh', 'SaNTaSaN', 'Socke', 'DeMusliM', 'HeRoMaRinE', 'FeaR', 'hotflake', 'RoerPeer','GipsyDanger', 'Heilskov', 'Spazymazy', 'Rebellion', 'jonas', 'Zezuane', 'PainGamer', 'hea', 'NicolaiFox', 'WPz', 'Mackintac', 'Bombs', 'Flood', 'Seb', 'Revolution', 'Buff', 'MystiC', 'Azures', 'Knuckey', 'Risky', 'tn', 'Gamerrichy', 'Afelay', 'Multi', 'GamerRichy', 'Mythic', 'Soulkey', 'Has', 'Blaze', 'Symbol', 'ImmortalPasT', 'ghasT', 'WojTaS', 'LordJim', 'Xaoras', 'Nedi', 'SmelC', 'Kirwa', 'Siglave', 'Iselia', 'Gaspi', 'YoGo', 'MekTypro', 'Ylaff', 'MoMaN', 'Lind', 'Relmer', 'Elyona', 'MiNiMaTh', 'CoolBreeze', 'Crow', 'Aggression', 'Thorminator', 'Snovski', 'SlemPastor', 'Adrian', 'PaulMag', 'Kolbein', 'Tretsy', 'erL', 'HOODOUT','Magen', 'Civi', 'Poseidon', 'Evire', 'Forte', 'horror', 'DeParture', 'Armani','HyuN', 'desRow', 'NoRegreT', 'intense', 'Zazu', 'SuperSaiyan', 'Wardi', 'Ourk', 'Distan', 'fishbonedD', 'Flux', 'Figaro', 'Bazooka', 'Krosis', 'Ziroy', 'PandaBearMe', 'Monty', 'Dolan', 'NXZ', 'Azure', 'KingkOng', 'Crimson', 'Rize', 'MightyKiwi', 'Wally', 'Frustration', 'Blysk', 'Stephano', 'VortiX', 'Rogue', 'Cure', 'sOs', 'Elroye', 'DeeN', 'iSy', 'Zylcu', 'Snoxtar', 'OrnLu', 'CNProtoss', 'Namzx', 'Vulak', 'Crayon', 'zamzx', 'Nomad', 'iAmJeffReY', 'Illusion', 'Arcanumus', 'heavyarms', 'MangoKim', 'Freeedom', 'Fleshspawn', 'FatCatChef', 'rainCzar', 'Kuyzz', 'Fullmetal', 'Ice', 'Chase', 'Yours', 'Chick', 'Choya', 'Ein', 'Seed', 'Leenock', 'Bomber', 'Blue', 'Qike', 'Nice', 'Law', 'Arthur', 'NaMeK', 'Alopex', 'ProzeR', 'KingKong', 'TaeJa', 'Curious', 'Happy', 'TerranWeak', 'Easy', 'CoolTea','Hurricane', 'TY', 'Life', 'MyuNgSiK', 'Zest', 'Trap', 'Dear', 'jjakji', 'Dark', 'DongRaeGu', 'Sorry', 'TheWeakness', 'Apocalypse', 'Zanster', 'Destiny', 'MasterBonsai', 'GreatTeacher', 'Mioga', 'Zbelin', 'LeMorse', 'Moulou', 'AaRaSs', 'NeutronX', 'ZBelin', 'Epic', 'Journey', 'MaFarazZo', 'Capricorn', 'Bakemonoda', 'Cirrus', 'NightEnD', 'PeRi', 'Revolver', 'qxc', 'MagicRover', 'Picasso', 'EJK', 'Believe', 'DouDou', 'Ezrc', 'Rushcrazy', 'Clannad','u4e0a\\u6d77\\u4eba\\u5f62', 'Punk', 'Sakya', 'JIN', 'Mystery', 'Cloudy', 'Six', 'SaberAltoria', 'JoCeLyN','SeRafiNe', 'MacSed', 'Ever', 'Arrogance', 'Zycart', 'PartinG', 'BrAvO', 'Osiris', 'deth', 'Deakins', 'Arrival', 'Kez', 'Petrify', 'Djvillian', 'Lumiya', 'Redemption', 'Fender', 'Namakaye', 'Metalcore', 'Enak', 'MrLando', 'Phoenix', 'MiLes', 'Fourby', 'StrongMike', 'Azz', 'MontyCarlo', 'Rendorian', 'ChadMann', 'Eros','Pezz', 'Fuzer', 'elfi', 'sLivko', 'Rail', 'BuRning', 'LiveZerg','u0428\\u0430\\u0445\\u043c\\u0430\\u0442\\u0438\\u0441\\u0442', 'Doublieu', 'Slowed', 'Macon', 'Umarlak', 'Sliwnisky', 'Molder', 'MorDka', 'Janikos', 'ToZiS', 'ADR', 'DarkSoul', 'wenez', 'ByRada', 'PrimusDeksiA', 'Smile', 'Spectrum', 'CatZ', 'Bioice', 'Arium', 'avilo', 'Jaedong', 'PsychO', 'Magico', 'Boombox', 'Sluggy', 'Nabwhoo','Daspocksta', 'Grimzzy', 'Zeal', 'KellerMaN', 'Sonic', 'KiToO', 'ReasoN', 'DominiC', 'Sektor', 'Moosegills', 'Xenocider', 'Trace', 'Aizen', 'Verdi', 'Cooltea','DMC', 'EiBS', 'Herbefa', 'SaDe', 'Divinesia', 'sepisepi', 'Kalinski', 'Vincent', 'Alphard', 'Chucky', 'StarEagle', 'RiK', 'FoxeR', 'HuShang', 'SirRobin', 'PoultryPouch', 'Mystic', 'CLN', 'KrasS', 'State', 'Minigun', 'Oz', 'Kamker', 'Phog', 'KoNtiNuE', 'TargA', 'Kane', 'Hitman', 'plzleaveduck', 'sWs', 'Fenner', 'Spear']
 	}
Q, Qmax = modularity(G,c)
print '\nModularity for groups based on geography:'
print 'Modularity: %1.4f / %1.4f' % (Q,Qmax)





#############DIFFUSION
#dt = 0.01 # the "infintesimal" size steps we take to integrate
#T = 20 # the end of the simulation time
#time = linspace(0,T,int(T/dt)) # the array of time points spaced by dt
##
#
#M1 = numpy.zeros( (N,) )
#M111 = numpy.zeros( (N,) )
#M222 = numpy.zeros( (N,) )
#for i in range(N):
#    for j in range(N):
#        M1[i] += A[i,j]    ####Number of wins
#        M111[i] += A[j,i]   ###Number of losses
#        
#M333 = M1 + M111  ####Total number of games by players  
#
#Nerchio= index_of_max(M1) #######Index of the player with most wins
#
#D = numpy.zeros( (N,N) )
#
#for j in range(N):
#    for i in range(N):
#        D[i,i] += A[i,j]
#L= D-A
#C=1
##
#def index_of_min(v):
#    return numpy.where(v == min(v))[0]
#
#k, v = la.eig(L)
#k1_idx = index_of_min(k) # find the index of the smallest eigenvalue
#
#Eigenvmin = k[k1_idx]
#Eigenvreal = numpy.abs(Eigenvmin)
#z = v[:,k1_idx]
#vectorreal = numpy.abs(z)
#vector_norm = vectorreal/la.norm(vectorreal) #########Normalized equilibrium state
#
#x = zeros(G.num_nodes) # the state vector
#x[99] =1
#
#statenorm = 0
#x_dist = zeros(len(time))
#for i,t in enumerate(time):
#    f = -C*numpy.dot(L,x)
#    x = f*dt + x
#    state_norm = x/la.norm(x)
#    x_dist[i] = la.norm(state_norm-vector_norm)
#print x_dist
#
#
#plt.figure()
#plt.plot(time,x_dist) # replace xvalue and yvalue with what you want to plot
#plt.xlabel('t')
#plt.ylabel('Diffusion Distance From Equillibrum') # change this label
#plt.show()


