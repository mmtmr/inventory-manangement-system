# Automobile Parts Inventory Management System
In this assignment, students are required to design an automobile parts inventory management system.
There are four designs needed for this system, including parts inventory creation in warehouses, parts inventory update, parts inventory tracking and searching functionalities.

This automobile manufacturing plant has several divisions, each division assembles a different model. This form of departmentalization is called product departmentalization, where each model has its own assembly line, which is assembly division in this case. Each assembly division has several assembly sections. The assembly sections assemblies the parts of specific car model. There is only one variant for each car model. Therefore, the assembly section each assembly one type of the car section. Every assembly division has one warehouse that stores different parts for each car model, which later will be sent to specific assembly section. Different assembly section may use the same kind of parts stored in the warehouse.

There are six elements needed in the inventory system, which are part id, warehouse code, assembly division, assembly section, quantity and supplier details. In my assumption on the inventory creation, the assembly section should have the same name as the car model. Also, it should allow user to decide the amount of assembly divisions or warehouse in the plant and the assembly sections under each division.

I first designed a system to add warehouse, assembly section and part types according to the user’s needs.

The system probably will only be modified when a new product line is established, or the design of an assembly section or car model is changed. I assumed that the system needs four function: adding new section, division or parts, modify purely the quantities of parts, print and search. The program should go through different file to obtain data.

## Overview of Functions
![Overview Of Functions](https://user-images.githubusercontent.com/76145646/150675943-639620be-c0cd-4c3d-b739-8c9a7f62638c.png)
