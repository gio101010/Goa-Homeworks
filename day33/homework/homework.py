#დავალება1

ხილი=["ვაშლი","ბანანი", "ალუბალი","ფინიკი", "მაყვალი"]

print(ხილი)
print(ხილი[0],ხილი[-1])
ხილი.append("ლეღვი")
ხილი.remove("ბანანი")
ხილი[1] = "ლურნი კენკრა"
print(len(ხილი))

#დავალება2

რიცხვები = [10,20,30,40,50,60,70,80,90]

რიცხვები.append(100)
რიცხვები.insert(0,5)
რიცხვები.remove(30)
რიცხვები.reverse()
print(რიცხვები.index(50))
print(რიცხვები.count(20))

#დავალება3

რიცხვები = list(range(1,11))
პირველი_ნახევარი= რიცხვები[5:]
მეორე_ნახევარი=რიცხვები[5:]
კვადრატები = [n ** 2 for n in რიცხვები]
print(პირველი_ნახევარი)
print(მეორე_ნახევარი)
print(კვადრატები)
