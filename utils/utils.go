package utils

import (
	"bufio"
	"log"
	"os"
	"strconv"
)

func ReadLines(filepath string) ([]string, error) {
	file, err := os.Open(filepath)
	defer file.Close()
	if err != nil {
		log.Fatal(err)
	}
	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	return lines, scanner.Err()
}

func ArrMin(arr []int) int {
	min := arr[0]
	for _, val := range arr[1:] {
		if val < min {
			min = val
		}
	}
	return min
}

func ArrStrToInt(arrStr []string) []int {
	var arrInt []int
	for _, str := range arrStr {
		num, err := strconv.Atoi(str)
		if err != nil {
			log.Fatal(err)
		}
		arrInt = append(arrInt, num)
	}
	return arrInt
}
