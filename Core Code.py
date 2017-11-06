# top level choices: select grid type and input square footage
# requires 1 choice from list and one variable input
# x = coverage required in sqare feet


grid_choice = ['38-18', '50-35HD', '50-35HDR', '60-40', '65-45']

#Type the grid choice and square footage in here x = coverage in square feet)
grid_choice = '38-18'
x = 5600

if grid_choice =='38-18':
# code for 38 X 18 Core Path Grid
    print '38-18 Core Path Quote'
    a = round(x/9.8 + x*.05) #panels    
    b = a*18.68 #cost
    c = a*2.2 #weight
    print 'Square Feet:'
    print x
    print 'Number of panels (includes +five percent for guaranteed coverage):'
    print a
    print 'Weight (lbs):'
    print c
    print 'Cost: ($USD)'
    if x < 300:
        print b
        print 'order shipped out in small packs, fixed shipping rate'
    elif x in range (300, 1001):
        print b
    elif x in range (1000, 5001):
        print (b*.9)
        print '(ten percent discount applied)'
    elif x in range (5000, 10001):
        print (b * .85)
        print '(fifteen percent discount applied)'
    elif x in range (10000, 15001):
        print (b * .8)
        print '(twenty percent discount applied, contact for container shipment details)'
    elif x > 15000:
        print 'tbd'
        print '(proprietors discount; contact for pricing, container shipment details, and special rate)'
else:
# code for 50 X 35 HD Core Drive Grid #STILL NEED TO EDIT ALL VARIABLES BUT STRUCTURE WORKS :D
    if grid_choice == '50-35HD':
        print '50-35 Core Drive'
        a = round(x/9.8 + x*.05) #panels
        b = a*25.68 #cost
        c = a*5.2 #weight
        print 'Square Feet:'
        print x
        print 'Number of panels (includes +five percent for guaranteed coverage):'
        print a
        print 'Weight (lbs):'
        print c
        print 'Cost: ($USD)'
        if x < 300:
            print b
            print 'order shipped out in small packs, fixed shipping rate'
        elif x in range (300, 1001):
            print b
        elif x in range (1000, 5001):
            print (b*.9)
            print '(ten percent discount applied)'
        elif x in range (5000, 10001):
            print (b * .85)
            print '(fifteen percent discount applied)'
        elif x in range (10000, 15001):
            print (b * .8)
            print '(twenty percent discount applied, contact for container shipment details)'
        elif x > 15000:
            print 'tbd'
            print '(proprietors discount, contact for pricing, container shipment details, and special rate)'
    else:
# code for 50-35HDR Grid NEEDS UPDATED VARIABLES BUT CODE WORKS :D 
        if grid_choice == '50-35HDR':
            print'50-35HDR Core Drive Quote'
            a = round(x/9.8 + x*.05) #panels
            b = a*25.68 #cost
            c = a*5.5 #weight
            print 'Square Feet:'
            print x
            print 'Number of panels (includes +five percent for guaranteed coverage):'
            print a
            print 'Weight (lbs):'
            print c
            print 'Cost: ($USD)'
            if x < 300:
                print b
                print 'order shipped out in small packs, fixed shipping rate'
            elif x in range (300, 1001):
                print b
            elif x in range (1000, 5001):
                print (b*.9)
                print '(ten percent discount applied)'
            elif x in range (5000, 10001):
                print (b * .85)
                print '(fifteen percent discount applied)'
            elif x in range (10000, 15001):
                print (b * .8)
                print '(twenty percent discount applied, contact for container shipment details)'
            elif x > 15000:
                print 'tbd'
                print '(proprietors discount, contact for pricing, container shipment details, and special rate)'
        else:
# code for 60-40 Grid NEEDS UPDATED VARIABLES BUT CODE WORKS :D 
            if grid_choice == '60-40':
                print'60-40 Core Drive Quote'
                a = round(x/9.8 + x*.05) #panels
                b = a*25.68 #cost
                print 'Square Feet:'
                print x
                print 'Number of panels (includes +five percent for guaranteed coverage):'
                print a
                print 'Weight (lbs):'
                print c
                print 'Cost: ($USD)'
                if x < 300:
                    print b
                    print 'order shipped out in small packs, fixed shipping rate'
                elif x in range (300, 1001):
                    print b
                elif x in range (1000, 5001):
                    print (b*.9)
                    print 'ten percent discount applied'
                elif x in range (5000, 10001):
                    print (b * .85)
                    print 'fifteen percent discount applied'
                elif x in range (10000, 15001):
                    print (b * .8)
                    print 'twenty percent discount applied, contact for container shipment details'
            else:
# code for 65-45 Grid NEEDS UPDATED VARIABLES BUT CODE WORKS :D 
                if grid_choice == '65-45':
                    print'65-45 Heavy Duty Core Drive Quote'
                    a = round(x/9.8 + x*.05) #panels
                    b = a*25.68 #cost
                    c = a*12
                    print 'Square Feet:'
                    print x
                    print 'Number of panels (includes +five percent for guaranteed coverage):'
                    print a
                    print 'Weight (lbs):'
                    print c
                    print 'Cost: ($USD)'
                    if x < 300:
                        print b
                        print 'order shipped out in small packs, fixed shipping rate'
                    elif x in range (300, 1001):
                        print b
                    elif x in range (1000, 5001):
                        print (b*.9)
                        print 'ten percent discount applied'
                    elif x in range (5000, 10001):
                        print (b * .85)
                        print 'fifteen percent discount applied'
                    elif x in range (10000, 15001):
                        print (b * .8)
                        print 'twenty percent discount applied, contact for container shipment details'  
                else:
                     print grid_choice, ' - incorrect variable entered for "grid choice", please check input and try again!'

print ' '
print 'Thank you for choosing Core Landscape Products :)'

#fini!
