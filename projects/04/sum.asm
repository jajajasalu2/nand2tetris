@i
M=1
@sum
M=0
(LOOP)
@i
D=M
@100
D=D-A
@END
D;JGT
@sum
M=D+M
@i
M=M+1
@LOOP
0;JMP
(END)
@END
0;JMP
