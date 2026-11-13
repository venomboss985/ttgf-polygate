/*
 * Copyright (c) 2024 Your Name
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

  module gate (
    input wire a_in,
    input wire b_in,
    input wire ctrl,
    input wire nrst,
    output reg out
    // output wire nout
  );
    reg [1:0] state;

    always @ (negedge nrst or posedge ctrl) begin
      if (~nrst) begin
        state <= 0;
        out <= 0;
      end else begin
        state <= state + 1;
        
        case (state)
          0: out <= b_in ? a_in : ~a_in;
          1: out <= a_in & b_in;
          2: out <= a_in | b_in;
          3: out <= a_in ^ b_in;
        endcase

        // nout = ~out;
      end
    end
  endmodule

module tt_um_polygate (
    input  wire [7:0] ui_in,    // Dedicated inputs
    output wire [7:0] uo_out,   // Dedicated outputs
    input  wire [7:0] uio_in,   // IOs: Input path
    output wire [7:0] uio_out,  // IOs: Output path
    output wire [7:0] uio_oe,   // IOs: Enable path (active high: 0=input, 1=output)
    input  wire       ena,      // always 1 when the design is powered, so you can ignore it
    input  wire       clk,      // clock
    input  wire       rst_n     // reset_n - low to reset
);

  // Set each channel
  wire ch0_out, ch1_out, ch2_out, ch3_out;
  // wire ch0_ctrl, ch0_a, ch0_b, ch0_and, ch0_or, ch0_xor, ch0_output;
  // reg [1:0] ch0_state;



  gate ch0 (
    .a_in(ui_in[0]),
    .b_in(ui_in[1]),
    .ctrl(uio_in[0]),
    .nrst(rst_n),
    .out(ch0_out)
    // .nout(uo_out[1])
  );

  gate ch1 (
    .a_in(ui_in[2]),
    .b_in(ui_in[3]),
    .ctrl(uio_in[1]),
    .nrst(rst_n),
    .out(ch1_out)
    // .nout(uo_out[1])
  );

  gate ch2 (
    .a_in(ui_in[4]),
    .b_in(ui_in[5]),
    .ctrl(uio_in[2]),
    .nrst(rst_n),
    .out(ch2_out)
    // .nout(uo_out[1])
  );

  gate ch3 (
    .a_in(ui_in[6]),
    .b_in(ui_in[7]),
    .ctrl(uio_in[3]),
    .nrst(rst_n),
    .out(ch3_out)
    // .nout(uo_out[1])
  );

  assign uo_out[0] = ch0_out;
  assign uo_out[1] = ~ch0_out;

  assign uo_out[2] = ch1_out;
  assign uo_out[3] = ~ch1_out;

  assign uo_out[4] = ch2_out;
  assign uo_out[5] = ~ch2_out;

  assign uo_out[6] = ch3_out;
  assign uo_out[7] = ~ch3_out;

  // Reset when rst_n goes low, otherwise run logic
  // always @ (posedge clk or negedge rst_n) begin
    // if (!rst_n) begin
    //   ch0_state = 0;
    
    // // end else begin
    // //   ch0_state = ch0_state + 1;
    // //   if (ch0_state > 2)
    // //     ch0_state = 0;
      

    // end
  // end

  // assign uio_out[7:6] = ch0_state;

  // assign ch0_ctrl = uio_in[0];
  // assign ch0_a = ui_in[0];
  // assign ch0_b = ui_in[1];
  // assign ch0_and = ch0_a & ch0_b;
  // assign ch0_or  = ch0_a | ch0_b;
  // assign ch0_xor = ch0_a ^ ch0_b;


  // assign ch0 = ch0_output;
  // assign uo_out[1:0] = {~ch0, ch0};

  // assign ch1 = ui_in[2] | ui_in[3];
  // assign uo_out[3:2] = {~ch1, ch1};

  // assign ch2 = ui_in[4] ^ ui_in[5];
  // assign uo_out[5:4] = {~ch2, ch2};

  // assign ch3 = ~ui_in[6] ^ ui_in[7];
  // assign uo_out[7:6] = {~ch3, ch3};

  // Set bidirectional pins to inputs for later use
  assign uio_out[7:0] = 0;
  assign uio_oe[7:0] = 8'b11111110;

  // List all unused inputs to prevent warnings
  wire _unused = &{ena, clk, rst_n, uio_in[7:0], 1'b0};

endmodule
