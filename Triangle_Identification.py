criteria = input("Enter the category based on which you want to identify the triangle(angle or side or both): ")
category = criteria.lower()
side=[]
valid_side=0
angle=[]
valid_angle=0
both_side=[]
valid_both_side=0
both_angle=[]
valid_both_angle=0

#Identifying on the basis of sides
if category=="side":

    #Taking value from the user until 3 valid entries are done
   while valid_side<3:
       sides=input("Enter the side of the triangle: ")

       #Verifying whether the entered value is number or not
       if sides.isdigit():
           valid_side+=1
           side.append(sides)
       else:
           print(f"{sides} is not a valid integer!!!")
           continue

   #Condition for identification of triangle
   if side[0] != side[1] != side[2] != side[0]:
       print("Scalene Triangle")
   elif side[0] == side[1] != side[2] or side[1] == side[2] != side[0] or side[2] == side[0] != side[1]:
       print("Isosceles Triangle")
   elif side[0] == side[1] == side[2]:
       print("Equilateral Triangle")
   else:
       print("Unknown Error Occurred")

#Identifying on the basis of angles
elif category=="angle":

    # Taking value from the user until 3 valid entries are done
    while valid_angle<3:
        angles=input("Enter the angle of the triangle: ")

        # Verifying whether the entered value is number or not
        if angles.isdigit():
            valid_angle+=1
            angle.append(angles)

            #Condition for checking that the sum of interior angles of a triangle can't exceed 180 degree
            if valid_angle>2:
                if int(angle[0])+int(angle[1])+int(angle[2])==180:

                    #Condition for identification of triangle
                    if int(angle[0])<90 and int(angle[1])<90 and int(angle[1])<90:
                        print("Acute Angled Triangle")
                    elif int(angle[0])==90 or int(angle[1])==90 or int(angle[1])==90:
                        print("Right Angled Triangle")
                    elif int(angle[0])>90 or int(angle[1])>90 or int(angle[1])>90:
                        print("Obtuse Angled Triangle")
                    else:
                        print("Unknown Error Occurred!!!")

                #When sum of interior angles of triangle is less than 180 degree
                elif int(angle[0])+int(angle[1])+int(angle[2])<180:
                    print("Sum of the interior angles of a triangle cannot be less than 180 degree!!!")
                    valid_angle=0
                    angle=[]
                    continue

                #When sum of interior angles of triangle is greater than 180 degree
                elif int(angle[0])+int(angle[1])+int(angle[2])>180:
                    print("Sum of the interior angles of a triangle cannot be greater than 180 degree!!!")
                    valid_angle = 0
                    angle = []
                    continue
        else:
            print(f"{angles} is not a valid integer!!!")
            continue

#Identifying on the basis of both sides and angles
elif category=="both":

    # Taking value from the user until 3 valid entries are done
    while valid_both_side<3:
        valid_both_sides=input("Enter the sides of the triangle: ")

        # Verifying whether the entered value is number or not
        if valid_both_sides.isdigit():
            valid_both_side+=1
            both_side.append(valid_both_sides)
        else:
            print(f"{valid_both_sides} is not a valid integer!!!")
            continue

    # Taking value from the user until 3 valid entries are done
    while valid_both_angle<3:
        valid_both_angles=input("Enter the angle of the triangle: ")

        # Verifying whether the entered value is number or not
        if valid_both_angles.isdigit():
            valid_both_angle+=1
            both_angle.append(valid_both_angles)

            # Condition for checking that the sum of interior angles of a triangle can't exceed 180 degree
            if valid_both_angle>2:
                if int(both_angle[0]) + int(both_angle[1]) + int(both_angle[2]) == 180:

                    # Condition for identification of triangle
                    #Condition 1
                    if int(both_angle[0]) < 90 and int(both_angle[1]) < 90 and int(both_angle[1]) < 90:
                        if both_side[0] != both_side[1] != both_side[2] != both_side[0]:
                            print("Scalene And Acute Angled Triangle")
                        elif both_side[0] == both_side[1] != both_side[2] or both_side[1] == both_side[2] != both_side[
                            0] or both_side[2] == both_side[0] != both_side[1]:
                            print("Isosceles and Acute Angled Triangle")
                        elif both_side[0] == both_side[1] == both_side[2]:
                            print("Equilateral and Acute Angled Triangle")
                        else:
                            print("Unknown Error Occurred")

                    #Condition 2
                    elif int(both_angle[0]) == 90 or int(both_angle[1]) == 90 or int(both_angle[1]) == 90:
                        if both_side[0] != both_side[1] != both_side[2] != both_side[0]:
                            print("Scalene And Right Angled Triangle")
                        elif both_side[0] == both_side[1] != both_side[2] or both_side[1] == both_side[2] != both_side[
                            0] or both_side[2] == both_side[0] != both_side[1]:
                            print("Isosceles And Right Angled Triangle")
                        elif both_side[0] == both_side[1] == both_side[2]:
                            print("Equilateral And Right Angled Triangle")
                        else:
                            print("Unknown Error Occurred")

                    #Condition 3
                    elif int(both_angle[0]) > 90 or int(both_angle[1]) > 90 or int(both_angle[1]) > 90:
                        if both_side[0] != both_side[1] != both_side[2] != both_side[0]:
                            print("Scalene And Obtuse Angled Triangle")
                        elif both_side[0] == both_side[1] != both_side[2] or both_side[1] == both_side[2] != both_side[
                            0] or both_side[2] == both_side[0] != both_side[1]:
                            print("Isosceles And Obtuse Angled Triangle")
                        elif both_side[0] == both_side[1] == both_side[2]:
                            print("Equilateral And Obtuse Angled Triangle")
                        else:
                            print("Unknown Error Occurred")
                    else:
                        print("Unknown Error Occurred!!!")

                # When sum of interior angles of triangle is less than 180 degree
                elif int(both_angle[0]) + int(both_angle[1]) + int(both_angle[2]) < 180:
                    print("Sum of the interior angles of a triangle cannot be less than 180 degree!!!")
                    valid_both_angle = 0
                    both_angle = []
                    continue

                # When sum of interior angles of triangle is greater than 180 degree
                elif int(both_angle[0]) + int(both_angle[1]) + int(both_angle[2]) > 180:
                    print("Sum of the interior angles of a triangle cannot be greater than 180 degree!!!")
                    valid_both_angle = 0
                    both_angle = []
                    continue
        else:
            print(f"{valid_both_angles} is not a valid integer!!!")
            continue

else:
    print("Choose between angle,side or both only!!!")