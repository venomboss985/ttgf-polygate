# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles

chnl_offset = [0, 2, 4, 6]

# func: inv=0, and=1, or=2, nand=3, nor=4, xor=5, xnor=6
async def setChannelFunction(dut, channel, func):
    # Pulse control pin to set channel function
    pass

async def reset(dut):
    # Reset
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

# @cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    reset(dut)

    dut._log.info("Test project behavior")

    # Set the input values you want to test
    dut.ui_in.value = 255
    dut.uio_in.value = 0

    # Wait for one clock cycle to see the output values
    await ClockCycles(dut.clk, 1)

    # The following assersion is just an example of how to check the output values.
    # Change it to match the actual expected output of your module:
    assert dut.uo_out.value == 0

    # Keep testing the module by changing the input values, waiting for
    # one or more clock cycles, and asserting the expected output values.

# @cocotb.test()
async def testChannel(dut):
    # for channel in channels:
    dut._log.info("Testing all channels")

    clock = Clock(dut.clk, 10, unit='us')
    cocotb.start_soon(clock.start())

    reset(dut)

@cocotb.test()
async def testAND(dut):
    channel = 0
    dut._log.info(f"Testing CH{channel} AND")

    clock = Clock(dut.clk, 10, unit='us')
    cocotb.start_soon(clock.start())

    reset(dut)

    await ClockCycles(dut.clk, 1)

    # Input incrementer
    for check_and in range(4):
        value = f"{check_and:02b}"
        A = int(value[-1])
        B = int(value[ 0])
        result = A & B
        
        dut._log.info(f"{A=} & {B=} = {result}")
        dut._log.info(f"{chnl_offset[channel]=}")
        
        dut.ui_in.value = check_and << chnl_offset[channel]
        await ClockCycles(dut.clk, 1)
        dut._log.info(f"{dut.uo_out.value[0]=}")
        assert dut.uo_out.value[0] == result << chnl_offset[channel]
