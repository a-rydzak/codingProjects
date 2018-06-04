###https://www.dataquest.io/blog/web-scraping-tutorial-python/

from lxml import html
import requests
page0 = requests.get('http://wiki.teamliquid.net/starcraft2/Level_Up_Roma')
page1= requests.get('http://wiki.teamliquid.net/starcraft2/Gauntlet_Season_2_Global_Finals')
page2= requests.get('http://wiki.teamliquid.net/starcraft2/VTL_Allstars')
page3= requests.get('http://wiki.teamliquid.net/starcraft2/Passioncraft_Open_S3')
page4= requests.get('http://wiki.teamliquid.net/starcraft2/GG_year_2016')
page5= requests.get('http://wiki.teamliquid.net/starcraft2/WardiTV_Christmas_Invitational')
page6= requests.get('http://wiki.teamliquid.net/starcraft2/Taco_Cup')
page7= requests.get('http://wiki.teamliquid.net/starcraft2/PSISTORM_Cup_4')
page8= requests.get('http://wiki.teamliquid.net/starcraft2/Topdogs_8')
page9= requests.get('http://wiki.teamliquid.net/starcraft2/StarLine_League_Season_3')
###page10= requests.get('http://wiki.teamliquid.net/starcraft2/Leifeng_Cup/158')###### throw out???
page11= requests.get('http://wiki.teamliquid.net/starcraft2/Shang_gan_ling/6')
page12= requests.get('http://wiki.teamliquid.net/starcraft2/Stream.Me_Arena_2')
page13= requests.get('http://wiki.teamliquid.net/starcraft2/EGU_2016')
page14= requests.get('http://wiki.teamliquid.net/starcraft2/Xtreme_Dude_Championship')
page15= requests.get('http://wiki.teamliquid.net/starcraft2/Cheesadelphia_3.5')
page16= requests.get('http://wiki.teamliquid.net/starcraft2/International_Topdogs')
page17= requests.get('http://wiki.teamliquid.net/starcraft2/Shang_gan_ling/5')
page18= requests.get('http://wiki.teamliquid.net/starcraft2/Lima_Gaming_Festival')
page19= requests.get('http://wiki.teamliquid.net/starcraft2/Topdogs_7')
page20= requests.get('http://wiki.teamliquid.net/starcraft2/PSISTORM_Cup_3')
page21= requests.get('http://wiki.teamliquid.net/starcraft2/Topdogs_6')
page22= requests.get('http://wiki.teamliquid.net/starcraft2/ChallengeWars/GGLetsRE')
page23= requests.get('http://wiki.teamliquid.net/starcraft2/Passioncraft_Open')
page24= requests.get('http://wiki.teamliquid.net/starcraft2/Gamer_Sensei_Grand_Slam')
page25= requests.get('http://wiki.teamliquid.net/starcraft2/Shang_gan_ling/4')
page26= requests.get('http://wiki.teamliquid.net/starcraft2/Stream.Me_Arena')
page27= requests.get('http://wiki.teamliquid.net/starcraft2/TAW_Open_EU')
page28= requests.get('http://wiki.teamliquid.net/starcraft2/DSCL_Open_2016')
page29= requests.get('http://wiki.teamliquid.net/starcraft2/Gauntlet_Season_1_Global_Finals')
page30= requests.get('http://wiki.teamliquid.net/starcraft2/Topdogs_5')
page31= requests.get('http://wiki.teamliquid.net/starcraft2/StarLine_1xBet_League_Season_2')
page32= requests.get('http://wiki.teamliquid.net/starcraft2/Shang_gan_ling/3')
page33= requests.get('http://wiki.teamliquid.net/starcraft2/Wardi_Open_1')
page34= requests.get('http://wiki.teamliquid.net/starcraft2/GeForce_Cup_Summer_Edition')
###page35= requests.get('http://wiki.teamliquid.net/starcraft2/Leifeng_Cup/150')###Throw this one out
page36= requests.get('http://wiki.teamliquid.net/starcraft2/Topdogs_4')
page37= requests.get('http://wiki.teamliquid.net/starcraft2/Valhalla_-_Battle_of_Scandinavia')
###page38= requests.get('http://wiki.teamliquid.net/starcraft2/Leifeng_Cup/149') Throw this one out
page39= requests.get('http://wiki.teamliquid.net/starcraft2/World_Electronic_Sports_Games_2016/Asia-Pacific/China/Wuhan')
page40= requests.get('http://wiki.teamliquid.net/starcraft2/World_Electronic_Sports_Games_2016/Asia-Pacific/China/Chengdu')
page41= requests.get('http://wiki.teamliquid.net/starcraft2/Huangshan_Mountain_Open_Cup')
page42= requests.get('http://wiki.teamliquid.net/starcraft2/Shang_gan_ling/1')
page43= requests.get('http://wiki.teamliquid.net/starcraft2/World_Electronic_Sports_Games_2016/Asia-Pacific/China/Nanning')
page44= requests.get('http://wiki.teamliquid.net/starcraft2/World_Electronic_Sports_Games_2016/Asia-Pacific/China/Shenyang')
page45= requests.get('http://wiki.teamliquid.net/starcraft2/Gamercom_2016')
page46= requests.get('http://wiki.teamliquid.net/starcraft2/Topdogs_3')
page47= requests.get('http://wiki.teamliquid.net/starcraft2/Coaching_Zone_1')
page48= requests.get('http://wiki.teamliquid.net/starcraft2/World_Electronic_Sports_Games_2016/Asia-Pacific/China/Beijing')
page49= requests.get('http://wiki.teamliquid.net/starcraft2/PSISTORM_Cup_2')
page50= requests.get('http://wiki.teamliquid.net/starcraft2/The_Gauntlet/Global_showdown')
page51= requests.get('http://wiki.teamliquid.net/starcraft2/World_Electronic_Sports_Games_2016/Asia-Pacific/China/Hefei')
page52= requests.get('http://wiki.teamliquid.net/starcraft2/BaseTradeTV_Map_Test_Tournament')
page53= requests.get('http://wiki.teamliquid.net/starcraft2/Fantasy_Expo_Challenge_Season_3')
page54= requests.get('http://wiki.teamliquid.net/starcraft2/World_Electronic_Sports_Games_2016/Asia-Pacific/China/Qingdao')
page55= requests.get('http://wiki.teamliquid.net/starcraft2/World_Electronic_Sports_Games_2016/Asia-Pacific/China/Changsha')
###page56= requests.get('http://wiki.teamliquid.net/starcraft2/Leifeng_Cup/145')### Throw this out
page57= requests.get('http://wiki.teamliquid.net/starcraft2/Ting_of_the_Hill')
page58= requests.get('http://wiki.teamliquid.net/starcraft2/Topdogs_2')
page59= requests.get('http://wiki.teamliquid.net/starcraft2/Torino_Comics_2016')
page60= requests.get('http://wiki.teamliquid.net/starcraft2/Leifeng_Cup/144')
page61= requests.get('http://wiki.teamliquid.net/starcraft2/Cheesadelphia_Online_2_Season_2')
page62= requests.get('http://wiki.teamliquid.net/starcraft2/International_Topdogs')
page63= requests.get('http://wiki.teamliquid.net/starcraft2/Starcraft2.fi_6V._Cup')
page64= requests.get('http://wiki.teamliquid.net/starcraft2/Leifeng_Cup/157')
page65= requests.get('http://wiki.teamliquid.net/starcraft2/HFLAN_13')
page66= requests.get('http://wiki.teamliquid.net/starcraft2/TaKe%27s_Penthouse_Party')
page67= requests.get('http://wiki.teamliquid.net/starcraft2/NPF_2016')
page68= requests.get('http://wiki.teamliquid.net/starcraft2/Bonus_Pool_Season_2')
###page69= requests.get('http://wiki.teamliquid.net/starcraft2/ESL_ANZ_Cup_October') ##Throw out
page70= requests.get('http://wiki.teamliquid.net/starcraft2/Monday_Night_Gauntlet/4')
page71= requests.get('http://wiki.teamliquid.net/starcraft2/Epic.NINETEEN')
page72= requests.get('http://wiki.teamliquid.net/starcraft2/Monday_Night_Gauntlet/4')
###page73= requests.get('http://wiki.teamliquid.net/starcraft2/HFLAN_12') throw out
page74= requests.get('http://wiki.teamliquid.net/starcraft2/DingIt_StarCraft_II_Invitational_Season_4')
page75= requests.get('http://wiki.teamliquid.net/starcraft2/Indy_Cup/5')
###page76= requests.get('http://wiki.teamliquid.net/starcraft2/ASL_Season_6/Prime_League') throw out
page77= requests.get('http://wiki.teamliquid.net/starcraft2/Topdogs')
page78= requests.get('http://wiki.teamliquid.net/starcraft2/Monday_Night_Gauntlet/3')
page79= requests.get('http://wiki.teamliquid.net/starcraft2/Gamers_Assembly_2016')
page80= requests.get('http://wiki.teamliquid.net/starcraft2/Copenhagen_Games_Spring_2016')
page81= requests.get('http://wiki.teamliquid.net/starcraft2/The_Gathering_2016')
page82= requests.get('http://wiki.teamliquid.net/starcraft2/Monday_Night_Gauntlet/2')
###page83= requests.get('http://wiki.teamliquid.net/starcraft2/ESL_ANZ_Cup_March') throw out???
###page84= requests.get('http://wiki.teamliquid.net/starcraft2/Cheesadelphia_2') throw out???
page85= requests.get('http://wiki.teamliquid.net/starcraft2/DingIt_StarCraft_II_Invitational_Season_3')
page86= requests.get('http://wiki.teamliquid.net/starcraft2/Kings_of_the_North_2016')
page87= requests.get('http://wiki.teamliquid.net/starcraft2/Monday_Night_Gauntlet/1')
page88= requests.get('http://wiki.teamliquid.net/starcraft2/Super_Turniej_K***o')
page89= requests.get('http://wiki.teamliquid.net/starcraft2/Epic.SEVENTEEN')
page90= requests.get('http://wiki.teamliquid.net/starcraft2/Rival_StarCraft_II_League_2016_Season_1')
page91= requests.get('http://wiki.teamliquid.net/starcraft2/David_Filth_League')
page92= requests.get('http://wiki.teamliquid.net/starcraft2/ESL_ANZ_Cup_February')
page93= requests.get('http://wiki.teamliquid.net/starcraft2/Gauntlet_2016_Preseason_Final')
page94= requests.get('http://wiki.teamliquid.net/starcraft2/Acer_Pro_Challenge')
page95= requests.get('http://wiki.teamliquid.net/starcraft2/Kings_of_the_Craft')
page96= requests.get('http://wiki.teamliquid.net/starcraft2/Assembly_Winter_2016')
page97= requests.get('http://wiki.teamliquid.net/starcraft2/Fantasy_Expo_Challenge_Season_2')
page98= requests.get('http://wiki.teamliquid.net/starcraft2/Super_Test_Tuesday')
page99= requests.get('http://wiki.teamliquid.net/starcraft2/PSISTORM_Cup_1')
page100= requests.get('http://wiki.teamliquid.net/starcraft2/ESL_ANZ_Cup_January')
page101= requests.get('http://wiki.teamliquid.net/starcraft2/DingIt_StarCraft_II_Invitational_Season_2')
page102= requests.get('http://wiki.teamliquid.net/starcraft2/CybBet_Race_Wars')
page103= requests.get('http://wiki.teamliquid.net/starcraft2/AfreecaTV_LotV_Open')
page104= requests.get('http://wiki.teamliquid.net/starcraft2/SC2SEA_OSC_Championship_3')
page105= requests.get('http://wiki.teamliquid.net/starcraft2/Monday_Night_Gauntlet/0')
page106= requests.get('http://wiki.teamliquid.net/starcraft2/DingIt_StarCraft_II_Invitational_Season_1')
page107= requests.get('http://wiki.teamliquid.net/starcraft2/GG_Goda_2015')
page108= requests.get('http://wiki.teamliquid.net/starcraft2/2016_Global_StarCraft_II_League_Pre-Season/Week_2')
page109= requests.get('http://wiki.teamliquid.net/starcraft2/2016_Global_StarCraft_II_League_Pre-Season/Week_1')
page110= requests.get('http://wiki.teamliquid.net/starcraft2/Gauntlet_StarCraft_LotV_Series_1')
page111= requests.get('http://wiki.teamliquid.net/starcraft2/WW3')
page112= requests.get('http://wiki.teamliquid.net/starcraft2/HFLAN_11')
page113= requests.get('http://wiki.teamliquid.net/starcraft2/Rival_StarCraft_II_League_2015_Invitational')
page114= requests.get('http://wiki.teamliquid.net/starcraft2/BaseTradeTvT_Tournament')
page115= requests.get('http://wiki.teamliquid.net/starcraft2/Gauntlet_LotV_Open/2')
page116= requests.get('http://wiki.teamliquid.net/starcraft2/Gauntlet_LotV_Open/1')
page117= requests.get('http://wiki.teamliquid.net/starcraft2/Insomnia_XVII')
###page118= requests.get('http://wiki.teamliquid.net/starcraft2/Cheesadelphia_1') throw out???
####page119= requests.get('http://wiki.teamliquid.net/starcraft2/Epic.SIXTEEN') throw out???
page120= requests.get('http://wiki.teamliquid.net/starcraft2/Rival_StarCraft_II_League_2015_Season_3')
page121= requests.get('http://wiki.teamliquid.net/starcraft2/TSH_Cup')
page122= requests.get('http://wiki.teamliquid.net/starcraft2/Open_Lat_2015')
page123= requests.get('http://wiki.teamliquid.net/starcraft2/The_8')
page124= requests.get('http://wiki.teamliquid.net/starcraft2/Australian_Cyber_League/2015_Pro_Circuit/Melbourne')
page125= requests.get('http://wiki.teamliquid.net/starcraft2/OletVoittaja')
page126= requests.get('http://wiki.teamliquid.net/starcraft2/RSTL_Solo_League_2')
page127= requests.get('http://wiki.teamliquid.net/starcraft2/Indy_Cup/4')
page128= requests.get('http://wiki.teamliquid.net/starcraft2/LCS_2015/Invitational_1')
page129= requests.get('http://wiki.teamliquid.net/starcraft2/Copa_America_2015/Season_3')
page130= requests.get('http://wiki.teamliquid.net/starcraft2/The_Gauntlet_Cup_Final')
page131= requests.get('http://wiki.teamliquid.net/starcraft2/The_Gauntlet_Cup_2')
###page132= requests.get('http://wiki.teamliquid.net/starcraft2/Australian_Cyber_League/2015_Pro_Circuit/Sydney') throw out
###page133= requests.get('http://wiki.teamliquid.net/starcraft2/OSC_Global_Allstars_2') throw out
page134= requests.get('http://wiki.teamliquid.net/starcraft2/Epic.FIFTEEN')
page135= requests.get('http://wiki.teamliquid.net/starcraft2/Rival_StarCraft_II_League_2015_Season_2')
page136= requests.get('http://wiki.teamliquid.net/starcraft2/Copa_America_2015/Season_2')
page137= requests.get('http://wiki.teamliquid.net/starcraft2/WATCH_This:_Jord_Invitational')
page138= requests.get('http://wiki.teamliquid.net/starcraft2/The_Gauntlet_Cup_1')
page139= requests.get('http://wiki.teamliquid.net/starcraft2/The_Breakout_Invitational_IV')
page140= requests.get('http://wiki.teamliquid.net/starcraft2/Evry_Games_City')
page141= requests.get('http://wiki.teamliquid.net/starcraft2/Copa_America_2015/Season_1')
###page142= requests.get('http://wiki.teamliquid.net/starcraft2/HFLAN_9') throw out
page143= requests.get('http://wiki.teamliquid.net/starcraft2/RSTL_Solo_League')
###page144= requests.get('http://wiki.teamliquid.net/starcraft2/User:HoZBlooddrop/SC2_Modena_PLAY_2015')
page145= requests.get('http://wiki.teamliquid.net/starcraft2/LANTREK%2715')
page146= requests.get('http://wiki.teamliquid.net/starcraft2/User:SuperHofmann/IeSN_Challenge')
page147= requests.get('http://wiki.teamliquid.net/starcraft2/Rival_StarCraft_II_League_2015_Season_1')
page148= requests.get('http://wiki.teamliquid.net/starcraft2/MAL_presents:_Smallest_Map_Possible')
page149= requests.get('http://wiki.teamliquid.net/starcraft2/Epic.FOURTEEN')
page150= requests.get('http://wiki.teamliquid.net/starcraft2/The_Safety_Net')
page151= requests.get('http://wiki.teamliquid.net/starcraft2/MAL_presents:_The_Beginning')
page152= requests.get('http://wiki.teamliquid.net/starcraft2/ZOTAC_Cup/Season_4_Final_2014')
page153= requests.get('http://wiki.teamliquid.net/starcraft2/OSC_Global_Allstars')
page154= requests.get('http://wiki.teamliquid.net/starcraft2/Assembly_Winter_2015')
page156= requests.get('http://wiki.teamliquid.net/starcraft2/Hairy_Smash_Tournament')


page_array=[page0,page1,page2,page3,page4,page5,page6,page7,page8,page9,page11,page12,page13,page14,page15,page16,page17,page18,page19,page20,page21,page22,page23,page24,page25,page26,page27,page28,page29,page30,page31,page32,page33,page34,page36,page37,page39,page40,page41,page42,page43,page44,page45,page46,page47,page48,page49,page50,page51,page52,page53,page54,page55,page57,page58,page59,page60,page61,page62,page63,page64,page65,page66,page67,page68,page70,page71,page72,page74,page75,page77,page78,page79,page80,page81,page82,page85,page86,page87,page88,page89,page90,page91,page92,page93,page94,page95,page96,page97,page98,page99,page100,page101,page102,page103,page104,page105,page106,page107,page108,page109,page110,page111,page112,page113,page114,page115,page116,page117,page120,page121,page123,page124,page125,page126,page126,page127,page128,page129,page130,page131,page134,page135,page136,page137,page138,page139,page140,page141,page143,page145,page146,page147,page148,page149,page150,page151,page152,page153,page154,page156]

###Start Trees------------------------------------------------------------------
trees=[]
for page in page_array:
	trees.append(html.fromstring(page.content))

#stars players----------------------------------------
players=[]
for tree in trees:
	players.append(tree.xpath('//span[@style="vertical-align:-1px;"]/text()'))
	
	
###start scores-------------------------------------------
scores=[]
for tree in trees:
	if tree.xpath('//div[@style="width:21px"]/text()'):
		scores.append(tree.xpath('//div[@class="bracket-score"]/text()'))
	
player_list=[]
for i in range (0, len(players)):
	for t in range(0, len(players[i])):
		player_list.append(players[i][t])

player_scores=[]
for i in range (0, len(scores)):
	for t in range(0, len(scores[i])):
		player_scores.append(scores[i][t])
		
print len(player_list)
print len(player_scores)
print player_list
print player_scores

#print players[2]
#print scores[2]
#print len(players[2])
#print len(scores[2])


###left off at http://wiki.teamliquid.net/starcraft2/Gamer_Sensei_Grand_Slam

