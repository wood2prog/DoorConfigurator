# Door Configurator

***

### This project is designed to import a list of door sizes and other information and ultimately export a list of door parts configured in one or more of the following ways:

- Sorted by one of the columns.
- A subset of parts selected by filtering one of the columns included in the file.

***

## Input

### The imported list must be a comma delimitted file (.csv). It can have any number of columns. Such as:

- unique_id*
- length*
- width*
- thickness
- color

***These columns are necessary since the initialization of the import depends on these for defining the door objects**

***

## Errors

### The import might fail for the following reasons:

- the required columns **unique_id, length, width** are not in the imported file.
- the file is not a csv file. 

***

## Export

### It is possible to export the following items from a properly imported list:

- The frame parts of a door - top rail, bottom rail, side stiles, mid rails, etc.
- The panels for a door. This can be exported as a simple list of door panels or a cutlist of the strips necessary to glue up the door panels.
- A list of the doors and the details used for fabrication and assembly