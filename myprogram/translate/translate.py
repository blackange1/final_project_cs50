import os
A = [[],['','эй','оу','и:','ай','ай','ю:'],['','э','о','е','и','и','а'],['','а:','о:','э:','э:','э:','э:'],['','эа','о:','иэ','аиэ','аиэ','юэ']]
primer = ['same','rat','car','care','note','hot','sort','store','he','red','term','mere',
'fine','bit','fir','fire','my','myth','byrd','tyre','cube','run','fur','cure']

primer2 = ['rain','may','sea','bee','new','point','boy','book','too','out','brown','chair','engineer','out','moor']

primer3 = ['chalk','wall','also','work','want','warm','light','quantity','quarter','shame','chest','catch','crack','thick','myth','this','bathe',
'what','who','question','long','thank','write']
print('################start################')
def tableA(word,i):
    if word[i+1] == 'r':
        if word[i+2] == 'e':
            i += 2
            return [4,i]
        else:
            i += 1
            return [3,i]
    for j in 'aoeiy':
        if word[i+2] == j:
            return [1,i]
    if word[i+1] == '_' and word[i+2] == '_':
        return [1,i]
    return [2,i]

def translation(word):
	#word = 'chalk'
	word = word.lower()
	#print(word)
	end = len(word)-1
	word = word + '____'
	rule = ''#правила
	rez = ''
	i = 0
	while i <= end:
		#a
		if word[i] == 'a':
			if word[i+1] == 'i':
				if word[i+1] == 'r':
					#print('эa')
					rez = rez + 'эа'
					rule = rule + 'B8'
					i += 2
				else:
					#print('эй')
					rez = rez + 'эй'
					rule = rule + 'B1'
					i += 1
			elif word[i+1] == 'y':
				#print('эй')
				rez = rez + 'эй'
				rule = rule + 'B1'
				i += 1
			elif word[i+1] == 'l':
				#print('о:л')
				rez = rez + 'о:л'
				rule = rule + 'C1'
				i += 1
			else:
				t = tableA(word,i)
				#print(A[t[0]][1])
				rez = rez + A[t[0]][1]
				i = t[1]
				rule = rule + 'A' + '1' + str(t[0])
		#b
		elif word[i] == 'b':
			#print('б')
			rez = rez + 'б'
		elif word[i] == 'c':
			if word[i+1] == 'h':
				#print('ч')
				rez = rez + 'ч'
				rule = rule + 'C7'
				i += 1
			elif word[i+1] == 'k' and i>0:
				if word[i-1] == 'a' or word[i-1] == 'o' or word[i-1] == 'e' or word[i-1] == 'i' or word[i-1] == 'y' or word[i-1] == 'u':
					#print('к')
					rez = rez + 'к'
					rule = rule + 'C9'
					i += 1
				else:
					#print('k')
					rez = rez + 'к'
			else:
				#print('k')
				rez = rez + 'к'
		elif word[i] == 'd':
			#print('д')
			rez = rez + 'д'
		elif word[i] == 'e':
			if end > 2 and i == end:
				break
			else:
				if word[i+1] == 'e':
					if word[i+2] == 'r':
						#print('иэ')
						rez = rez + 'из'
						rule = rule + 'B9'
						i += 2
					else:
						#print('и:')
						rez = rez + 'и:'
						rule = rule + 'B2'
						i += 1
				elif word[i+1] == 'a':
					#print('и:')
					rez = rez + 'и:'
					rule = rule + 'B2'
					i += 1
				elif word[i+1] == 'w':
					#print('ю:')
					rez = rez + 'ю:'
					rule = rule + 'B3'
					i += 1
				else:
					t = tableA(word,i)
					#print(A[t[0]][3])
					rez = rez + A[t[0]][3]
					i = t[1]
					rule = rule + 'A' + '3' + str(t[0])
		elif word[i] == 'f':
			#print('ф')
			rez = rez + 'ф'
		elif word[i] == 'g':
			if i == 0:
				#print('г')
				rez = rez + 'г'
			else:
				#print('дж')
				rez = rez + 'дж'
		elif word[i] == 'h':
			#print('х')
			rez = rez + 'х'
		elif word[i] == 'i': 
			if word[i+1] == 'g' and word[i+2] == 'h':
				#print('ай')
				rez = rez + 'ай'
				rule = rule + 'C4'
				i += 2
			else:
				t = tableA(word,i)
				#print(A[t[0]][4])
				rez = rez + A[t[0]][4]
				i = t[1]
				rule = rule + 'A' + '4' + str(t[0])
		elif word[i] == 'j':
			#print('ж')
			rez = rez + 'ж'
		elif word[i] == 'k':
			#print('к')
			rez = rez + 'к'
		elif word[i] == 'l':
			#print('л')
			rez = rez + 'л'
		elif word[i] == 'm':
			#print('м')
			rez = rez + 'м'
		elif word[i] == 'n':
			if i > 0:
				if word[i-1] == 'a' or word[i-1] == 'o' or word[i-1] == 'e' or word[i-1] == 'i' or word[i-1] == 'y' or word[i-1] == 'u':
					if word[i+1] == 'k':
						#print('нк')
						rez = rez + 'нк'
						rule = rule + 'C14'
						i += 1
					elif word[i+1] == 'g' and i+1 == end:
						#print('н')
						rez = rez + 'н'
						rule = rule + 'C13'
						i += 1
					else:
						#print('н')
						rez = rez + 'н'
				else:
					#print('н')
					rez = rez + 'н'
			else:
				#print('н')
				rez = rez + 'н'
		elif word[i] == 'o':
			if word[i+1] == 'o':
				if word[i+2] == 'k':
					#print('у')
					rez = rez + 'у'
					rule = rule + 'B5'
					i += 1
				elif word[i+2] == 'r':
					#print('о:')
					rez = rez + 'о:'
					rule = rule + 'B11'
					i += 2
				else:
					#print('у:')
					rez = rez + 'у:'
					rule = rule + 'B6'
					i += 1
			elif word[i+1] == 'u':
				if word[i+2] == 'r':
					#print('ауэ')
					rez = rez + 'эуе'
					rule = rule + 'B10'
					i += 2
				else:
					#print('ау')
					rez = rez + 'ау'
					rule = rule + 'B7'
					i += 1
			elif word[i+1] == 'w':
				#print('ау')
				rez = rez + 'ау'
				rule = rule + 'B7'
				i += 1
			elif word[i+1] == 'i' or word[i+1] == 'y':
				#print('ой')
				rez = rez + 'ой'
				rule = rule + 'B4'
				i += 1
			else:
				t = tableA(word,i)
				#print(A[t[0]][2])
				rez = rez + A[t[0]][2]
				i = t[1]
				rule = rule + 'A' + '2' + str(t[0])
		elif word[i] == 'p':#qwer
			#print('п')
			rez = rez + 'п'
		elif word[i] == 'q':
			if word[i+1] == 'u':
				if word[i+2] == 'a':
					if word[i+3] == 'r':
						#print('кво')
						rez = rez + 'кво'
						rule = rule + 'C5'
						i += 3
					elif word[i+3] != 'a' and word[i+3] != 'o' and word[i+3] != 'e' and word[i+3] != 'i' and word[i+3] != 'y' and word[i+3] != 'u' and word[i+3] != '_':
						#print('кво:')
						rez = rez + 'кво:'
						rule = rule + 'C5'
						i += 2
					else:
						#print('кв')
						rez = rez + 'кв'
						rule = rule + 'C12'
						i += 1
				elif word[i+2] == 'o' or word[i+2] == 'e' or word[i+2] == 'i' or word[i+2] == 'y' or word[i+2] == 'u':
					#print('кв')
					rez = rez + 'кв'
					rule = rule + 'C12'
					i += 1
			else:
				#print('?')
				rez = rez + '?'
		elif word[i] == 'r':
			#print('р')
			rez = rez + 'р'
		elif word[i] == 's':
			if word[i+1] == 'h':
				#print('ш')
				rez = rez + 'ш'
				rule = rule + 'C6'
				i += 1
			else:
				#print('с')
				rez = rez + 'с'
		elif word[i] == 't':
			if word[i+1] == 'c' and word[i+2] == 'h' and i>0 and (word[i-1] == 'a' or word[i-1] == 'o' or word[i-1] == 'e' or word[i-1] == 'i' or word[i-1] == 'y' or word[i-1] == 'u'):
				#print('ч')
				rez = rez + 'ч'
				rule = rule + 'C8'
				i += 2
			elif word[i+1] == 'h':
				if i == 0 or i == end - 1:
					#print('c')
					rez = rez + 'с'
					rule = rule + 'C10'
					i += 1
				else:
					#print('з')
					rez = rez + 'з'
					rule = rule + 'C10'
					i += 1
			else:
				#print('т')
				rez = rez + 'т'
		elif word[i] == 'u':
			t = tableA(word,i)
			#print(A[t[0]][6])
			rez = rez + A[t[0]][6]
			i = t[1]
			rule = rule + 'A' + '6' + str(t[0])
		elif word[i] == 'v':
			#print('в')
			rez = rez + 'в'
		elif word[i] == 'w':
			if word[i+1] == 'o':
				if word[i+2] != 'a' and word[i+2] != 'o' and word[i+2] != 'e' and word[i+2] != 'i' and word[i+2] != 'y' and word[i+2] != 'u' and word[i+2] != '_':
					#print('вэ:')
					rez = rez + 'вэ:'
					rule = rule + 'C2'
					i += 1
				else:
					#print('в')
					rez = rez + 'в'
			elif word[i+1] == 'a':#doraotat
				if word[i+2] == 'r':
					#print('во:')
					rez = rez + 'во:'
					rule = rule + 'C3'
					i += 2
				elif word[i+2] != 'a' and word[i+2] != 'o' and word[i+2] != 'e' and word[i+2] != 'i' and word[i+2] != 'y' and word[i+2] != 'u' and word[i+2] != '_':
					#print('во')
					rez = rez + 'во'
					rule = rule + 'C3'
					i += 1
			elif word[i+1] == 'h':
				if word[i+2] == 'o':
					#print('х')
					rez = rez + 'х'
					rule = rule + 'C11'
					i += 1
				elif (word[i+2] == 'a' or  word[i+2] == 'e' or word[i+2] == 'i' or word[i+2] == 'y' or word[i+2] == 'u') and i == 0:
					#print('ув')
					rez = rez + 'ув'
					rule = rule + 'C11'
					i += 1
				else:
					#print('в')
					rez = rez + 'в'
			elif word[i+1] == 'r' and (word[i+2] == 'a' or word[i+2] == 'o' or word[i+2] == 'e' or word[i+2] == 'i' or word[i+2] == 'y' or word[i+2] == 'u') and i == 0:
				#print('р')
				rez = rez + 'р'
				rule = rule + 'C15'
				i += 1
			else:
				#print('в')
				rez = rez + 'в'
		elif word[i] == 'x':
			#print('кс')
			rez = rez + 'кс'
		elif word[i] == 'y':
			t = tableA(word,i)
			#print(A[t[0]][5])
			rez = rez + A[t[0]][5]
			i = t[1]
			rule = rule + 'A' + '5' + str(t[0])
		elif word[i] == 'z':
			#print('з')
			rez = rez + 'з'
		i += 1
	#print(rule)
	return [rez,rule]

def main(p):#str
	arr_words = []
	arr_translation = []
	arr_words_for_rulle = []
	arr_trans_for_rulle = []
	arr_rulle = []
	word = ''
	j = 0
	global findex
	while j < len(p):
		c = p[j]
		if c == '\n':
			if word != '':
				arr_words.append(word)
				trans = translation(word)#peremennay odnorazovay
				arr_translation.append(trans[0])
				arr_rulle.append(trans[1])
				word = ''
			i = 0
			#print('abzach')
			arr_words_for_rulle = arr_words.copy()
			arr_trans_for_rulle = arr_translation.copy()
			#print(arr_words_for_rulle)
			while i < len(arr_words):
				len_one = len(arr_words[i])
				len_two = len(arr_translation[i])
				if len_one != len_two:
					if len_one > len_two:
						arr_translation[i] = arr_translation[i] + ' '*(len_one-len_two)
					else:
						arr_words[i] = arr_words[i] + ' '*(len_two-len_one)#arr_words_for_rulle = [] and arr_rulle = []
				ln_one = len(arr_words_for_rulle[i])
				ln_two = len(arr_rulle[i])
				ln_tree = len(arr_trans_for_rulle[i])
				max_ln = ln_tree
				if ln_two > ln_tree:
					if ln_one > ln_two:
						max_ln = ln_one
					else:
						max_ln = ln_two
				elif ln_one > ln_tree:
						max_ln = ln_one
				arr_words_for_rulle[i] = arr_words_for_rulle[i] + ' '*(max_ln-ln_one)
				arr_rulle[i] = arr_rulle[i] + ' '*(max_ln-ln_two)
				arr_trans_for_rulle[i] = arr_trans_for_rulle[i] + ' '*(max_ln-ln_tree)
				i += 1
			print(arr_words)
			if arr_words != []:
				low = arr_words[0][0].lower()
				if low == 'q' or low == 'w' or low == 'e' or low == 'r' or low == 't' or low == 'y' or low == 'u' or low == 'i' or low == 'o' or low == 'p' or low == 'a' or low == 's' or low == 'd' or low == 'f' or low == 'g' or low == 'h' or low == 'j' or low == 'k' or low == 'l' or low == 'z' or low == 'x' or low == 'c' or low == 'v' or low == 'b' or low == 'n' or low == 'm':
					findex.write('<p>')
					for h in arr_words:
						findex.write('<a href = "https://wooordhunt.ru/word/'+str(h)+'" target="_blank">'+str(h)+'     </a>\n' )
					findex.write('</p>')
			print(arr_translation)
			print(arr_words_for_rulle)
			print(arr_trans_for_rulle)
			print(arr_rulle)
			wfiletext(arr_words,arr_translation)
			wfiletextandrule(arr_words_for_rulle,arr_trans_for_rulle,arr_rulle)
			
			arr_words = []
			arr_translation = []
			arr_words_for_rulle = []
			arr_trans_for_rulle = []
			arr_rulle = []
			print('')
			#print('ok')
			#j += 1
		elif c == ' ' or c == ',' or c == '.' or c == '!' or c == '?' or c == '1' or c == '2' or c == '3' or c == '4' or c == '5' or c == '6' or c == '7' or c == '8' or c == '9' or c == '0':
			if word != '':
				arr_words.append(word)
				trans = translation(word)#peremennay odnorazovay
				arr_translation.append(trans[0])
				arr_rulle.append(trans[1])
				word = ''
		else:
			word = word + c
		j += 1
def wfiletext(w,t):
	global ftext
	wtext(w,ftext)
	wtext(t,ftext)
	ftext.write('\n')

def wfiletextandrule(w,t,r):
	global ftextandrule
	wtext(w,ftextandrule)
	wtext(t,ftextandrule)
	wtext(r,ftextandrule)
	ftextandrule.write('\n')

def wtext(arr,f):
	for i in arr:
		f.write(i)
		f.write('   ')
	f.write('\n')
#primer4 = 'Have we lost the spark or a guide? \nWhat s the latest on the screen? \nCan t be too late to turn around \nI need all the help from you\n'
#main(primer)
#main(primer2)
#main(primer3)
#main(pprimer4)
#print(primer4)
#main(primer4)
file = open(r'D:\myprogram\translate\original_text.txt')
filestr = file.read()
#print(filestr)
findex = open(r'D:\myprogram\translate\index.html', 'w')
ftext = open(r'D:\myprogram\translate\translate_text.txt', 'w')
ftextandrule = open(r'D:\myprogram\translate\translate_text_and_rule.txt', 'w')

findex.write('<!DOCTYPE html>\n<html lang="ru">\n<head>\n\t<title>translate</title>\n\t<style>\n\t\tbody{padding: 5rem; background-color: #f0f0f0; opacity: 0.5;}\n\t\ta{color: black;text-decoration: none;font-size: 2rem;}\n\t\ta:hover{border: 2px solid red;border-radius: 10px;padding: 2px 8px;color: red;}\n\t</style>\n</head>\n<body>\n')
main(filestr)
findex.write('\n</body>\n</html>')

ftext.close()
ftextandrule.close()
findex.close()
os.startfile(r'D:\myprogram\translate\translate_text.txt')
#print('ok end')
input('для виходу з програми натисніть Enter')