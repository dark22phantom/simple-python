class Bmi:
    data = []

    def addPerson(self):
        print("HPB BMI Solution")
        print("=======================")
        
        while True:
            email = input("Email: ")
            if(email.isdigit() == 1):
                print("Email must be string!")
                continue
            else:
                if(email.find("@") > 0 and email.find(".") > 0):
                    break
                else:
                    continue

        while True:
            name = input("Name: ")
            if(name.replace(" ","").isalpha() == 0):
                print("Name must be string!")
                continue
            else:
                break

        while True:
            bmi = input("BMI: ")
            try:
                if(float(bmi) > 0):
                    break
                else:
                    continue
            except ValueError:
                print("BMI must be int/double!")
                continue
        
        self.data.append({
            "email": email,
            "name": name,
            "bmi": bmi
        })

        print("No of people track : ", len(self.data))
        print("=======================")

        return True

    def deletePerson(self):
        print("HPB BMI Solution")
        print("=======================")

        while True:
            email = input("Email to delete : ")
            if(email.isdigit() == 1):
                print("Email must be string!")
                continue
            else:
                if(email.find("@") > 0 and email.find(".") > 0):
                    break
                else:
                    continue

        index = next((i for i, item in enumerate(self.data) if item["email"] == email), None)
        if(index == None):
            print("Email is Not Found!")
        else:
            self.data.pop(index)
            print("Email found. Remaining People : ", len(self.data))

        print("=======================")
        return True

    def listPerson(self):
        print("HPB BMI Solution")
        print("=======================")

        while True:
            bmi = input("Display BMI higher or equal to : ")
            try:
                if(float(bmi) > 0):
                    break
                else:
                    continue
            except ValueError:
                print("BMI must be int/double!")
                continue

        result = [i for i in self.data if float(i["bmi"]) >= float(bmi)]

        print("{0:<30} {1:<30} {2:<30}".format("Email", "Name", "BMI"))
        
        print("====================================================================")
        if (len(result) == 0):
            print("Data is not found")
        else:
            for x in result:
                print("{0:<30} {1:<30} {2:<30}".format(x['email'], x['name'], x['bmi']))
        
        print("Records found : ", len(result))
        print("====================================================================")
        return True

obj = Bmi()

while True:
    print("HPB BMI Solution")
    print("=======================")
    print("1. Add a person's BMI")
    print("2. Delete a person's BMI")
    print("3. List BMI")
    print("4. Exit")
    choice = input("Choice: ")
    if choice.isdigit() and int(choice) == 1:
        if(obj.addPerson()):
            continue
    elif choice.isdigit() and int(choice) == 2:
        if(obj.deletePerson()):
            continue
    elif choice.isdigit() and int(choice) == 3:
        if(obj.listPerson()):
            continue
    elif choice.isdigit() and int(choice) == 4:
        break
    else:
        print("You must choose between 1-4")
        continue
