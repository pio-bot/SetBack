import random

class DeckOfCards:
	def __init__(self):
		self.deck = []

	def Deck(self):
		self.suits = ["hearts", "diamonds", "spades", "clubs"]
		self.values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
		self.deck = [[v,s] for s in self.suits for v in self.values]

	def Shuffle(self):
		random.shuffle(self.deck)

	def PrintDeck(self):
		print(self.deck)

	def __getitem__(self, value):
		return self.deck[value]


class SetBack:
	def __init__(self):
		
		self.gameDeck = DeckOfCards()
		self.gameDeck.Deck()
		self.gameDeck.Shuffle()
		#self.gameDeck.PrintDeck()

	def PrintGameDeck(self):
		print(self.gameDeck)

	def DealHands(self):
		self.player1 = self.gameDeck[0:6]
		self.player2 = self.gameDeck[6:12]
		self.player3 = self.gameDeck[12:18]
		self.player4 = self.gameDeck[18:24]
		
		
	def PrintHands(self):
		print(f"Player1 hand {self.player1}\nplayer2 hand {self.player2}\nplayer3 hand {self.player3}\nplayer4 hand {self.player4}\n")

	def Bid(self):
		self.player1Bid = input("Enter your bid player 1: ")
		self.player2Bid = input("Enter your bid player 2: ")
		self.player3Bid = input("Enter your bid player 3: ")
		self.player4Bid = input("Enter your bid player 4: ")
		self.bidList = [self.player1Bid,self.player2Bid,self.player3Bid,self.player4Bid]
		self.playerToMove = self.bidList.index(max(self.bidList))
		self.printPlayerToMove = self.playerToMove + 1
		self.maxBid = max(self.player1Bid, self.player2Bid, self.player3Bid, self.player4Bid)

	def PrintBids(self):
		print(f"the bids are {self.player1Bid}, {self.player2Bid}, {self.player3Bid}, {self.player4Bid} the max is {self.maxBid}, {self.printPlayerToMove} starts")

	def Turn(self):
		self.turnList = [] 
		if self.playerToMove == 0:
			self.cardPlayed = input("Player 1 what card do you want to play? ")
			self.turnList.append(self.player1[int(self.cardPlayed)])
			self.player1.remove(self.player1[int(self.cardPlayed)])
			self.cardPlayed = input("Player 2 what card do you want to play? ")
			self.turnList.append(self.player2[int(self.cardPlayed)])
			self.player2.remove(self.player2[int(self.cardPlayed)])
			self.cardPlayed = input("Player 3 what card do you want to play? ")
			self.turnList.append(self.player3[int(self.cardPlayed)])
			self.player3.remove(self.player3[int(self.cardPlayed)])
			self.cardPlayed = input("Player 4 what card do you want to play? ")
			self.turnList.append(self.player4[int(self.cardPlayed)])
			self.player4.remove(self.player4[int(self.cardPlayed)])
		elif self.playerToMove == 1:
			self.cardPlayed = input("Player 2 what card do you want to play? ")
			self.turnList.append(self.player2[int(self.cardPlayed)])
			self.player2.remove(self.player2[int(self.cardPlayed)])
			self.cardPlayed = input("Player 3 what card do you want to play? ")
			self.turnList.append(self.player3[int(self.cardPlayed)])
			self.player3.remove(self.player3[int(self.cardPlayed)])
			self.cardPlayed = input("Player 4 what card do you want to play? ")
			self.turnList.append(self.player4[int(self.cardPlayed)])
			self.player4.remove(self.player4[int(self.cardPlayed)])
			self.cardPlayed = input("Player 1 what card do you want to play? ")
			self.turnList.append(self.player1[int(self.cardPlayed)])
			self.player1.remove(self.player1[int(self.cardPlayed)])
		elif self.playerToMove == 2:
			self.cardPlayed = input("Player 3 what card do you want to play? ")
			self.turnList.append(self.player3[int(self.cardPlayed)])
			self.player3.remove(self.player3[int(self.cardPlayed)])
			self.cardPlayed = input("Player 4 what card do you want to play? ")
			self.turnList.append(self.player4[int(self.cardPlayed)])
			self.player4.remove(self.player4[int(self.cardPlayed)])
			self.cardPlayed = input("Player 1 what card do you want to play? ")
			self.turnList.append(self.player1[int(self.cardPlayed)])
			self.player1.remove(self.player1[int(self.cardPlayed)])
			self.cardPlayed = input("Player 2 what card do you want to play? ")
			self.turnList.append(self.player2[int(self.cardPlayed)])
			self.player2.remove(self.player2[int(self.cardPlayed)])
		elif self.playerToMove == 3:
			self.cardPlayed = input("Player 4 what card do you want to play? ")
			self.turnList.append(self.player4[int(self.cardPlayed)])
			self.player4.remove(self.player4[int(self.cardPlayed)])
			self.cardPlayed = input("Player 1 what card do you want to play? ")
			self.turnList.append(self.player1[int(self.cardPlayed)])
			self.player1.remove(self.player1[int(self.cardPlayed)])
			self.cardPlayed = input("Player 2 what card do you want to play? ")
			self.turnList.append(self.player2[int(self.cardPlayed)])
			self.player2.remove(self.player2[int(self.cardPlayed)])
			self.cardPlayed = input("Player 3 what card do you want to play? ")
			self.turnList.append(self.player3[int(self.cardPlayed)])
			self.player3.remove(self.player3[int(self.cardPlayed)])
		#print(self.turnList)
	def SetTrumpSuit(self):
		self.trumpSuit = self.turnlist[0][1]

	def DetermineTrickWinner(self):
		self.turnSuit = self.turnList[0][1]
		for i in range(len(self.turnList)):
			if self.turnList[i][0] == 'Jack':
				self.turnList[i][0] = '11'
			if self.turnList[i][0] == 'Queen':
				self.turnList[i][0] = '12'
			if self.turnList[i][0] == 'King':
				self.turnList[i][0] = '13'
			if self.turnList[i][0] == 'Ace':
				self.turnList[i][0] = '14'
		self.possibleWinners = [int(i[0]) for i in self.turnList if i[1] == self.turnSuit or i[1] == self.trumpSuit]
		self.roundWinner = max(self.possibleWinners)
		print(self.roundWinner)



game = SetBack()
game.DealHands()
game.PrintHands()
game.Bid()
game.PrintBids()
game.Turn()
game.SetTrumpSuit()
game.PrintHands() 
game.DetermineTrickWinner()  
