# NOTES

## General
* `uio_out` and `uio_in` will need to be set to 0 in the Verilog if not being utilized (depending on assignments)

## Testing
* Remember to pulse a single clock cycle to "unreset" the chip
* Remember to `await` the `reset(dut)` function (doesnt properly reset the chip otherwise)

## MVP
* Functions as a flexible 4-channel logic gate chip
* Each channel is individually configurable with a dedicated output enable
* Channel functions include:
    * AND
    * OR
    * XOR
* Functions are cycled by signaling HIGH on the channel control pin while `clk` is HIGH
* Outputs include Q and nQ

# TODO

## CRITICAL
- [x] Initial repo setup
- [ ] (Test) Start using `ctypes` to make bitwise testing easier
- [ ] (Feature) Control pin functionality

## In Progress
- [x] Setup a test bench function for a single channel and single gate type
- [ ] (Test) Change channel function test to test all gate functions
- [x] (Bug) Figure out why `test_project` test needs to run for `testAND` to pass?
- [ ] (Test) Create test case list
- [ ] (Docs) Update README
- [x] (Test) Remove the default test case when no longer needed
- [ ] (Test) Make `setChannelFunctionFromReset()` adaptive (reads from chx_state)
- [ ] (Test) Make a parallelized version of `setChannelFunctionFromReset()` (to set multiple channels at once simultaneously)

## Backlog
- [ ] Generative channel block
- [ ] Gate-level testing
- [ ] Extensive docs

## Revisit

## Retired
