class TrieNode():

	def __init__(self):
		self.hasWord = False
		self.children = {}

class Trie():

	def __init__(self):
		self.root = TrieNode()

	def addWord(self, word):
		curNode = self.root
		word = word.lower()
		for char in word:
			if char not in curNode.children:
				curNode.children[char] = TrieNode()
			curNode = curNode.children[char]

		curNode.hasWord = True

	def initializeTrie(self, Entries):
		for word in Entries:
			self.addWord(word)

	def autoComplete(self, prefix):
		prefix = prefix.lower()
		curNode = self.root
		for char in prefix:
			if char not in curNode.children:
				return []
			curNode = curNode.children[char]

		result = []
		self.dfs(result, curNode, prefix)
		return result

	def dfs(self, result, curNode, prefix):
		if curNode.hasWord:
			result.append(prefix)

		for key, child in curNode.children.items():
			self.dfs(result, child, prefix + key)


if __name__ == '__main__':
	test = Trie()
	entries = ['Man United', 'Man City', 'Arsenal', 'Ajax', 'Real Madrid', 'Barcelona', 'Real Malgb', 'Barton', 'Milwall', 'Malaga']
	test.initializeTrie(entries)
	#print test.autoComplete('M')
	#print test.autoComplete('Ma')
	#print test.autoComplete('Man')
	#print test.autoComplete('Man ')
	#print test.autoComplete('man u')
	#print test.autoComplete('A')
	#print test.autoComplete('Ar')
	#print test.autoComplete('real ')
	#print test.autoComplete('real m')
	#print test.autoComplete('real ma')
	#print test.autoComplete('real mad')






