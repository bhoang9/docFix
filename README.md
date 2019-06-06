# docFix
Adjusts documents to adhere to format of document maker.

* Able to convert bulletpoints into HTML lists
* Able to convert Spanish special characters 
* Able to fix newlines that appear from text editor formatting
* Able to create new lists (text must be formatted like a list prior)

## Bugs

* Some PDF viewers will interpret Spanish characters as two letters
  * This results as the special character being read as a 2 "letter"
  string where each letter has its own ASCII value. Cannot currently
  discern between these in a way that wouldn't be very arbitrary.
  
* Newline fixer does not account for a single blank newline very well
