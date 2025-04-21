# sudoku
personal project for boot.dev course, implementing a sudoku game in python (no difficulty differences, only to present a somewhat easy random board and allow the user to fill with pencil or pen the empty spaces).

to clone: save all files in one folder with src subfolder as is
confirm if requirements are met
run main.sh

in game controls:
you can move your focus (the yellow part) around with mouse or wasd
where your focus is you can input a number for the cell (if there is a black number already you cannot overwrite it)
you can del caracters with DEL
you can change from pen to pencil and the other way aroud clicking on the buttons bellow boar (mouse required)
when you solve the board (with pen), click to validate, if it is right it will show and close, case it is not, a message of invalid
    solution appears and the game continues

#future implementation plans (just for fun):
    - moving mode: the board will bounce around to make it harder to concentrate (a pause button shall be provided)
    - schizo board: the cells are not draw alonside of each other, they will be all around with indexes showing
    - completly schizo: same as above, but the cells will be moving around (a pause button shall be provided)
