# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles

CHNL_OFFSET = [0, 2, 4, 6]

# Pulse control pin to set channel function
async def setChannelFunctionFromReset(dut, channel, func):
    dut._log.info(f"Setting CH{channel} to {func}")
    
    pulses = 0
    match (func):
        case "INV": pulses = 0
        case "AND": pulses = 1
        case "OR" : pulses = 2
        case "XOR": pulses = 3
        case _: dut._log.info(f"INVALID FUNCTION={func}"); pulses = -1

    assert pulses >= 0 and pulses <= 3
    
    for pulse in range(pulses):
        dut._log.info(f"pulse={pulse+1}, {channel=}")
        dut.uio_in.value = 1 << CHNL_OFFSET[channel]
        await ClockCycles(dut.clk, 1)
        dut.uio_in.value = 0 << CHNL_OFFSET[channel]
        await ClockCycles(dut.clk, 1)

async def reset(dut):
    # Reset
    dut._log.info("~Reset~")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 3)
    dut.rst_n.value = 1
    await ClockCycles(dut.clk, 2)


# @cocotb.test()
async def testChannel(dut):
    # for channel in channels:
    dut._log.info("Testing all channels")

    clock = Clock(dut.clk, 10, unit='us')
    cocotb.start_soon(clock.start())

    reset(dut)

# @cocotb.test()
async def testReset(dut):
    dut._log.info(f"Testing rst_n")
    dut._log.info(f"{dut.rst_n.value=}")

    clock = Clock(dut.clk, 10, unit='us')
    cocotb.start_soon(clock.start())

    await reset(dut)

    dut._log.info(f"Initiating 1 clock cycle")
    await ClockCycles(dut.clk, 1)
    
    dut._log.info(f"Initiating 1 reset cycle")
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 1)
    assert dut.rst_n.value == 0
    
    dut.rst_n.value = 1
    await ClockCycles(dut.clk, 1)
    assert dut.rst_n.value == 1
    
    dut._log.info(f"Finished reset")

@cocotb.test()
async def testAND(dut):
    channel = 0
    dut._log.info(f"Testing CH{channel} AND")

    clock = Clock(dut.clk, 10, unit='us')
    cocotb.start_soon(clock.start())

    await reset(dut)

    await ClockCycles(dut.clk, 1)
    
    await setChannelFunctionFromReset(dut, channel, 'AND')

    # Input incrementer
    for check in range(4):
        value = f"{check:02b}"
        A = int(value[-1])
        B = int(value[ 0])
        res = (A & B)
        n_res = ~(A & B) & 0b1
        
        result = (res << CHNL_OFFSET[channel]) | (n_res << CHNL_OFFSET[channel]+1)
        
        dut._log.info(f"{A=} & {B=} = {result:02b}")
        dut._log.info(f"{CHNL_OFFSET[channel]=}")
        
        dut.ui_in.value = check << CHNL_OFFSET[channel]
        await ClockCycles(dut.clk, 1)
        dut._log.info(f"{dut.uo_out.value=}")
        assert int(dut.uo_out.value) & (0b11 << CHNL_OFFSET[channel]) == (result << CHNL_OFFSET[channel])

@cocotb.test()
async def testOR(dut):
    channel = 0
    dut._log.info(f"Testing CH{channel} OR")

    clock = Clock(dut.clk, 10, unit='us')
    cocotb.start_soon(clock.start())

    await reset(dut)

    await ClockCycles(dut.clk, 1)
    
    await setChannelFunctionFromReset(dut, channel, 'OR')

    # Input incrementer
    for check in range(4):
        value = f"{check:02b}"
        A = int(value[-1])
        B = int(value[ 0])
        res = A | B
        n_res = ~(A | B) & 0b1
                
        result = (res << CHNL_OFFSET[channel]) | (n_res << CHNL_OFFSET[channel]+1)
        
        dut._log.info(f"{A=} | {B=} = {result}")
        dut._log.info(f"{CHNL_OFFSET[channel]=}")
        
        dut.ui_in.value = check << CHNL_OFFSET[channel]
        await ClockCycles(dut.clk, 1)
        dut._log.info(f"{dut.uo_out.value=}")
        assert int(dut.uo_out.value) & (0b11 << CHNL_OFFSET[channel]) == (result << CHNL_OFFSET[channel])

@cocotb.test()
async def testXOR(dut):
    channel = 0
    dut._log.info(f"Testing CH{channel} XOR")

    clock = Clock(dut.clk, 10, unit='us')
    cocotb.start_soon(clock.start())

    await reset(dut)

    await ClockCycles(dut.clk, 1)
    
    await setChannelFunctionFromReset(dut, channel, 'XOR')

    # Input incrementer
    for check in range(4):
        value = f"{check:02b}"
        A = int(value[-1])
        B = int(value[ 0])
        res = A ^ B
        n_res = ~(A ^ B) & 0b1
                
        result = (res << CHNL_OFFSET[channel]) | (n_res << CHNL_OFFSET[channel]+1)
        
        dut._log.info(f"{A=} ^ {B=} = {result}")
        dut._log.info(f"{CHNL_OFFSET[channel]=}")
        
        dut.ui_in.value = check << CHNL_OFFSET[channel]
        await ClockCycles(dut.clk, 1)
        dut._log.info(f"{dut.uo_out.value[0]=}")
        assert int(dut.uo_out.value) & (0b11 << CHNL_OFFSET[channel]) == (result << CHNL_OFFSET[channel])