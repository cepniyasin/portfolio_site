// scroll to top functionality
const scrollUp = document.querySelector("#scroll-up");

scrollUp.addEventListener("click", () => {
  window.scrollTo({
    top: 0,
    left: 0,
    behavior: "smooth",
  });
});


// Nav hamburgerburger selections

const burger = document.querySelector("#burger-menu");
const ul = document.querySelector("nav ul");
const nav = document.querySelector("nav");

burger.addEventListener("click", () => {
  ul.classList.toggle("show");
});

// Close hamburger menu when a link is clicked

// Select nav links
const navLink = document.querySelectorAll(".nav-link");

navLink.forEach((link) =>
  link.addEventListener("click", () => {
    ul.classList.remove("show");
  })
);

// BLACKJACK
let sum = 0
let hasBlackjack = false
let isAlive = true
let dealerIsAlive = true
let gameIsOn = false
let currentCards = []

let player = {
	name: "Elon Musk",
	chip: 100,
	active: true}

let message = ""
let messageEL = document.getElementById("message-el")
let betMessageEl = document.getElementById("bet-message-el")
let betEl = document.getElementById("bet-el")
let sumEl = document.getElementById("sum-el")
let cardEl = document.querySelector("#card-el")
let playerEl = document.querySelector("#player-el")
let chipsEl = document.querySelector("#chips-el")
let dealerCards = document.querySelector("#dealercard-el")
let dealerSum = document.querySelector("#dealersum-el")

let dealerCardsList=[]
let dealerScore=0
let bet=5


playerEl.textContent ="Player Name: " + player["name"]
chipsEl.textContent = "Chips: " + "$" + player.chip

function increase(){
	if (bet+5 <= player.chip && gameIsOn === false) {
		bet += 5
		betEl.textContent = bet +"$"
	}
}


function decrease(){
	if (bet-5 >= 5 && gameIsOn === false) {
		bet -= 5
		betEl.textContent = bet +"$"
	}
}


function dealer() {
	if (gameIsOn === true) {
		dealerCards.textContent = "Dealer's Cards: " + dealerCardsList[0] +" "+dealerCardsList[1]
		dealerScore=dealerCardsList[0]+dealerCardsList[1]
		dealerSum.textContent = "Sum: "+ dealerScore
		dealer_pull_card()


function dealer_pull_card(){
		if (dealerScore > 21){
			dealerIsAlive = false
			checkresults()
		}else if (dealerScore > 16) {
			checkresults()
		}else if (dealerScore < 17 && gameIsOn===true) {
			let newRandomCard = getRandomCard(dealerScore)
			dealerCardsList.push(newRandomCard)
			dealerScore += newRandomCard

			if (dealerScore > 21) {check_As(dealerCardsList)}
			dealerScore = 0
			for (i=0; i < dealerCardsList.length; i++) {dealerScore+=dealerCardsList[i]}

			dealerSum.textContent = "Sum: "+ dealerScore
			dealerCards.textContent += " " + newRandomCard
			if (dealerScore < 17 ) {
				let newRandomCard2 = getRandomCard(dealerScore)
				dealerCardsList.push(newRandomCard2)
				dealerScore += newRandomCard2

				if (dealerScore > 21) {check_As(dealerCardsList)}
				dealerScore = 0
				for (i=0; i < dealerCardsList.length; i++) {dealerScore+=dealerCardsList[i]}

				dealerSum.textContent = "Sum: "+ dealerScore
				dealerCards.textContent += " " + newRandomCard2

				if  (dealerScore < 17 ) {
					let newRandomCard3 = getRandomCard(dealerScore)
					dealerCardsList.push(newRandomCard3)
					dealerScore += newRandomCard3

					if (dealerScore > 21) {check_As(dealerCardsList)}
					dealerScore = 0
					for (i=0; i < dealerCardsList.length; i++) {dealerScore+=dealerCardsList[i]}

					dealerSum.textContent = "Sum: "+ dealerScore
					dealerCards.textContent += " " + newRandomCard3

						if  (dealerScore < 17 ) {
						let newRandomCard4 = getRandomCard(dealerScore)
						dealerCardsList.push(newRandomCard4)
						dealerScore += newRandomCard4
						if (dealerScore > 21) {check_As(dealerCardsList)}
						dealerScore = 0
						for (i=0; i < dealerCardsList.length; i++) {dealerScore+=dealerCardsList[i]}

						dealerSum.textContent = "Sum: "+ dealerScore
						dealerCards.textContent += " " + newRandomCard4
					}
				}
			}
		}
		}
			dealerCards.textContent = "Dealer's Cards: "
			for (i = 0; i < dealerCardsList.length; i++ ) {
			if (dealerCardsList[i]==1 || dealerCardsList[i]==11 ) { dealerCardsList[i]="A"}
			dealerCards.textContent += " " + dealerCardsList[i]
			}
		checkresults()
	}
}

function win () {
	if (gameIsOn === true) {
	player.chip += bet
	}
	gameIsOn = false
}

function lose () {
	if (gameIsOn === true) {
	player.chip -= bet
	}
	gameIsOn = false
}

function check_As(card_list) {
	for (i=0; i < card_list.length; i++){
		if (card_list[i] === 11) {
			card_list[i] = 1
		}
	}
}


function checkresults() {
	if (dealerScore > 21 ) {
		dealerIsAlive = false
		message = "Dealer is Bust! Player Wins!"
				win()
			}else if (sum > 21) {
				message = "Bust! Dealer Wins!"
				lose()
			}else if (dealerScore < sum) {
				message = "Player Wins!"
				win()
			}else if (dealerScore > sum ) {
				message = "Dealer Wins!"
				lose()
			}else if (dealerScore === sum) {
				message = "Tie"
			}
	chipsEl.textContent = "Chips: " + "$" + player.chip
	messageEL.textContent = message
	gameIsOn = false
	if ( player.chip <= 0 ) {
		bet = 5
	} else if (player.chip < bet) { bet=player.chip}
	betEl.textContent = bet +"$"

}

function start() {
	if (gameIsOn == true) {
		player.chip -= bet
		chipsEl.textContent= "Chips: " + "$" + player.chip
	}
	dealerCardsList=[]
	dealerCardsList.push(getRandomCard(0))
	dealerCardsList.push(getRandomCard(dealerCardsList[0]))
	dealerScore = dealerCardsList[0]+dealerCardsList[1]
	dealerCards.textContent = "Dealer's Cards: " + dealerCardsList[0] +" X"
	dealerSum.textContent = "Sum: " + dealerCardsList[0]
	playerEl.textContent ="Player Name: " + player["name"]
	chipsEl.textContent = "Chips: " + "$" + player.chip
	dealerIsAlive = true
	isAlive = true
	hasBlackjack = false
	gameIsOn = true
	cardEl.textContent = "Player's Cards: "
	currentCards = []
	currentCards.push(getRandomCard(0))
	currentCards.push(getRandomCard(currentCards[0]))
	sum = 0
	if (currentCards[0]+currentCards[1] === 22){
			currentCards[1] = 1}
	for ( let i = 0; i < 2; i++) {
		cardEl.textContent += " " + currentCards[i]
		sum += currentCards [i]
	}
	renderGame()
	sumEl.textContent = "Sum: " + sum
}

function renderGame() {
		if (sum <= 20 && gameIsOn===true){
		message = "Would u like a new card?"
	} else if (sum === 21) {
		hasBlackjack = true
		checkresults()
		gameIsOn = false
	} else {
		isAlive = false
	//	gameIsOn = false
		dealerIsAlive = true
		checkresults()
	}
	messageEL.textContent = message
}

function new_card() {
	if (hasBlackjack === false && isAlive === true && gameIsOn=== true){
		let added_card = getRandomCard(sum)
		currentCards.push(added_card)
		cardEl.textContent = "Cards: "
		for ( let i = 0; i < currentCards.length; i++ ) {
		cardEl.textContent += " " + currentCards[i]
		}
		sum += added_card
		if (sum > 21){
			check_As(currentCards)
			sum = 0
			for ( let i = 0; i < currentCards.length; i++ ) {
			sum += currentCards[i]
				}
			cardEl.textContent = "Cards: "
			for ( let i = 0; i < currentCards.length; i++ ) {
			cardEl.textContent += " " + currentCards[i]
				}
			}
		sumEl.textContent = "Sum: " + sum
		}
	renderGame()
}

function getRandomCard(givenSum) {
	let randomNumberraw = Math.random() * 13 + 1
	let randomNumber = Math.floor(randomNumberraw)
	if (randomNumber === 13 || randomNumber === 12 || randomNumber === 11) {
	return 10
}  else if (randomNumber === 1) {
	if ((givenSum + 11) < 22){
		return 11
	} else if ((givenSum + 11) > 21) {
		return 1
	}
} else {
		return randomNumber}

}
