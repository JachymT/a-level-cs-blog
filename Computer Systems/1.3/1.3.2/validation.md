# Input Validation
Validation is the process of checking that data entered by a user is in the right format in order to confirm that it is sensible, acceptable and meaningful.

Different validation checks include:

## Data-type check
Requires an input to be of a certain datatype: integer, text, date... This is useful for saving storage and working with data later. Data-type checks are commenly used for inputing dates.

## Range check
Requires an input to be between certain values, like between two numbers or alphebetical words. For example someone should be born before 2003.

## Length check
Requires an input to be of a certain length, like creating password a that should be between 8 and 32 characters. 

## Presence check
Requires some data has been entered into a field. For example an email must be entered to access many databases.

## Check digits
Uses the last few digits of an input to perfom a mathemematical check on the input. for example an ISBN number has a check digit at the end, used in barcodes.

## Structured (complexity) check
Combines multiple validation checks for example where a password must contain different characters, be a certain length, and not be the same as the email. This allows for more complex validation checks and dealing with more complex data.

## Consistency check
Requires that an input makes sense in context and is logical. For example a meeting must be scheduled after todays date.

## Format check
Requires that an input follows a set format, for example a postcode, phone number or passport number.

## Table look up check
Requires an input to be part of a set list, or part of a database table. Other data should be rejected. For example a dropdown box containing gender options, or boolean choices.
