from Bag import first_Bag, linked_list_Bag
import time
from Student import Student

def main():

    # bag = first_Bag()
    bag = linked_list_Bag()

    startTime = time.time()
    #inserting the students
    with open("FakeNames.txt","r") as file: 
        for line in file:
            data = line.split()

            if not data:
                continue

            lName = data[0]
            fName = data[1]
            ssn = data[2]
            email = data[3]
            age = int(data[4])
            

            student = Student(fName, lName, email, age, ssn)

            #inserting and seeing if it worked
            didWork = bag.insert(student)
            if not didWork:
                print("error", fName,lName, time.time())
            

    print("Total students in bag: ",bag.getSize())
    print("Time to insert: ",time.time() - startTime, "seconds\n")

    #adding the total time and also finding the average student age
    startTime= time.time()
    total_age = 0
    
    for item in bag: 
        total_age += item.age

    avg_age_all = total_age / bag.getSize()
    print("Average age of all students: ,",avg_age_all)
    print("Time to calculate average age: ",time.time() - startTime ,"seconds\n")



    with open("DeleteNames.txt","r") as file:
        for line in file:
            ssn = line.strip()
            
            if not ssn:
                continue

            temp = Student(ssn=ssn)
            

            deleted = bag.delete(temp)
            if not deleted:
                print("error deleting", ssn)

            


    print("Students remaining in bag: ", bag.getSize())
    print("Time to delete: ", time.time() - startTime ,"seconds\n")

    startTime= time.time()
    retrieved_count = 0
    retrieved_total_age = 0

    with open("RetrieveNames.txt", "r") as file:
        for line in file:
            ssn = line.strip()
            if not ssn:
                continue
            
            temp = Student(ssn=ssn)
            retrieved_student = bag.retrieve(temp)

            if retrieved_student is None:
                print(f"Error retrieving SSN: {ssn}")
            else:
                retrieved_total_age += retrieved_student.age
                retrieved_count += 1

    avg_age_retrieved = retrieved_total_age / retrieved_count if retrieved_count > 0 else 0
    print("Average age of retrieved students: ",avg_age_retrieved)
    print("Time to retrieve: ",time.time() - startTime, "seconds")
    


            


if __name__ == "__main__":
    main()
