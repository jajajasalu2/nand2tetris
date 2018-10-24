// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.
(INF_LOOP)
@24576
D=M
@black
D;JGT

(white)
@color
M=0
@PAINT_SCREEN
0;JMP

(black)
@color
M=-1

(PAINT_SCREEN)
@16384
D=A
@words
A=D
(INNER_LOOP)
@color
D=M
@words
M=D
A=A+1
D=A
@24575
D=A-D
@INNER_LOOP
D;JGT

@INF_LOOP
0;JMP

