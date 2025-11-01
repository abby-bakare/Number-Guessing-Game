## Project Title: Number Guessing Game (1–10)
## Project Author: Abiodun Bakare
## Peer Reviewer: Abdur-Rahman Olaniyan

## Description
A simple Python program that lets the user guess a random number between 1 and 10.  
It uses basic programming concepts: input/output, loops, and decision control.

---

## Algorithm (Pseudocode)
1. Start the program  
2. Generate a random number between 1 and 10  
3. Ask the user for a guess  
4. While guess is not equal to the number:  
   - If guess < number → print "Too low!"  
   - If guess > number → print "Too high!"  
   - Ask for another guess 
      - <!-- Reviewer Note: Added input validation to handle non-numeric input -->
 
5. When guess is correct → print "Congratulations!"  
6. End program  

---

## How to Run
1. Activate your environment:
   ```bash
   myenv\Scripts\Activate
