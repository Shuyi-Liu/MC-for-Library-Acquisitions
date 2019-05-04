# Title
MC-Simulation for Library Acquisitions

# Team Member
JinKyung Lee (Git: jin-kyung), Shuyi Liu (Git: Shuyi-Liu)

# Summary
Library Acquisitions refer to a library response for the selection and purchase of materials or resources. Acquisitions may be impacted by budget, library space, materials format, resources price, users’ preference, etc. There are several ways to acquire materials: purchase, subscriptions, interlibrary loan, gifts, etc.

Our primary goal in the project is to simulate the possibility of acquisitions focusing on printed and e-books. The project has two steps. The first step is to create a book list. The book list includes book price, thickness, and user's demands (preference). The second step is that to select books from the list. we selected books based on budget and space. 

For the simulation, we also consider indirect costs including maintenance and cataloging costs, since acquisitions refer to buying book as well as providing books for user access. This costs are calculated based on annual wage, volume of collections, and a cataloger's productivity.  

In addition, there are one more variables we consider in terms of e-books. A vendor provides e-book in three different conditions based on Based on GOBI vendors: one person access, three person access, and unlimited access. Depending on condititiosn, e-book price changes. For example, price of three person access is 1.5 times higher than price of one person access. Also, unlimited is 2 times higher than one person access.

In the simulation, we consider two stragegies: users' demands and expansion of collections (purchase books as many as a library can based on budget and space).Thus, our results consists of number of books, total prices, and total thickness of each strategy.

We simulate two different cases, to purchase printed books only and to purchase printed and e-books together. In each case, we simulate 100 times.
 
 
# Hypothesis
1.     If a library purchases only printed books, the two strategies may not remarkably impact total number of books, total prices, and thickness.

2.     If a library purchased both printed and electronic books, the two strategies remarkably impact total number of books and number of thickness; however, total prices are not significantly different.


# About Codes and Files
There are four files related to the simulation.
Preliminary.py is the code of the MC simulation for purchasing only printed books.
Preliminary_printed_book_acquisitions.ipynb explores the code and visualization.
The second-simulation.py is the code of the MC simulation for purchasing both printed and electronic books.
The second-simulation-notebook.ipynb explores the code and visualization.

 
# Reference
ALCTS Technical Services Costs Committee. "Guide to Cost Analysis of Acquisitions and Cataloging in Libraries," ALCTS Newsletter 2. no. 5, 1991: 49-52.

American Library Association. “Acquisitions Procedures.” http://www.ala.org/tools/challengesupport/selectionpolicytoolkit/acquisitions. Accessed on April 11. 2019.

Arms, W. Y. and T. P. Walter, “A Simulation Model for Purchasing Duplicate Copies in a Library.” Information Technology and Libraries 7, issue 2. 1974: 73-82.

Burger, Robert H. Financial Management of Libraries and Information Centers. California and Colorado: Libraries Unlimited, 2017.

Calvi, Elise. Yvonne Carignan, Liz Dube, and Whitney Pape. The Preservation Manager's Guide to Cost Analysis. Chicago: American Library Association, 2006.






