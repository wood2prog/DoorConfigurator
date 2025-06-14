# Door Configurator

***

### This project is designed to import a list of door sizes and other information and ultimately export a list of door parts configured in one or more of the following ways:

- Sorted by one of the columns.
- A subset of parts selected by filtering one of the columns included in the file.

### The list that can be imported must be a comma delimitted file (.csv). It can have any number of columns and the columns are the different types of data. Such as:

- unique_id
- length
- width
- thickness
- color

### The only columns that are necessary are the unique_id, length, and width columns. If you don't have these columns the import will fail. The reason for this is:

- The dimensions and id are required during initial import of the door objects in the list.
- There isn't much use for the program if the doors don't have any dimensions
- The id is used to create a unique reference to each door. If the id is not unique the import will fail.

### It is possible to export the following items from a properly imported list:

- The frame parts of a door - top rail, bottom rail, side stiles, mid rails, etc.
- The panels for a door. This can be exported as a simple list of door panels or a cutlist of the strips necessary to glue up the door panels.
- A list of the doors and the details used for fabrication and assembly