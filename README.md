[Documentatie](https://docs.google.com/document/d/1oLFMqnbFzGv6Rmf4rerF7mPBoxEW1BKRBdt6uiz1G4Q/edit)  
Rezolvarea problemei de optimizare a unei mașini cu vectori suport cu ajutorul unui algoritm evolutiv:  
* Mai întâi, se va alege o problemă de clasificare pe care să o învețe SVM-ul. S-a ales detectia site-urilor de phishing, folosindu-ne de [acest dataset](https://archive.ics.uci.edu/ml/datasets/phishing+websites).  
* Apoi, pentru acea problemă, se va rezolva problema duală a SVM cu
ajutorul algoritmului evolutiv cu codare reală.  
* Pentru satisfacerea constrângerilor legate de multiplicatorii lagrangieni, se
poate folosi procedura de ajustare din secțiunea V.C a [articolului](https://www.researchgate.net/publication/309565420_Evolutionary_Support_Vector_Machines_A_Dual_Approach).  
* În final, se vor afișa rezultatele obținute de SVM pentru
mulțimea de antrenare a problemei de clasificare. Pentru algoritmul evolutiv, trebuie implementă varianta standard
prezentată în curs.