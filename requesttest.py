import requests
import sys
import re
import numpy as np

f = open('PPlus.csv', 'w+')
f.write('Fat,Carbs,Protein,Fiber,PPlus\n')

fat = 0
carbs = 0
protein = 0
fiber = 0

stepsize = 4

for i in xrange(5):
	carbs = 0
	fiber = 0
	protein = 0
	fat = fat + stepsize
	for j in xrange(5):
		fiber = 0
		protein = 0
		carbs = carbs + stepsize
		for k in xrange(5):
			protein = 0
			fiber = fiber + stepsize
			for l in xrange(5):
				protein = protein + stepsize
				xml = '<FoodItemEntry type="FoodItemEntry"><FoodItem type="Food"><DefaultPortion type="Portion"><DefaultQuantity>1</DefaultQuantity><Energy>0</Energy><Fiber>2</Fiber><MonoUnsaturatedLipid>'+str(fat)+'</MonoUnsaturatedLipid><PolyUnsaturatedLipid>'+str(fat)+'</PolyUnsaturatedLipid><SaturatedLipid>'+str(fat)+'</SaturatedLipid><TotalLipid>3</TotalLipid><TransLipid>'+str(fat)+'</TransLipid><SugarAlcohol>0</SugarAlcohol><Protein>'+str(protein)+'</Protein><TotalCarb>'+str(carbs)+'</TotalCarb><Weight>0</Weight></DefaultPortion></FoodItem><ServingCount>1</ServingCount><ServingSize type="Portion"><DefaultQuantity>1</DefaultQuantity><Energy>0</Energy><Fiber>'+str(fiber)+'</Fiber><MonoUnsaturatedLipid>'+str(fat)+'</MonoUnsaturatedLipid><PolyUnsaturatedLipid>'+str(fat)+'</PolyUnsaturatedLipid><SaturatedLipid>'+str(fat)+'</SaturatedLipid><TotalLipid>'+str(fat)+'</TotalLipid><TransLipid>'+str(fat)+'</TransLipid><SugarAlcohol>0</SugarAlcohol><Protein>'+str(protein)+'</Protein><TotalCarb>'+str(carbs)+'</TotalCarb><Weight>0</Weight></ServingSize></FoodItemEntry>'

				payload={'method':'CalculateFoodPoints','xml':xml}
				r = requests.post('http://www.weightwatchers.com/httpservices/PointsAccounting/PointsCalculatorService.aspx',data=payload)
				m = re.search('(<Value>)(.*)(</Value>)',r.text)
				print ('fat:'+str(fat)+' carbs:'+str(carbs)+' fiber:'+str(fiber)+' protein:'+str(protein)+' pts:'+m.group(2)+'\n')
	
				f.write(str(fat)+','+str(carbs)+','+str(protein)+','+str(fiber)+','+m.group(2)+'\n')
	
f.close()