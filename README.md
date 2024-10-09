This is just an exercise in Object Oriented Programming (OOP) in Python. The aspect of this exercise is to use sepration of concerns to calculate the diamter, circumference and the area from the radius. 

One very unique aspect of this program, is the use of the round() function. The reason for this is so that the output, when displayed by the print() function, shows a value shortened to some decimal place. The method is formulated as such: 

            round(value, decimal places)

For example, when calculating the circumference and then displaying the circumference as an output, the following print statement was used: 

            print(
                f"Circumference: {round(cir_circumference, 2)}\n"
            )

            output: 31.42 from 31.41_592653589793           (31.41592653589793)

There is a possibility of this particular program to be added to a math program, that calucalates area of a geometric shape along with a circle. 