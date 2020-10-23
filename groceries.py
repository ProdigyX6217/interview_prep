# Variables holding the prices of the six items:
 
# Variables multiplied by 100 to make them into integers so there would be no approximation errors when added together.
 

pasta = 16.68 * 100  # penne 16 oz, pack of 12
sauce = 6.98 * 100  # Arrabiata sauce 24oz
garlic = 16.78 * 100  # 20 pack garlic clove
seasoning = 15.26 * 100  # Italian Seasoning
bread = 3.00 * 100  # Baguette twin pack
meatballs = 4.39 * 100  # 12 oz bag of meatballs

# subtotal is the sum of all prices before sales taxes or discounts are added
subtotal = (pasta + sauce + garlic + seasoning + bread + meatballs) / 100
print(subtotal)
 

# Rounded Solution
pasta = 16.68  
sauce = 6.98  
garlic = 16.78  
seasoning = 15.26  
bread = 3.00  
meatballs = 4.39
 
# round() was used to round the subtotal to 1 decimal place
subtotal = round((pasta + sauce + garlic + seasoning + bread + meatballs), 1)
print(subtotal)