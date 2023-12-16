package main

import (
	"slices"
)

func twoSum(a []int, target int) []int {
	m := map[int]bool{}
	for i := 0; i < len(a); i++ {
		if m[a[i]] {
			return []int{a[i], target - a[i]}
		} else {
		m[target-a[i]] = true
	}
	}
	return []int{1, 1}
}

func twoSumTwo(a []int, target int) []int {
	slices.Sort(a)
	lo := 0
	hi := len(a) - 1
	for lo < hi {
		lowNum := a[lo]
		hiNum := a[hi]
		test := lowNum + hiNum
		if test == target {
			return []int{lowNum, hiNum}
		} else if test < target {
			lo++
		} else {
			hi--
		}
	}
	return []int{0, 0}
}

func main() {
	
}