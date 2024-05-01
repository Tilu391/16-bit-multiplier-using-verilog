



 


module SISO(clk,rst,data_in,data_out)
input clk;
input rst;
input data_in;
output data_out;

 reg [3:0] temp;

assign data_out=temp[0];

always @ (posedge clk, negedge rst) begin
if(!rst) temp<=4'b0000;
else begin

temp[3]<=data_in;
temp[2]<=temp[3];
temp[1]<=temp[2];
temp[0]<=temp[1];
end
end
endmodule

DEGITAL DESIGN AND COMPUTER ORGA


BATCH NO.5




Section-A
PES2UG21CS055-ALEKHYA PONNEKANTI PES2UG21CS053-AKULA PRANAVI
PES2UG20CS347- SREE HEMA HASMITA KANCHARLA

 
PES2UG21CS031-ADITI KHASNIS
 
SISO AND SIPO
 









 


Clas
 
Design & implement a 4– bit Shift Register (serial–in,
 


serial–out & serial–in, parallel–out).
 


Table of Contents
1.	Abstract
2.	Siso and Sipo
2.1.	what is Siso?
2.2.	Siso implementation and scope ..
2.3.	What is Sipo ?
2.4.	Sipo implementation and Scope ..


3.	Code
4.	VVp output and GTK wave
6.	References	24
 



Abstract
In this project we are making 4 bit serial in serial out (SISO) and serial in serial out (SIPO)
The use of SISO shift register is to act as temporary data storage device.
But the main use of a siso is to act as a delay element
In SIPO type of register,serial data input can be taken from the left side of the Flip Flop and generates an equivalent output.



 


2.1 What is Siso?
Serial In Serial Out shift registers delay data by one clock time for each stage. They will store a bit of data for each register .
Thus, this is all about an overview of the SISO shift register – working with applications. Similarly, the SISO shift register using Jk Flip-Flop can also be designed like using D flip flops but it needs the
connection of both the inputs of J & K. Like the above D-FF-based shift register, in the JK FF-based shift register also both the inputs are given at the left side flip flop where all the FFs are serially connected

 




 

The use of SISO shift register is to act as temporary data storage device. But the main use of a SISO is to act as a delay element.
2.3	What is Sipo?
The Shift Register which allows serial input parallel output is known as the SIPO shift register. In the SIPO register, the term SIPO stands for serial input parallel output. In this type of shift register, the input data is given bit by bit serially. For each clock pulse, the input data at all the FFs can be shifted by a single position. The o/p at every flip-flop can be received parallel.
 





2.4	SIPO IMPLEMENTATION
1.	In this type of register, serial data input can be taken from the left side of the FF & generates an equivalent output. The applications of these registers include communication lines because the main function of the SIPO register is to change serial information into parallel information.
2.	SIPO registers are commonly attached to the output of microprocessors when more general-purpose input/output pins are required than are available.







Verilog code:

module SIPO (clk,rst,data_in,data_out); input clk;
 

input rst; input data_in;
output [3:0] data_out;

reg [3:0] temp;

assign data_out=temp;

always @ (posedge clk, negedge rst) begin if(!rst) temp<=4'b0000;
else begin
temp[0]<=data_in; temp[1]<=temp[0]; temp[2]<=temp[1]; temp[3]<=temp[2]; end
end endmodule

//SIPO
 

module SIPO_l (clk,rst,data_in,data_out); input clk;
input rst; input data_in;
output [3:0] data_out;

reg [3:0] temp;

assign data_out=temp;
always @ (posedge clk, negedge rst) begin if(!rst) temp<=4'b0000;
else begin
temp<={temp[2:0],data_in}; end
end endmodule

Testbench file:
module test;
reg clk; reg rst;
 


reg data_in;
wire [3:0] data_out;
wire [3:0] data_out_ref;


SIPO M1 (clk,rst,data_in,data_out); SIPO_l M2 (clk,rst,data_in,data_out_ref);

always #5 clk=!clk;


initial begin
$dumpfile("dump.vcd");
$dumpvars; clk=0;
rst=0; data_in=0; #7;
rst=1; #2;
repeat (20) begin data_in=1;
 


@(posedge clk); #3;
end

 



end
 
#100;
$finish;
 



always @ (posedge clk) begin #1;
$display("DATA_IN=%b DATA_OUT=%b",data_in,data_out);
if (data_out == data_out_ref)
$display ("DESIGN CORRECT");

 
else


end
 

$display ("DESIGN WRONG");
 

endmodule
4.
Verilog VVP Output Screen Shot:(SIPO)
 


 
 


 

GTKWAVE Screenshot :
 


 


Truth table:

Circuit diagram:
 



 


Timing Diagram:


Verilog code:




 



 

























 



 






















 



 


Testbench file:























 



 
















 






 



Verilog VVP Output Screen Shot:
 


 





GTKWAVE Screenshot :
 


 




Truth table:

 

Circuit diagram:



Timing Diagram:
 


 




1.	References

https://www.allaboutcircuits.com/uploads/articles/synchronize
-the-data-to-system-wide-clock-in-a-circuit-board.jpg

https://youtu.be/sTh0ZJv5r90
 
circuit-board.jpg

















