package main

import (
	"fmt"
	"mymodule/data"
)

func main() {

	halghe()
	fmt.Println("=================")
	data.SayHello()
	fmt.Println("=================")
	book()
	fmt.Println("=================")
	slice()
	fmt.Println("=================")
	objectmap()
	fmt.Println("=================")
}

func halghe() {
	for i := 1; i < 5; i++ {
		fmt.Println("salam")
	}
}

func book() {
	book := "sokoote bareha"
	fmt.Println(book)
}

func slice() {
	slice := []string{"ghazal", "hafezi", "birgani", "25", "mehrshahr", "female"}

	fmt.Printf("etelaate shakhs %v", slice)
	fmt.Println("=================")
	// PRINT THE ITEMS
	for i := 0; i < len(slice); i++ {
		fmt.Println(slice[i])
	}
	fmt.Println("=================")
	// PRINT THE INDEXES only
	for index := range slice {
		fmt.Println(index)

	}
	fmt.Println("=================")
	// PRINT THE INDEX and value together
	for index, value := range slice {
		fmt.Printf("%d - %v \n", index, value)
	}
	fmt.Println("=================")
	//append(ezafekardan) ye item be slice ya araye
	slice = append(slice, "developer")
	for key, value := range slice {
		fmt.Println(key, value)
	}

}
func objectmap() {
	mapdict := map[string]float64{
		"medad":    12000,
		"khodkar":  15000,
		"kaghazA4": 3000,
		"tarash":   20000,
		"jamedadi": 50000,
	}
	//age behesh key bedi, vasat value chap mikone
	fmt.Println(mapdict["khodkar"])
	fmt.Println("=================")
	//age ye item vojod nadashte bashe 0 barmigardone
	fmt.Println(mapdict["pakkon"])
	fmt.Println("=================")
	value, checking := mapdict["pakkon"]
	if !checking {
		fmt.Println("PAKKON TOOYE LIST NIST")
	} else {
		fmt.Println(value)
	}
	fmt.Println("=================")
	//append new item to the map
	mapdict["pakkon"] = 4000
	mapdict["ghalatgir"] = 10000
	fmt.Println(mapdict)
	fmt.Println("=================")
	//delete an item
	delete(mapdict, "ghalatgir")
	fmt.Println(mapdict)
}
