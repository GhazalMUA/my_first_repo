package main

import (
	"fmt"
	"math"
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
	usepointer()
	fmt.Println("=================")
	arrayoperation()
	fmt.Println("=================")
	radikalprocess()
	fmt.Println("=================")
	instance := Moshakhasat{
		Ram:        8,
		Ssd:        100,
		Systemamel: "Windows",
		Screensize: 15.6,
		TouchID:    true,
	}
	result := instance.ScreenDouble()
	fmt.Println(result)
	resul := instance.Pishnahad()
	fmt.Println(resul)
	fmt.Println("=================")
	interfaca()
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
	fmt.Println("=================")
	//printing keys in seprate lines(indexes)
	for key := range mapdict {
		fmt.Println(key)
	}
	fmt.Println("=================")
	// printing key and value
	for key, value := range mapdict {
		fmt.Printf(" %s - %.2f\n", key, value)
	}
}

func pointer(n *int) {
	*n *= 2
}
func arrayoperation() {
	arrname := []int{11, 5, 4, 67, 40}
	doubleAt(arrname, 4)

	for _, value := range arrname {
		fmt.Printf("%d \n", value)
	}
	fmt.Println("=================")

}

func usepointer() {
	val := 10
	pointer(&val)
	fmt.Println(val)

}

func doubleAt(values []int, index int) {
	values[index] *= 2
}

func radikal(x float64) (float64, error) {
	if x < 0 {
		return 0.0, fmt.Errorf("nemishe manfi bezari (%f)", x)
	}
	return math.Sqrt(x), nil
}
func radikalprocess() {
	n, err := radikal(-5)
	if err != nil {
		fmt.Printf("error %s\n", err)

	} else {
		fmt.Println(n)
	}
}

// struct
type Moshakhasat struct {
	Ram        int
	Ssd        int
	Systemamel string
	Screensize float64
	TouchID    bool
}

func (moshakhasat *Moshakhasat) ScreenDouble() int {
	value := int(moshakhasat.Ram) * moshakhasat.Ssd
	if moshakhasat.TouchID {
		value = -value
	}
	return value
}
func (m *Moshakhasat) Pishnahad() int {
	meghdar := int(m.Ssd) * 2
	if m.Ssd < 200 {
		meghdar = -meghdar
	}
	return meghdar
}

type Square struct {
	Length float64
}
type Circle struct {
	Radius float64
}

func (s *Square) Area() float64 {
	areasquare := s.Length * s.Length
	return areasquare
}
func (c *Circle) Area() float64 {
	areacircle := math.Pi * c.Radius * c.Radius
	return areacircle
}

// interface mesle class mimone dakhele in class e inter az noe  interface, mikhaym ye method dashte bashe be esme area hala age bekhaym masalaan az circle estefade kone age area nadashte bashe azash estefade nmikone
type Inter interface {
	Area() float64
}

// SumAreas masahataro baham jam mikone ke ye shapes i ro migire ke az noe intere . total:=0.0 yani az ghabl sefre. tooye halghe hamontori kje midonim halghje faghat tooye araye toria mitone iterate bokone. vase hamin asan too function esh shapes ro be onvane vorodi be shekle araye tarif kardim ke khob albate noesh az type e  intere ke inter ham ye class jodagppnast  ke az noe interface e  harfesh ine ke age jai mikhay az type e inter estefade koni bayad hatman hameye parametr hat AREA dashte bashan
// arayehai ke be  shapes midi bayad hamashon az interface e Inter hemayat bokonan
// ke interface e Inter ye gharardade ke mige class ha harkodomeshon bayad Area dashte bashan
func SumAreas(shapes []Inter) float64 {
	total := 0.0
	for _, value := range shapes {
		total += value.Area()
	}
	return total
}

func interfaca() {
	s := &Square{4}
	fmt.Println(s.Area())
	c := &Circle{10}
	fmt.Println(c.Area())
	sc := SumAreas([]Inter{s, c})
	fmt.Println(sc)
}
