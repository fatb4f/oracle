# Vérifier et pratiquer (English Translation)



Source PDF: `inf1250_ Vérifier et pratiquer _ TELUQ.pdf`



_Note: Automatically translated from French; minor wording differences may remain._



Module 2: Database Concepts, Relational Model and Database Management Systems

Check and practice
              Presentation
              In this activity, we offer you a series of questions. The questionnaire will allow you to consolidate your knowledge and
              return, if necessary, to certain passages of the reference text that you studied during the previous activity.

Step by step…
              1. Mathematical warming

Database theory is based on mathematics. Do the following problems to get in shape. Don't you
                    Don't worry if you can't do all the problems, it's just a simple warm up. If you cannot resolve some
                    problems, do your research to refresh your memory. Appendix 25 of the Hainaut book is also available for consultation.

Question 1: We say that a relation forms a partial equivalence class if a ∼ b then b ∼ a (symmetry) for all a, b and a ∼ b
                    and b ∼ c implies a ∼ c (transitivity) for all a, b, c. Prove that if x ∼ x is false for some x, then x ∼ b is false for all b.

Answer: a

Suppose x ∼ b is true. Then by symmetry, b ∼ x. So we have x ∼ b and b ∼ x. By transitivity, we therefore have x ∼ x,
                    a contradiction.

Question 2: Using only the union and difference, calculate the intersection between A and B.

Answer :

We have that A ∪ B = (A ∪ B) − (A − B) − (B − A)

Question 3: If we write A ∼ B for two sets A and B if and only if A ∩ B is not empty, is that the relation ∼ is
                    transitive?

Answer :

No. Consider A = {1, 2}, B = {2, 3}, C = {3, 4}. We have that A ∼ B, B ∼ C, but not A ∼ C

Question 4: If the letter A can be red or black while the letter B must be blue, does the color depend on the letter? Does the
                    letter is based on color?

Answer :

No, the color does not depend on the letter because for the same letter, more than one color is possible. On the other hand, the letter is a function
                    of color.

Question 5: Consider a continuous function f (x). If there exists an inverse function g such that f (g(x)) = g(f (x)) = x what can you say a
                    subject of f?

Answer :

2
                    The function f is strictly monotonic (increasing or decreasing). For example, f(x) = 2x has this property but f(x) = x does not.

n−1
                                                                                     n
                    Question 6: Suppose there exists ∑k=1 ( ) distinct non-empty sets A
                                                                                                                                ′
                                                                                                                                    such that A is strictly contained in A. What is the
                                                                                     k

n
                    cardinality of A? (By convention, the expression ( ) represents the binomial coefficient
                                                                                              k
                    (https://fr.wikipedia.org/wiki/Coefficient_binomial).)

Answer :

n
                    The quantity ( ) represents the number of distinct subsets of cardinality k coming from a set of cardinality n. By
                                    k
                    inspection, so the answer is n.

Question 7: Let there be two propositions A and B. We have that A ∨ B is true if A or B is true. We have that A ∧ B is true if A
                    and B are true. We have that ¬A is true if A is false. If A ∨ B is true, what can you also say about (¬A) ∧ (¬B)?

Answer :

According to De Morgan's law (https://fr.wikipedia.org/wiki/Lois_de_De_Morgan), we have that (¬A) ∧ (¬B) = ¬(A ∨ B). In
                    Consequently, we have that (¬A) ∧ (¬B) must be false.
                                                                                 i
                                                                 3 2
                    Question 8: What is log2 (∏i=1 = 1)? (Without calculator or computer.)

Answer:
                                                                 i
                                                 3 2 3 i 3
                    We have that log2 (∏i=1 = 1) = ∑
                                                                             i=1
                                                                                         log2(2) = ∑
                                                                                                             i=1
                                                                                                                   i = 1 + 2 + 3 = 6.

3 1
                    Question 9: What is ∑? (Without calculator or computer.)
                                                       k=1k

Answer :

3 1 1 1 11
                    We have that ∑ = 1 + + = .
                                           k=1 k 2 3 6

Reminder: If you cannot complete these self-assessment questions, you should not continue in this course.

2. Access the Relational Model Questionnaire

Question 1: What is the difference between the concepts of domain and attribute for a relationship?

Answer :

A domain is a set of values ​​characterized by a name. For example, the domain “University work” whose values would be
                    “Essay”, “Abstract”, “State of the art”, “Research report”, “Master’s thesis”, “Doctoral thesis”, etc. or the domain
                    “University study programs” whose values would be “Baccalaureate”, “Certificate”, “Short program”, “Master’s degree with
                    dissertation”, “PhD”, etc.

A relation is a subset of the Cartesian product of two domains. It is a subset, because certain vectors resulting from
                    Cartesian product are not valid in relation to the real world and the intended relationship. With the fields “University work” and
                    “University study programs”, the vector (“Doctoral thesis”, “Baccalaureate”) result of the Cartesian product of the two domains
                    does not make sense for the relationship “Academic work in study programs”. The attribute is the name given to a column of a
                    relationship; the column does not necessarily contain all the values ​​of a domain.

Explanation

The definitions of the domain and attribute concepts are presented and exemplified in section 2 of text 2.2 “Relational model and
                    standardization”, starting on page 72.

Question 2: What is an integrity constraint?

1. An assertion that the data contained in a database must be verified.
                    2. An assertion that must be verified by the data contained in a database and which is inherent to the data model.
                    3. An assertion that must be verified by the data contained in a database and which corresponds to a behavior rule specific to the
                       particular diagram of an application.

Answer: a

Explanation

This concept is defined at the beginning of page 59.

Question 3: What is the role of an identifier (also called a key) in a relationship?

1. The relationship identifier is a unique identifier to designate the relationship among a set of relationships.
                    2. The identifier of a relationship makes it possible to uniquely identify each of the n-tuples (or tuples) of the relationship.
                    3. The key of a relationship is the name given to the first attribute of the relationship (first column of the relationship).

Answer: b

Explanation

The concept of identifier (or key) is defined in section 4 of text 2.1 “Database concepts”, on page 52, and in section 3 d
                    text 2.3 “Relational models and normalization”, page 76.

Hainaut uses the term tuples, which is similar to the concept of tuples (anglicism used in computer science).

For more information: https://fr.wikipedia.org/wiki/Uplet (https://fr.wikipedia.org/wiki/Uplet)

Question 4: Among the identifiers of a table, what is the most representative identifier called?

1. Primary identifier
                    2. Primitive identifier
                    3. Primary identifier

Answer: c

Explanation

See page 52. In standard terminology, the primary identifier is called the primary key.

Question 5: What does the uniqueness constraint allow?

Answer: The uniqueness constraint ensures that the identifier (the key) has distinct values. This constraint is guaranteed
                    by the DBMS which will automatically reject any attempt to insert a row whose identifier is already present in the table.

Explanation

See page 53.

Question 6: What is the role of a foreign key?

1. A foreign key allows you to optionally specify a relation key that is not the primary key.
                    2. A foreign key expresses a domain constraint on a particular relationship.
                    3. A foreign key allows you to relate rows in separate tables.

Answer: c

Explanation

The concept of a foreign key is defined in section 5 of text 2.1 “Database Concepts” on page 53.

Question 7: What is the name given to the constraint that applies to the foreign key?

Answer: referential constraint

Explanation

For a foreign key to play its reference role, it is necessary that the set of values of a foreign key be a sub-
                    set of values of the target identifier, at any time. The referential constraint makes it possible to ensure this. But for this it is necessary
                    explicitly declare foreign keys.

Refer to page 54 and page 59.
                    Question 8: What definition applies to an inclusion constraint?

1. An inclusion constraint specifies that the values of an attribute in a relationship must simultaneously be values of an attribute
                       from another relationship.
                    2. An inclusion constraint specifies that the values of an attribute in one relationship must not be values of an attribute in another
                       relationship.

Answer: a

Explanation: refer to the definition given on page 82

Question 9: A user or a program can interact with a database via calls to the DBMS. What are their names?
                    these calls?

1. Servers
                    2. Customers
                    3. Requests

Answer: c

Explanation: These are queries (page 184).

Question 10: In the execution of these calls, the DBMS guarantees absolute quality of service; this guarantee has four properties
                    What are they?

1. atomicity, consistency, isolation and durability (ACID)
                    2. Atomicity, Transferability, Isolation and Durability (ATID)
                    3. Atomicity, Consistency, Isolation and Volatility (ACIV)

Answer: a

Explanation: (page 185)

The atomicity of a query refers to the complete execution of a query or, conversely, its non-execution in the event of a failure. This
                    property ensures data integrity in the event of an incident.

Consistency ensures compliance with all integrity constraints imposed on the data.

Isolation allows each query to be performed without worrying about concurrent operations processing the same data.

Durability ensures that updates made to databases are permanent.

A transaction will then be defined as a sequence of operations constituting a logical sequence of processing and for which the
                    ACID guarantees are required.

Note

The explanations offered in the questionnaire solutions refer to sections of Gardarin's book. The questionnaire put to
                    update is proposed at the end of the module 2 update.

Answer the questions and carefully analyze your answers by asking yourself: “What are the arguments that make this
                    Could this answer be correct? » and “What are the reasons why this answer could be a bad answer?” »

Check your answer by clicking on the Solution button. For each question, the answer and an explanation are provided.
              3. Access the SGDB Architecture Questionnaire

Questionnaire 1: on the architecture of DBMS
                    Question 1: What is a database made of?

1. A set of tables.
                    2. From a set of files.
                    3. From a set of records.

Answer: a

Explanation

See page 39 of the Hainaut book, “first conclusions”.

The word table is used instead of the word file. A record refers to a row in a table. The word line will be
                    preferably used.

Question 2: What are the challenges facing databases?

1. Bad data.
                    2. The volume of data.
                    3. Ensure easy access to data.
                    4. Their maintenance.

Answer: a, b, c and d.

Explanation

Refer to page 41.
                    Question 3: From the following list, which elements represent a function of a DBMS (database management system)?

1. Data organization.
                    2. Data management.
                    3. Data acquisition.
                    4. Data access.

Answer: a, b and d.

Explanation

Refer to page 40.

Question 4: So-called NoSQL DBMSs emerged in the 2000s to mainly fill what gap?

1. Data consistency.
                    2. Data protection.
                    3. Data accessibility

Answer: c

Explanation

The history of DBMS is detailed starting on page 42.

Question 5: Complete the following table:

Model Years Example

First generation There is no content Collectivist There is no content

Second generation There is no content There is no content ORACLE
                                                                                                                                  SQL/DS
                                                                                                                                  DB2

Third generation There is no content There is no content Oracle version 8
                                                                                                                                  SQL3

Fourth generation There is no NoSQL MongoDB content
                                                                                                                                  Cassandra

Answer :

Model Years Example

First generation 1960 Collectivist IDS2
                                                                                                                                  IDMS
                                                                                                                                  DBMS

Second generation 1970 Relational ORACLE
                                                                                                                                  SQL/DS
                                                                                                                                  DB2

Third generation 1980 Object oriented Oracle version 8
                                                                                                                                  SQL3

Fourth generation 2000 NoSQL MongoDB
                                                                                                                                  Cassandra

Explanation

The evolution of DBMS is described starting on page 42 of the Hainaut book. The table provides a summary of this history.

Self-assessment activity
                    To prepare for graded work, complete the following activity.

Consider the following relational diagram:

Professor (professor ID, name, address, salary, office building)
                       Course (course acronym, teacher identifier, classroom number, start of course, end of course)
                       Classroom (classroom number, room capacity, building)

Question 1: In order to ensure the uniqueness of the tuples of each entity, what attributes could constitute the primary key of each entity?

Answer :

teacher identifier, course acronym, classroom number.

Question 2: Which teachers earn more than $80,000?

Answer :

RESTRICT (Professor, salary>80,000)

Question 3: Which professors give courses in the same building where their office is?

Answer :

R1=JOIN(Teacher,Classroom)
                    R2=JOIN(R1,Course)
                    R3=RESTRICT(R2, building where the office is=building)
                    PROJECT(R3, teacher ID, name)

There are other acceptable formulations, such as:

R1 = JOIN (Teacher, Course, Classroom)
                    R2 = RESTRICT (R1, building = building where the office is)
                    R2 = RESTRICT (R1, building = building where the office is)

Question 4: Which professors only give classes in the same building where their office is?

Answer :

R1=JOIN(Teacher,Classroom)
                    R2=JOIN(R1,Course)
                    R3=RESTRICT(R2, building where the office is<>building)
                    R4=PROJECT(R3, teacher identifier, name)
                    R5=PROJECT(R2, teacher identifier, name)
                    DIFFERENCE(R5,R4)

We can accept other formulations like this:

R1 = JOIN (Teacher, Course, Classroom)
                    R2 = RESTRICT (R1, building = building where the office is)
                    R3 = PROJECT (R2, name)
                    R4 = RESTRICT (R1, building ≠ building where the office is)
                    R5 = PROJECT (R4, name)
                    RESULT = MINUS (R2 - R4)

Question 5: Which teachers give a lesson before 9:00 a.m.?

Answer :

R1=JOIN(Professor,Course)
                    R2=RESTRICT(R1, start of class <9:00 a.m.)
                    PROJECT(R2, teacher ID, name)

Question 6: Identify at least two keys to the Teacher entity.

Answer :

Any set of attributes containing the teacher ID is a key. We could therefore use the following keys:

teacher ID, name, address, salary
                    teacher ID, name
                    teacher ID, name, address
                    ...

Question 7: Identify a foreign key in the schema.

Answer :

The classroom number attribute of the course entity is a foreign key.

Question 8: Does an entity absolutely have to contain a foreign key?

Answer :

No.

Question 9: Does an entity absolutely have to contain a key?

Answer :

No.

Question 10: Does a foreign key of one entity absolutely have to be a primary key of another entity?

Answer :

No. It has to be a key from another entity, but not necessarily a primary key. On the other hand, in practice, it is often the
                    case that a foreign key is a primary key of another entity

Question 11: Which professors teach more than 3 courses?

Answer :

R1=JOIN(course, teacher)
                    R2=AGGREGATE (R1, teacher identifier, name, account (course acronym))
                    R3=RESTRICT(R2, course acronym>3)
                    PROJECT(R3, teacher identifier, name)

Question 12: Which professors teach more than 5 courses or less than 3 courses?

Answer :

R1=JOIN(course, teacher)
                    R2=AGGREGATE (R1, teacher identifier, name, account (course acronym))
                    R3=RESTRICT(R2, course acronym>5)
                    R4=RESTRICT(R2, course acronym<3)
                    R5=PROJECT(R3, teacher identifier, name)
                    R6=PROJECT(R4, teacher identifier, name)
                    UNION(R5,R6)

Question 13: Which professors teach more than 5 courses and who teach the INF 1250 course?

Answer :

R1=JOIN(course, teacher)
                    R2=AGGREGATE (R1, teacher identifier, name, account (course acronym))
                    R3=RESTRICT(R2, account(course acronym)>5)
                    R4=RESTRICT(R3, course acronym = INF 1250)
                    PROJECT(R4, teacher ID, name)

Question 14: Which professors teach more than 5 courses and an even number of courses?

Answer :

R1=JOIN(course, teacher)
                    R2=AGGREGATE (R1, teacher identifier, name, account (course acronym))
                    R3=RESTRICT(R2,COUNT (course acronym)>5)
                    R4=RESTRICT(R2,COUNT (course acronym) is even)
                    R5=PROJECT(R3, teacher identifier, name)
                    R6=PROJECT(R4, teacher identifier, name)
                    INTERSECTION(R5,R6)

Question 15: Consider the following tuples:

R1:

Jean Plumber

Pierre electrician

R2:

Jane Police

Élodie engineer

What is union(R1,R2)? What is intersection(R1,R2)? What is difference (R1,R2)?

Answer :

union(R1,R2):

Jane Police

Pierre electrician

Jane Police

Élodie engineer

intersection(R1,R2): the empty set

difference (R1,R2):

Jean Plumber

Pierre electrician

Question 16: Write a query that returns the string “empty” if there is nothing in R and “non-empty” if there is something.

Answer :

R1 = PROJECT(R,"empty")
                    R2 = MINUS(["empty"],R1)
                    R3 = PROJECT(R,"non-empty")
                    UNION(R3,R2)

Explanation :

If R is empty, then R1 will be empty and R2 = ["empty"], R3 empty and therefore, UNION(R3,R2) will be ["empty"].

If R contains something, R1 will be ["empty"], R2 will be empty, R3 will be ["non-empty"] and therefore, UNION(R2,R3) will be ["non-empty"] .

Question 17: Give the join between the following two relations.

A B

a b

c d

B D

b e

f g

Answer :

A B D

a b e
