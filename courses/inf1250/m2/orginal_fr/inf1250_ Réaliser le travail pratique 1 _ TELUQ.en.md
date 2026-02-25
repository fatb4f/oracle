# Réaliser le travail pratique 1 (English Translation)



Source PDF: `inf1250_ Réaliser le travail pratique 1 _ TELUQ.pdf`



_Note: Automatically translated from French; minor wording differences may remain._



Module 2: Database Concepts, Relational Model and Database Management Systems

Carry out practical work 1
              Presentation
              This activity is devoted to completing practical work 1 which counts for 15% of the final mark.

You must write a short report (in “PDF” or “Word” format), which you will submit using the graded work submission tool. You don't
              You should not submit your work in a zip, tar, rar or other archive. Following the correction of the work noted, it is possible to send a
              comment using the same filing tool.

If the University has assigned you a due date for this work, this is a suggestion. There is no need to resubmit the work
              noted on a pre-determined date. However, if you wait too long before submitting assignments, you may have difficulty completing the course at
              time.

Your work
                    Answer the questions in the order in which they are presented, indicating the question number.
                    Submit your work using the graded work submission tool.

Question 1

The new MusiReseau networking site has contacted you to develop a database used to manage user information
              of the site who will share these musical tastes. We ask you to take the following information into account:

There is a list of songs available from where users can choose the ones they like. For each song available, MusiReseau
              wants to have the title, performer, composer, language, year of publication and genre. It is also important to have specific information
              to each artist (Performer or composer), their last name, first name, date of birth, place of birth and the year they started as an artist.

The company wants to keep track of all users of the site. This information concerns at least the user ID, name, gender and
              the email address. It is optional to also include age and a personal description.

Each user will therefore be able to select one or more songs which will be part of their musical catalog, also keeping the date
              for inclusion of the song in the catalog.

Finally, each user can have friends who will have access to their catalog. For each “Friendship”, MusiReseau wants to keep the
              users, start and end date.

Figure 1

Starting from the User and Friendship entities presented in Figure 1 and the description of the customer's needs:

Give the complete relational model adding entities as needed, include the list of attributes. Also give the primary key and keys
              foreign per entity (you can add attributes as needed to the defined entities).

Question 2

The following model describes a car rental system. Here are descriptions of the entities and relationships included in the model:

Person - Identified by idClient, a person is the one renting the car.

Car - Identified by idVoiture, this entity represents the car to be rented by the company.

Rental - Association between Car and Person which indicates a contract for the rental of a car by a customer between the dates determined therein.

Figure 2

Figure 3

Rental 1

CustomerIdCarId DateRental DateReturn Mileage

1 2340 05-06-2012 There is no content There is no
                                                                                                                                                   of content

2 2290 02/24/2012 02/26/2012 124

3 2398 02-24-2012 01-12-2012 1400

Location 2

CustomerIdCarId DateRental DateReturn Mileage

4 2340 04/25/2012 04/29/2012 293

6 2190 05-18-2012 05-26-2012 1456

3 2082 04-03-2012 12-03-2012 1400

Considering Figure 2 and the data in Figure 3, answer the following questions.

Propose a key for the Location relationship. Justify your answer.

Give the results of the following relational algebra operations:

UNION (Location1, Location2)
                    PROJECT (Location1, CustomerID, CarID, LocationDate)

Question 3

Considering Figure 2, give the expressions in algebraic language allowing you to answer the following questions:

Which customers rented a car after March 1, 2012? Expected result: Last name, first name and email address.
                    What cars have more than 100,000 kilometers or whose year is less than 2007? Expected result: idCar, Year and
                    Mileage.
                    List all rentals with descriptions of the corresponding cars. All rentals must appear even
                    if the information about the car is missing. Please only keep rentals made after 01-03-2012. Result
                    expected: carid, brand, model,
                    Customerid, LocationDate, ReturnDate.

Give the number of rentals per customer. Expected result: Customerid, last name, first name, numberRentals
