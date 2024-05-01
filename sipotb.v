module test;
reg clk; reg rst;
 
reg data_in;
wire [3:0] data_out;
wire [3:0] data_out_ref;

SIPO M1 (clk,rst,data_in,data_out);
SIPO_l M2 (clk,rst,data_in,data_out_ref);
always #5 clk=!clk;

initial begin
$dumpfile("dump.vcd");
$dumpvars; clk=0;
rst=0; data_in=0; #7;
rst=1; #2;
repeat (20) begin data_in=1;
 
@(posedge clk); #3;
end

#100;
$finish;

always @ (posedge clk) begin #1;
$display("DATA_IN=%b DATA_OUT=%b",data_in,data_out);