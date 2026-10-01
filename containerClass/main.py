from Bag import Bag
import time
from Student import Student

def main():

    bag = Bag()

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
            

    print(f"Total students in bag: {bag.size()}")
    print(f"Time to insert: {time.time() - startTime:.4f} seconds\n")

    #adding the total time and also finding the average student age
    startTime= time.time()
    total_age = 0
    
    for item in bag: 
        total_age += item.age

    avg_age_all = total_age / bag.size()
    print(f"Average age of all students: {avg_age_all:.4f}")
    print(f"Time to calculate average age: {time.time() - startTime:.4f} seconds\n")



    with open("DeleteNames.txt","r") as file:
        for line in file:
            ssn = line.strip()
            
            if not ssn:
                continue

            temp = Student(ssn=ssn)
            found_student = bag.retrieve(temp)
            tempssn = temp.getSsn()

            deleted = bag.delete(temp)
            if found_student and not deleted:
                print("error deleting", tempssn)

            


    print(f"Students remaining in bag: {bag.size()}")
    print(f"Time to delete: {time.time() - startTime:.4f} seconds\n")

    # ==========================================
    # 4. RETRIEVAL PHASE
    # ==========================================
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
    print(f"Average age of retrieved students: {avg_age_retrieved:.4f}")
    print(f"Time to retrieve: {time.time() - startTime:.4f} seconds")
    


            


if __name__ == "__main__":
    main()
