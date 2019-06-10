# docFix
Adjusts documents to adhere to format of document maker.

## Features
* Convert bulletpoint lists into HTML lists
* Convert Spanish special characters 
* Fix newlines that appear from text editor formatting
* Able to create new lists (text must be formatted like a list prior)
* Add HTML tags (bold, underline, italics)

## Bugs

* Some PDF viewers will interpret Spanish characters as two letters
  * This results as the special character being read as a 2 "letter"
  string where each letter has its own ASCII value. Cannot currently
  discern between these in a way that wouldn't be very arbitrary.
  
* Newline fixer does not account for a single blank newline very well
