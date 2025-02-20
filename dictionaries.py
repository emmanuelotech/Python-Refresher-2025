#Dictionaries are python data types and do not allow duplicates.
#values are stored in form of key/Value pairs.

def Persons_dict():
        Persons = {
                "Name": "Emmanuel Okello",
                "Department": "Data & Analytics",
                "Division" : "Internal Audit"}

        print(Persons["Name"]);
        print(Persons["Division"]);
        print(Persons["Department"]);
        Persons["Home"]="Kole District";
        print(Persons["Home"]);
        Persons["Mother"] = "Harriet Anying";
        del Persons["Mother"]
        print(Persons);
        Persons["Status"]="Awake";
        Persons["Now"] = "Writing Codes right now....";
        Persons["Now"] = "...Writing code ..2 again..";

        for each in Persons:
                print(each,":", Persons[each])

Persons_dict();