import csv
import pandas as pd
from csv import writer, reader
# csv_rowlist = [["SN", "Movie", "Protagonist"], [1, "Lord of the Rings", "Frodo Baggins"],
#                [2, "Harry Potter", "Harry Potter"]]
# with open('protagonist.csv', 'w') as file:
#     writer = csv.writer(file)
#     writer.writerows(csv_rowlist)




# with open("people.csv", 'r') as file:
#     csv_file = csv.DictReader(file)
#     for row in csv_file:
#         print(dict(row))

# import csv

# with open('players.csv', 'w', newline='') as file:
#     fieldnames = ['player_name', 'fide_rating']
#     writer = csv.DictWriter(file, fieldnames=fieldnames)

#     writer.writeheader()
#     writer.writerow({'player_name': 'Magnus Carlsen', 'fide_rating': 2870})
#     writer.writerow({'player_name': 'Fabiano Caruana', 'fide_rating': 2822})
#     writer.writerow({'player_name': 'Ding Liren', 'fide_rating': 2801})



# # creating a data frame
# df = pd.DataFrame([['Jack', 24], ['Rose', 22]], columns = ['Name', 'Age'])

# # writing data frame to a CSV file
# df.to_csv('person.csv')


# fields = ['Name', 'Branch', 'Year', 'CGPA']
 
# # data rows of csv file
# rows = [ ['Nikhil', 'COE', '2', '9.0'],
#         ['Sanchit', 'COE', '2', '9.1'],
#         ['Aditya', 'IT', '2', '9.3'],
#         ['Sagar', 'SE', '1', '9.5'],
#         ['Prateek', 'MCE', '3', '7.8'],
#         ['Sahil', 'EP', '2', '9.1']]
 
# # name of csv file
# filename = "university_records.csv"
 
# # writing to csv file
# with open(filename, 'w') as csvfile:
#     # creating a csv writer object
#     csvwriter = csv.writer(csvfile)
     
#     # writing the fields
#     csvwriter.writerow(fields)
     
#     # writing the data rows
#     csvwriter.writerows(rows)

with open('./users.csv', 'r') as file:

    # csv_writer = writer(file, lineterminator='\n')
    # header = ('awale','akhire','umure')
    # data = (('jeneng awal','BRRRRR','40'),
    # ('jeneng awal','BRRRRR','40'),
    # ('jeneng awal','BRRRRR','40'))

    # csv_writer.writerow(header)
    # for row in data:
    #     csv_writer.writerow(row)

#    print(file.read())


   login = False
   isian =""
answer = input("Do you have an account?(yes or no) ")

if answer == 'yes' :
   with open('users.csv', 'r') as csvfile:
      csv_reader = csv.reader(csvfile)
      username = input("Player One Username: ")
      password = input("Player One Password: ")

      for row in csv_reader:
         print(row[0], row[1],row[2])
         print("iki isi sekan row awal",row[0])
         isian = row[0]
         print("isian e broooo",isian)
        
         if row[1]== username and row[2] == password:

            login = True
            break
         else:
            login = False
            break

   if login == True:
      print("You are now logged in!")
   else:
      print("Incorrect. Game Over.")
      exit()    
else:
   print('Only Valid Usernames can play. Game Over.')
   exit()