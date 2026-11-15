# NOTES

## General
* `uio_out` and `uio_in` will need to be set to 0 in the Verilog if not being utilized (depending on assignments)
* Registers being assigned in multiple `always` blocks will not compile due to "reg begin driven by multiple drivers"
* **NOTE: Find out why "network is combinational" error was happening**

## Testing
* Remember to pulse a single clock cycle to "unreset" the chip
* Remember to `await` the `reset(...)` function (doesnt properly reset the chip otherwise)
    * and the `setChannelFunctionFromReset(...)` too

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
- [x] (Feature) Control pin functionality
- [ ] (Feature) Channel output enable functionality
- [ ] (Test) INV gate test
- [ ] (Test) Parallel gate tests (CH0: INV, CH1: AND, CH2: OR, CH3: XOR)

## In Progress
- [x] Setup a test bench function for a single channel and single gate type
- [ ] (Test) Change channel function test to test all gate functions
- [x] (Bug) Figure out why `test_project` test needs to run for `testAND` to pass?
- [ ] (Test) Create test case list
- [x] (Test) Remove the default test case when no longer needed
- [ ] (Test) Make `setChannelFunctionFromReset()` adaptive (reads from chx_state)
- [ ] (Test) Make a parallelized version of `setChannelFunctionFromReset()` (to set multiple channels at once simultaneously)
- [ ] (Docs) Update README

## Backlog
- [ ] Generative channel block
- [ ] Gate-level testing
- [ ] Extensive docs

## Revisit

## Retired
* `ctypes` not needed, just had to get better at bit-masking...
