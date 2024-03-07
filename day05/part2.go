package main

import (
	aoc "aoc/utils"
	"fmt"
	"log"
	"math"
	"os"
	"regexp"
	"strings"
)

func readFile(filepath string) string {
	data, err := os.ReadFile(filepath)
	if err != nil {
		log.Fatal(err)
	}
	content := string(data)
	return content
}

type Interval struct {
	sourceStart      int
	destinationStart int
	length           int
}

func (i Interval) contains(n int) bool {
	if i.sourceStart <= n && n < i.sourceStart+i.length {
		return true
	}
	return false
}

func (i Interval) convert(value int) int {
	return i.destinationStart + int(math.Abs(float64(i.sourceStart)-float64(value)))
}

func getSeeds(seedsRaw []int) []int {
	var seeds []int
	for i := 0; i < len(seedsRaw); i += 2 {
		for s := seedsRaw[i]; s < seedsRaw[i]+seedsRaw[i+1]; s++ {
			seeds = append(seeds, s)
		}
	}
	return seeds
}

func getLayers(sections []string) [][]Interval {
	re := regexp.MustCompile(`\d+ \d+ \d+`)
	var layers [][]Interval
	for i, section := range sections[1:] {
		layers = append(layers, []Interval{})
		matches := re.FindAllString(section, -1)

		for _, match := range matches {
			nums := aoc.ArrStrToInt(strings.Split(match, " "))
			layers[i] = append(layers[i], Interval{sourceStart: nums[1], destinationStart: nums[0], length: nums[2]})
		}
	}
	return layers
}

func main() {
	input := readFile("./input.txt")

	sections := strings.Split(input, "\n\n")

	re := regexp.MustCompile(`\d+`)
	seedsRaw := aoc.ArrStrToInt(re.FindAllString(sections[0], -1))
	seeds := getSeeds(seedsRaw)

	layers := getLayers(sections)

	for _, layer := range layers {
		for i, seed := range seeds {
			for _, interval := range layer {
				if interval.contains(seed) {
					seeds[i] = interval.convert(seed)
					break
				}
			}
		}
	}

	fmt.Println(aoc.ArrMin(seeds))
}
