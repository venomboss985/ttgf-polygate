# NOTES

## General
* `uio_out` and `uio_in` will need to be set to 0 in the Verilog if not being utilized (depending on assignments)
* Registers being assigned in multiple `always` blocks will not compile due to "reg begin driven by multiple drivers"
* **NOTE: Find out why "network is combinational" error was happening**
* Cell and wire information is found in `runs/wokwi/06-yosys-synthesis/yosys-synthesis.log`
* Sign in then push to GitHub (idk why its being weird like that), if you push *even once* then sign in, subsequent push attempts will result in "Temporary failure in name resolution"

## Testing
* Remember to pulse a single clock cycle to "unreset" the chip
* Remember to `await` the `reset(...)` function (doesnt properly reset the chip otherwise)
  * and the `setChannelFunctionFromReset(...)` too
* Gate level worked after running `ciel ls` and `ciel enable <hash from ls>`, but not sure how to interpret results?

## MVP
* Functions as a flexible 4-channel logic gate chip
* Each channel is individually configurable with a dedicated control pin and output enable
* Channel functions include:
  * INV
  * AND
  * OR
  * XOR
* Functions are cycled by signaling HIGH on the channel control pin rising edge
* Outputs include Q and nQ

# TODO

## CRITICAL
- [x] Initial repo setup
- [x] (Feature) Control pin functionality
- [x] (Feature) Channel output enable functionality
- [x] (Test) INV gate test
- [ ] (Test) Control pin overflow test (CH0 cycles through all the functions and verifies it can return back to INV and function correctly without resetting)
- [ ] (Test) Parallel gate tests (CH0: INV, CH1: AND, CH2: OR, CH3: XOR) with individual OE toggle

## In Progress
- [x] Setup a test bench function for a single channel and single gate type
- [x] (Bug) Figure out why `test_project` test needs to run for `testAND` to pass?
- [x] (Test) Remove the default test case when no longer needed
- [ ] (Test) Make `setChannelFunctionFromReset()` adaptive (reads directly from chx_state)
- [*] (Docs) Update README

## Backlog
- [ ] Generative channel block?
- [x] Gate-level testing? (tested and worked, but don't really know how to interpret the results)
- [ ] Extensive docs

## Revisit

## Retired
- [ ] ~~(Test) Change channel function test to test all gate functions~~ (new parallel gate test)
- [ ] ~~(Test) Create test case list~~ (only need a couple more tests, so planning list is unnecessary atp)
- [ ] ~~(Test) Make a parallelized version of `setChannelFunctionFromReset()` (to set multiple channels at once simultaneously)~~ (parallel gate test)
* `ctypes` not needed, just had to get better at bit-masking...
