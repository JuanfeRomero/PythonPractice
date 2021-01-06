def hidden_anagram(text, phrase):
	stripPhrase = ''.join(e for e in phrase if e.isalnum()).lower()
	stripText = ''.join(e for e in text if e.isalnum()).lower()
	filteredText =  ''.join((filter(lambda x: x in stripPhrase, stripText)))
	counter = 0
	filteredLen = len(filteredText)
	phraseLen = len(stripPhrase)
	if filteredLen < phraseLen:
		return 'noutfond'
	while counter < filteredLen:
		checkMatch = filteredText[counter:phraseLen+counter]
		if sorted(checkMatch) == sorted(stripPhrase):
			return checkMatch
		else:
			counter +=1
	return 'noutfond'