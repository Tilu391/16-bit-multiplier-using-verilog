module SIPO (clk,rst,data_in,data_out); input clk;
 

input rst; input data_in;
output [3:0] data_out;

reg [3:0] temp;

assign data_out=temp;

always @ (posedge clk, negedge rst) begin if(!rst) temp<=4'b0000;
else begin
temp[0]<=data_in; temp[1]<=temp[0]; temp[2]<=temp[1]; temp[3]<=temp[2]; end
end endmodule
 

module SIPO_l (clk,rst,data_in,data_out); input clk;
input rst; input data_in;
output [3:0] data_out;

reg [3:0] temp;

assign data_out=temp;
always @ (posedge clk, negedge rst) begin if(!rst) temp<=4'b0000;
else begin
temp<={temp[2:0],data_in}; end
end endmodule