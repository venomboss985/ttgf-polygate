/*
 * Copyright (c) 2024 Your Name
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

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
  wire ch0, ch1, ch2, ch3;
  reg [2:0] ch0_state;

  assign ch0 = ui_in[0] & ui_in[1];
  assign uo_out[1:0] = {~ch0, ch0};

  always @ (posedge clk or negedge rst_n) begin
    if (!rst_n) begin
      ch0_state = 0;
    
    end else begin
      if (uio_in[0] == 1)
        ch0_state += 1;

        if (ch0_state > 5)
          ch0_state = 0;
    end
  end

  assign uio_out[7:5] = ch0_state;

  assign ch1 = ui_in[2] | ui_in[3];
  assign uo_out[3:2] = {~ch1, ch1};

  assign ch2 = ui_in[4] ^ ui_in[5];
  assign uo_out[5:4] = {~ch2, ch2};

  assign ch3 = ~ui_in[6] ^ ui_in[7];
  assign uo_out[7:6] = {~ch3, ch3};

  // Set bidirectional pins to inputs for later use
  assign uio_out[4:0] = 5'b00000;
  assign uio_oe[7:0] = 8'b11111110;

  // List all unused inputs to prevent warnings
  wire _unused = &{ena, clk, rst_n, 1'b0};

endmodule
