package main

import (
	aoc "aoc/utils"
	"fmt"
	"log"
	"math"
	"strconv"
	"strings"
)

type scratchcard struct {
	number         int
	winningNumbers []int
	numbers        []int
}

func getPoints(card scratchcard) int {
	// fmt.Println(card)
	var wins int
	for _, number := range card.numbers {
		for _, winningNumber := range card.winningNumbers {
			if number == winningNumber {
				wins += 1
			}
		}
	}
	// fmt.Println("wins: ", wins)
	return int(math.Exp2(float64(wins - 1)))
}

func main() {
	lines, err := aoc.ReadLines("./input.txt")
	if err != nil {
		log.Fatal(err)
	}

	// fmt.Println(lines)

	var scratchcards []scratchcard
	for i, line := range lines {
		card := scratchcard{number: i + 1}

		s := strings.Split(line, ": ")[1]
		bothNumers := strings.Split(s, " | ")

		for _, number_s := range strings.Split(bothNumers[0], " ") {
			if number_s == "" {
				continue
			}
			number, err := strconv.Atoi(number_s)
			if err != nil {
				log.Fatal(err)
			}
			card.winningNumbers = append(card.winningNumbers, number)
		}

		for _, number_s := range strings.Split(bothNumers[1], " ") {
			if number_s == "" {
				continue
			}
			number, err := strconv.Atoi(number_s)
			if err != nil {
				log.Fatal(err)
			}
			card.numbers = append(card.numbers, number)
		}

		scratchcards = append(scratchcards, card)
	}

	// fmt.Println(scratchcards)

	var pointsSum int
	for _, card := range scratchcards {
		points := getPoints(card)
		// fmt.Println(points)
		pointsSum += points
	}
	fmt.Println(pointsSum)
}
