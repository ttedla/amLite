#!/usr/bin/python
# -*- coding: UTF-8 -*-
def translitrate():
    text=open(raw_input("Enter Input File Name to translitrate:> "),'r')
    input_data=text.read()


    amharic_ascii_table={'he': u'ሀ', 'hu': u'ሁ', 'hi':u'ሂ' , 'ha':u'ሃ', 'hE':u'ሄ', 'hee':u'ሄ', 'h':u'ህ', 'ho':u'ሆ',\
'hW':u'ኋ', 'hWa':u'ኋ', 'hWe':u'ኈ', 'hWu':u'ኍ', 'hWi':u'ኊ', 'hWE':u'ኌ', 'hW\'':u'ኍ',\
'`he':u'ኀ', '`hu':u'ኁ', '`hi':u'ኂ','`ha':u'ኃ', '`hE':u'ኄ', '`hee':u'ኄ', '`h':u'ኅ', '`ho':u'ኆ',\
'`hWe':u'ኈ', '`hWu':u'ኍ', '`hWi':u'ኊ', '`hW':u'ኋ', '`hWa':u'ኋ', '`hWE':u'ኌ', '`hWee':u'ኌ',\
'`hW\'':u'ኍ', 'hhe':u'ኀ', 'hhu':u'ኁ', 'hhi':u'ኂ', 'hha':u'ኃ', 'hhE':u'ኄ', 'hhee':u'ኄ', 'hh':u'ኅ', 'hho':u'ኆ',\
'hhWe':u'ኈ', 'hhWu':u'ኍ', 'hhWi':u'ኊ', 'hhW':u'ኋ', 'hhWa':u'ኋ', 'hhWE':u'ኌ', 'hhWee':'ኌ', 'hhW\'':u'ኍ',\
'hhe':u'ኀ', 'hhu':u'ኁ', 'hhi':u'ኂ', 'hha':u'ኃ', 'hhE':u'ኄ', 'hhee':u'ኄ', 'hh':u'ኅ', 'hho':u'ኆ', 'hhWe':u'ኈ',\
'hhWu':u'ኍ', 'hhWi':u'ኊ', 'hhW':u'ኋ', 'hhWa':u'ኋ', 'hhWE':u'ኌ', 'hhWee':u'ኌ', 'h2e':u'ኀ', 'h2u':u'ኁ',\
'h2i':u'ኂ', 'h2a':u'ኃ', 'h2E':u'ኄ', 'h2ee':u'ኄ', 'h2':u'ኅ', 'h2o':u'ኆ', 'h2We':u'ኈ', 'h2Wu':u'ኍ', 'h2Wi':u'ኊ',\
'h2W':u'ኋ', 'h2Wa':u'ኋ', 'h2WE':u'ኌ', 'h2Wee':u'ኌ', 'h2W\'':u'ኍ', 'h2e':u'ኀ', 'h2u':u'ኁ', 'h2i':u'ኂ', 'h2a':u'ኃ',\
'h2E':u'ኄ', 'h2ee':u'ኄ', 'h2':u'ኅ', 'h2o':u'ኆ', 'h2We':u'ኈ', 'h2Wu':u'ኍ', 'h2Wi':u'ኊ', 'h2W':u'ኋ', 'h2Wa':u'ኋ',\
'h2WE':u'ኌ', 'h2Wee':u'ኌ', 'le':u'ለ', 'lu':u'ሉ', 'li':u'ሊ', 'la':u'ላ', 'lE':u'ሌ', 'lee':u'ሌ', 'l':u'ል', 'lo':u'ሎ', 'lW':u'ሏ',
'lWa':u'ሏ', 'Le':u'ለ', 'Lu':u'ሉ', 'Li':u'ሊ', 'La':u'ላ', 'LE':u'ሌ', 'Lee':u'ሌ', 'L':u'ል', 'Lo':u'ሎ', 'LW':u'ሏ', 'LWa':u'ሏ', \
'He':u'ሐ', 'Hu':u'ሑ', 'Hi':u'ሒ', 'Ha':u'ሓ', 'HE':u'ሔ', 'Hee':u'ሔ', 'H':u'ሕ', 'Ho':u'ሖ', 'HW':u'ሗ', 'HWa':u'ሗ', \
'me':u'መ', 'mu':u'ሙ','mi':u'ሚ', 'ma':u'ማ', 'mE':u'ሜ','mee':u'ሜ', 'm':u'ም','mo':u'ሞ','mW':u'ሟ','mWa':u'ሟ','mY':u'ፘ','mYa':u'ፘ',\
'Me':u'መ','Mu':u'ሙ','Mi':u'ሚ','Ma':u'ማ','ME':u'ሜ','Mee':u'ሜ','M':u'ም','Mo':u'ሞ','MW':u'ሟ','MWa':u'ሟ','MY':u'ፘ','MYa':u'ፘ',\
're':u'ረ','ru':u'ሩ','ri':u'ሪ','ra':u'ራ','rE':u'ሬ','ree':u'ሬ','r':u'ር','ro':u'ሮ','rW':u'ሯ','rWa':u'ሯ','rY':u'ፙ', 'rYa':u'ፙ',\
'Re':u'ረ','Ru':u'ሩ','Ri':u'ሪ','Ra':u'ራ','RE':u'ሬ','Ree':u'ሬ','R':u'ር','Ro':u'ሮ','RW':u'ሯ','RWa':u'ሯ','RYa':u'ፙ',\
'se':u'ሰ','su':u'ሱ','si':u'ሲ','sa':u'ሳ','sE':u'ሴ','see':u'ሴ','s':u'ስ','so':u'ሶ','sW':u'ሷ','sWa':u'ሷ',\
'`se':u'ሠ','`su':u'ሡ','`si':u'ሢ','`sa':u'ሣ','`sE':u'ሤ','`see':u'ሤ','`s':u'ሥ','`so':u'ሦ','`sW':u'ሧ','`sWa':u'ሧ',\
'sse':u'ሠ','ssu':u'ሡ','ssi':u'ሢ','ssa':u'ሣ','ssE':u'ሤ','ssee':u'ሤ','ss':u'ሥ','sso':u'ሦ','ssW':u'ሧ','ssWa':u'ሧ',\
's2e':u'ሠ','s2u':u'ሡ','s2i':u'ሢ','s2a':u'ሣ','s2E':u'ሤ','s2ee':u'ሤ','s2':u'ሥ','s2o':u'ሦ','s2W':u'ሧ','s2Wa':u'ሧ',\
'xe':u'ሸ','xu':u'ሹ','xi':u'ሺ','xa':u'ሻ','xE':u'ሼ','xee':u'ሼ','x':u'ሽ','xo':u'ሾ','xW':u'ሿ','xWa':u'ሿ',\
'Xe':u'ሸ','Xu':u'ሹ','Xi':u'ሺ','Xa':u'ሻ','XE':u'ሼ','Xee':u'ሼ','X':u'ሽ','Xo':u'ሾ','XW':u'ሿ','XWa':u'ሿ','qW':u'ቋ','qWa':u'ቋ',\
'qe':u'ቀ','qu':u'ቁ','qi':u'ቂ','qa':u'ቃ','qE':u'ቄ','qee':u'ቄ','q':u'ቅ','qo':u'ቆ','qWe':u'ቈ','qWu':u'ቍ','qWi':u'ቊ',\
'qWE':u'ቌ','qWee':u'ቌ','qW\'':u'ቍ','Qe':u'ቐ','Qu':u'ቑ','Qi':u'ቒ','Qa':u'ቓ','QE':u'ቔ','Qee':u'ቔ','Q':u'ቕ','Qo':u'ቖ',\
'QWe':u'ቘ','QWu':u'ቝ','QWi':u'ቚ','QW':u'ቛ','QWa':u'ቛ','QWE':u'ቜ','QWee':u'ቜ','QW\'':u'ቝ',\
'be':u'በ','bu':u'ቡ','bi':u'ቢ','ba':u'ባ','bE':u'ቤ','bee':u'ቤ','b':u'ብ','bo':u'ቦ','bW':u'ቧ','bWa':u'ቧ',\
'Be':u'በ','Bu':u'ቡ','Bi':u'ቢ','Ba':u'ባ','BE':u'ቤ','Bee':u'ቤ','B':u'ብ','Bo':u'ቦ',\
'BW':u'ቧ','BWa':u'ቧ','ve':u'ቨ','vu':u'ቩ','vi':u'ቪ','va':u'ቫ','vE':u'ቬ','vee':u'ቬ','v':u'ቭ','vo':u'ቮ','vW':u'ቯ','vWa':u'ቯ',\
'Ve':u'ቨ','Vu':u'ቩ','Vi':u'ቪ','Va':u'ቫ','VE':u'ቬ','Vee':u'ቬ','V':u'ቭ','Vo':u'ቮ','VW':u'ቯ','VWa':u'ቯ',\
'te':u'ተ','tu':u'ቱ','ti':u'ቲ','ta':u'ታ','tE':u'ቴ','tee':u'ቴ','t':u'ት','to':u'ቶ','tW':u'ቷ','tWa':u'ቷ',\
'ce':u'ቸ','cu':u'ቹ','ci':u'ቺ','ca':u'ቻ','cE':u'ቼ','cee':u'ቼ','c':u'ች','cW':u'ቿ','cWa':u'ቿ', 'co':u'ቾ',\
'ne':u'ነ','nu':u'ኑ','ni':u'ኒ','na':u'ና','nE':u'ኔ','nee':u'ኔ','n':u'ን','no':u'ኖ','nW':u'ኗ','nWa':u'ኗ',\
'Ne':u'ኘ','Nu':u'ኙ','Ni':u'ኚ','Na':u'ኛ','NE':u'ኜ','Nee':u'ኜ','N':u'ኝ','No':u'ኞ','NW':u'ኟ','NWa':u'ኟ',\
'a':u'አ','u':u'ኡ','U':u'ኡ','i':u'ኢ','A':u'ኣ','E':u'ኤ','I':u'እ','e':u'እ','o':u'ኦ',\
'O':u'ኦ','ea':u'ኧ','Ia':u'ኧ','`a':u'ዐ','`u':u'ዑ','`U':u'ዑ','`i':u'ዒ','`A':u'ዓ','`E':u'ዔ','`ee':u'ዔ','`I':u'ዕ','`e':u'ዕ','`o':u'ዖ',\
'`O':u'ዖ','ae':u'ዐ','a2':u'ዐ','eee':u'ዐ','Iee':u'ዐ','uu':u'ዑ','uU':u'ዑ','u2':u'ዑ','Uu':u'ዑ','Uu':u'ዑ','U2':u'ዑ','ii':u'ዒ',\
'i2':u'ዒ','aa':u'ዓ','AA':u'ዓ','Aa':u'ዓ','A2':u'ዓ','EE':u'ዔ','E2':u'ዔ','II':u'ዕ','Ie':u'ዕ','ee':u'ዕ','eI':u'ዕ','e2':u'ዕ','I2':u'ዕ',\
'oo':u'ዖ','OO':u'ዖ','o2':u'ዖ','O2':u'ዖ','oO':u'ዖ','Oo':u'ዖ','ke':u'ከ','ku':u'ኩ','ki':u'ኪ','ka':u'ካ',\
'kE':u'ኬ','kee':u'ኬ','k':u'ክ','ko':u'ኮ','kWe':u'ኰ','kWu':u'ኵ','kWi':u'ኲ','kW':u'ኳ','kWa':u'ኳ','kWE':u'ኴ','kWee':u'ኴ','kW\'':u'ኵ',\
'Ke':u'ኸ','Ku':u'ኹ','Ki':u'ኺ','Ka':u'ኻ','KE':u'ኼ','Kee':u'ኼ','K':u'ኽ','Ko':u'ኾ','KWe':u'ዀ','KWu':u'ዅ','KWi':u'ዂ','KW':u'ዃ',\
'KWa':u'ዃ','KWE':u'ዄ','KWee':u'ዄ','KW\'':u'ዅ','we':u'ወ','wu':u'ዉ','wi':u'ዊ','wa':u'ዋ','wE':u'ዌ','wee':u'ዌ','w':u'ው','wo':u'ዎ',\
'We':u'ወ','Wu':u'ዉ','Wi':u'ዊ','Wa':u'ዋ','WE':u'ዌ','Wee':u'ዌ','W':u'ው','Wo':u'ዎ',\
'ze':u'ዘ','zu':u'ዙ','zi':u'ዚ','za':u'ዛ','zE':u'ዜ','zee':u'ዜ','z':u'ዝ','zo':u'ዞ','zW':u'ዟ','zWa':u'ዟ','Ze':u'ዠ','Zu':u'ዡ','Zi':u'ዢ',\
'Za':u'ዣ','ZE':u'ዤ','Zee':u'ዤ','Z':u'ዥ','Zo':u'ዦ',\
'ZW':u'ዧ','ZWa':u'ዧ','ye':u'የ','yu':u'ዩ','yi':u'ዪ','ya':u'ያ','yE':u'ዬ','yee':u'ዬ','y':u'ይ','yo':u'ዮ',\
'Ye':u'የ','Yu':u'ዩ','Yi':u'ዪ','Ya':u'ያ','YE':u'ዬ','Yee':u'ዬ','Y':u'ይ','Yo':u'ዮ',\
'de':u'ደ','du':u'ዱ','di':u'ዲ','da':u'ዳ','dE':u'ዴ','dee':u'ዴ','d':u'ድ','do':u'ዶ','dW':u'ዷ','dWa':u'ዷ',\
'De':u'ዸ','Du':u'ዹ','Di':u'ዺ','Da':u'ዻ','DE':u'ዼ','Dee':u'ዼ','D':u'ዽ','Do':u'ዾ',\
'DW':u'ዿ','DWa':u'ዿ','je':u'ጀ','ju':u'ጁ','ji':u'ጂ','ja':u'ጃ','jE':u'ጄ','jee':u'ጄ','j':u'ጅ','jo':u'ጆ',\
'jW':u'ጇ','jWa':u'ጇ','Je':u'ጀ','Ju':u'ጁ','Ji':u'ጂ','Ja':u'ጃ',\
'JE':u'ጄ','Jee':u'ጄ','J':u'ጅ','Jo':u'ጆ','JW':u'ጇ','JWa':u'ጇ','ge':u'ገ','gu':u'ጉ','gi':u'ጊ','ga':u'ጋ','gE':u'ጌ','gee':u'ጌ','g':u'ግ',\
'go':u'ጎ','gWe':u'ጐ','gWu':u'ጕ','gWi':u'ጒ','gW':u'ጓ','gWa':u'ጓ','gWE':u'ጔ',\
'gWee':u'ጔ', 'gW\'':u'ጕ', 'Ge':u'ጘ', 'Gu':u'ጙ', 'Gi':u'ጚ', 'Ga':u'ጛ', 'GE':u'ጜ', 'Gee':u'ጜ', 'G':u'ጝ', 'Go':u'ጞ',\
'Te':u'ጠ','Tu':u'ጡ','Ti':u'ጢ','Ta':u'ጣ',\
'TE':u'ጤ','Tee':u'ጤ','T':u'ጥ','To':u'ጦ','TW':u'ጧ','TWa':u'ጧ','Ce':u'ጨ','Cu':u'ጩ','Ci':u'ጪ','Ca':u'ጫ','CE':u'ጬ','Cee':u'ጬ',\
'C':u'ጭ','Co':u'ጮ','CW':u'ጯ','CWa':u'ጯ',\
'Pe':u'ጰ','Pu':u'ጱ','Pi':u'ጲ','Pa':u'ጳ','PE':u'ጴ','Pee':u'ጴ','P':u'ጵ','Po':u'ጶ','PW':u'ጷ','PWa':u'ጷ',\
'Se':u'ጸ','Su':u'ጹ','Si':u'ጺ','Sa':u'ጻ','SE':u'ጼ','See':u'ጼ','S':u'ጽ','So':u'ጾ','SW':u'ጿ',\
'SWa':u'ጿ','`Se':u'ፀ','`Su':u'ፁ','`Si':u'ፂ','`Sa':u'ፃ','`SE':u'ፄ','`See':u'ፄ','`S':u'ፅ','`So':u'ፆ','`SW':u'ጿ','`SWa':u'ጿ','SSe':u'ፀ',\
'SSu':u'ፁ','SSi':u'ፂ','SSa':u'ፃ','SSE':u'ፄ',\
'SSee':u'ፄ','SS':u'ፅ','SSo':u'ፆ','S2e':u'ፀ','S2u':u'ፁ','S2i':u'ፂ','S2a':u'ፃ','S2E':u'ፄ','S2ee':u'ፄ','S2':u'ፅ',\
'S2o':u'ፆ','fe':u'ፈ','fu':u'ፉ','fi':u'ፊ','fa':u'ፋ','fE':u'ፌ','fee':u'ፌ','f':u'ፍ',\
'fo':u'ፎ','fW':u'ፏ','fWa':u'ፏ','fY':u'ፚ','fYa':u'ፚ','Fe':u'ፈ','Fu':u'ፉ',\
'Fi':u'ፊ','Fa':u'ፋ','FE':u'ፌ','Fee':u'ፌ','F':u'ፍ','Fo':u'ፎ','FW':u'ፏ','FWa':u'ፏ','FY':u'ፚ','FYa':u'ፚ','pe':u'ፐ','pu':u'ፑ',\
'pi':u'ፒ','pa':u'ፓ','pE':u'ፔ','pee':u'ፔ','p':u'ፕ','po':u'ፖ','pW':u'ፗ','pWa':u'ፗ', '**':u'፨', '*':u'*', '-:':u'፥', ';;':u';',\
'.':u'::', ':::':u':', '::':u'።', ':':u'፡', '\'\'':u'\'', ';':u'፤', ',,':u',', ',':u'፣', ':|:':u'፨', ':-':u'፦',\
'/':u'/', '?':u'?','??':u'፧','<':u'<','>':u'>','<<':u'«','>>':u'»','`':u'`','`?':u'፧','`!':u'!','`1':u'፩',\
'`2':u'፪','`3':u'፫','`4':u'፬','`5':u'፭','`6':u'፮','`7':u'፯','`8':u'፰','`9':u'፱','`10':u'፲',\
'`20':u'፳','`30':u'፴','`40':u'፵','`50':u'፶','`60':u'፷','`70':u'፸','`80':u'፹','`90':u'፺','`100':u'፻','`1000':u'፲፻',\
'`2000':u'፳፻','`3000':u'፴፻','`4000':u'፵፻','`5000':u'፶፻','`6000':u'፷፻','`7000':u'፸፻','`8000':u'፹፻',\
'`9000':u'፺፻','`10000':u'፼','`20000':u'፪፼','`30000':u'፫፼','`40000':u'፬፼','`50000':u'፭፼','`60000':u'፮፼','`70000':u'፯፼','`80000':u'፰፼',\
'`90000':u'፱፼','`100000':u'፲፼', \
'`200000':u'፳፼','`300000':u'፴፼','`400000':u'፵፼','`500000':u'፶፼','`600000':u'፷፼','`700000':u'፸፼',\
'`800000':u'፹፼','`900000':u'፺፼','`1000000':u'፻፼'}


#we need to start mapping from the maximum key combination to form amharic char first to the minimum in the dictionary (5,4,3,2,1)   
    mappings = [(-len(ascii_chars), unicode(ascii_chars), am_char) for ascii_chars, am_char in amharic_ascii_table.items()] # convert dictionary to (len(ascii_chars),uni(ascii_chars),uni(am_chars)) and list
    mappings.sort() # sorts the key (-5,key,value) all in unicode

    text_data = input_data.decode('ascii') # Explicitly encode the input text using ascii / the file input converted to unicode

    for _junk, ascii_text, am_text in mappings:      # _ read and discard put k,v to K_text, v_text
        text_data = text_data.replace(ascii_text, am_text) # replace ascii to with amharic the long combination first

# to add flexibility if '-' are used as inter-character markers, as in n-gu-sE they should be deleted at last(not first)
    text_data = text_data.replace(u'-', '')
    text_data = text_data.replace(u'#', '')
    print "untransliterated:", set(letter for letter in text_data if 0x20 < ord(letter) < 0x7f) #all ascii printable chars 

    BOM = u'\ufeff'
    outf = open(raw_input("Enter name of file to write the output:> "), 'w+')
    outf.write(BOM.encode('utf8')) # Adds byte order marking at the begining for the sake of explicit encoding information
    outf.write(text_data.encode('utf8')) # decode the chars using utf-8 write to the given file
    outf.close() # close the file
#except IndexError:
if __name__ == '__main__':
    try:
        translitrate()
    
    finally:
        print ('Check if there is/are any unmapped char/s')
