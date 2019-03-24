import requests
probel = '  '
fsite = open(r'D:\myprogram\translate\index.html')
fstr = str(fsite.read())
fsite.close()
#findex2 = open(r'D:\myprogram\translate\index2.html','w')
#intro = open(r'D:\myprogram\translate\intro.txt','w')
#f = open(r'D:\myprogram\translate\super_translate_text.html', 'w')

###<руский перевод
foriginal = open(r'D:\myprogram\translate\original_text.txt')
soriginal = foriginal.read()
foriginal.close()
ori = 0
arrori = []
sori = ''
lenori = len(soriginal)-1

while ori <= lenori:
	if soriginal[ori] == '\n':
		ori += 1
		if ori >= lenori:
			break
		else:
			while ori <= lenori:
				if soriginal[ori] == '\n':
					break
				sori += soriginal[ori]
				ori += 1
			if sori != '':
				arrori.append(sori)
				sori = ''
	ori += 1
ij = 0
###>руский перевод
#print(arrori)

i = 79
a = ''
word1 = []
translate1 = []

while i < len(fstr):
	#print(i)
	#findex2.write(fstr[i])
	if fstr[i] == '/' and fstr[i+1] == 'h' and fstr[i+2] == 't' and fstr[i+3] == 'm':
		print('\nTHE END')
		#f.write('\nTHE END')
		break
	elif fstr[i] == '<' and fstr[i+1] == 'p' and fstr[i+2] == '>':
		print('')
		#f.write('\n')
		while True:
			#print('while_'+str(i))
			if fstr[i] == '<' and fstr[i+1] == '/' and fstr[i+2] == 'p' and fstr[i+3] == '>':
				k = 0
				###<руский перевод
				#print(arrori[ij])
				ij += 1
				###>руский перевод
				while k < len(word1):
					lw = len(word1[k]) 
					lt = len(translate1[k])
					if lw - lt != 0:
						if lw - lt > 0:
							translate1[k] += ' '*(lw - lt)
						else:
							word1[k] += ' '*(lt - lw)
					#intro.write(word1[k] + ' ')#?str
					
					print(word1[k] + probel,end = '')
					#f.write(word1[k] + probel)
					k += 1
				print('')
				#f.write('\n')
				#print(word1)
				#print(translate1)
				k = 0
				
				while k < len(translate1):
					print(translate1[k] + probel, end = '')
					#conteiner = translate1[k] + probel
					#print(type(conteiner))
					#f.write(conteiner)
					k += 1
				print('')
				#f.write('\n')
				

				#intro.write('\n\n')
				
				####write
				word1 = []
				translate1 = []
				break
			elif  fstr[i] == '"':
				i += 1
				while fstr[i] != '"':
					a = a + str(fstr[i])
					i += 1
				########word
				#####print(a)
				i += 18
				w = ''
				while fstr[i] != ' ':
					if fstr[i] == '<':
						break
					w = w + str(fstr[i])#good
					i += 1
				word1.append(w)
				#doc = requests.get('https://wooordhunt.ru/word/have').content.decode('utf-8',errors='ignore')
				##print(a)
				doc = requests.get(a).content.decode('utf-8',errors='ignore')
				j = doc.find('transcription')
				##print(j)
				trsite = ''
				if j != -1:
					j += 17
					while True:
						if doc[j] == '|':
							break
						else:
							trsite += doc[j]
						j += 1
					##print(trsite)
					translate1.append(trsite)
				else:
					trsite = 'NaN'
					translate1.append(trsite)
					#print(trsite)
				a = ''
			i += 1
		#print('abzach')
	i += 1

#findex2.close()
#intro.close()
#f.close()
#os.startfile(r'D:\myprogram\translate\super_translate_text.txt')
input('для виходу з програми натисніть Enter')
