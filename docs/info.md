<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

Each channel on the device acts as it's own individually configurable gate. They can be configured as an inverter, AND gate, OR gate, or XOR gate (in that order). It starts on Invert mode on reset.

### Channel Inputs and Outputs

There are two input pins (`A` and `B`) and two output pins (`Q` and `~Q`) per channel. The inputs are your typical logical inputs that the gate will act upon, and the output pins offer both the inverted and non-inverted signals of that gates' transformation

The `~Q` signal is a **direct inversion** of the `Q` output, so if you want the inverted output from a channel's gate, refer to the gate function truth tables below and flip the output bit.

### Control

To change the gate function, pulse that channel's control pin to the desired gate function and will change on the **rising edge**. The functions are **cyclical** and will automatically set to Invert mode upon reset.

`Invert>AND>OR>XOR>Invert>...`

| Channel function | Next function after pulse |
|:----------------:|:----:|
| Invert | AND |
| AND | OR |
| OR  | XOR |
| XOR | Invert |

*Ex. Switch channel 1 to OR mode from reset by sending 2 pulses to `uio_in[1]`*

### Output Enable

There are also **active-high** output enable pins that are available for each channel.

| OE | Q |
|:--:|:-:|
| 0  | x |
| 1  | 0 or 1 |

### Gate functions

#### Invert mode

Pulse 0 times from reset

*Note: This mode is functionally similar to XOR, but is here as a placeholder until another function is implemented*

`Q = B ? ~A : A`

| A | B | Q |
|:-:|:-:|:-:|
| 0 | 0 | 0 |
| 1 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 1 | 0 |

#### AND mode

Pulse 1 time from reset

`Q = A & B`

| A | B | Q |
|:-:|:-:|:-:|
| 0 | 0 | 0 |
| 1 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 1 | 1 |

#### OR mode

Pulse 2 times from reset

`Q = A | B`

| A | B | Q |
|:-:|:-:|:-:|
| 0 | 0 | 0 |
| 1 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 1 | 1 |

#### XOR mode

Pulse 3 times from reset

`Q = A ^ B`

| A | B | Q |
|:-:|:-:|:-:|
| 0 | 0 | 0 |
| 1 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 1 | 0 |

## How to test

*TODO: Add pictures after tapeout*

1. Power the chip on and switch to the design (reference the Tiny Tapeout guide [here](https://tinytapeout.com/guides/get-started-breakout-card/))
2. Put an LED on one of the channels' output pins
3. Put either buttons or DIP switches on the input pins of the same channel (`A`, `B`, `CTRL`, and `OE` pins)
4. Pulse one of the channels' `CTRL` pins once to switch it to `AND` mode
5. At this point, adjusting the `A` and `B` pins should output nothing in every configuration as the corresponding `OE` pin has not been set yet
6. Set the `OE` pin for that channel `HIGH`
7. Adjusting the same `A` and `B` pins again should change the output according to the `AND` function's truth table listed above

## External hardware

*TODO: CircuitPython module for hardware control*

* For development: [Tiny Tapeout demoboard](https://github.com/TinyTapeout/tt-demo-pcb)
* For other uses: Recommend using a microcontroller for precise control

### IO Map

| # | Inputs | Outputs | Bidirectional |
|:-:|:------:|:-------:|:-------------:|
| 0 | A(CH0) |  Q(CH0) | CTRL(CH0) |
| 1 | B(CH0) | ~Q(CH0) | CTRL(CH1) |
| 2 | A(CH1) |  Q(CH1) | CTRL(CH2) |
| 3 | B(CH1) | ~Q(CH1) | CTRL(CH3) |
| 4 | A(CH2) |  Q(CH2) | OE(CH0)   |
| 5 | B(CH2) | ~Q(CH2) | OE(CH1)   |
| 6 | A(CH3) |  Q(CH3) | OE(CH2)   |
| 7 | B(CH3) | ~Q(CH3) | OE(CH3)   |

**Legend:**
* *CHx = channel x (ex. CH0 = channel 0)*
* *A/B = A input or B input*
* *Q = channel output*
* *~Q = channel inverted output*
* *CTRL = channel control pin*
* *OE = channel output enable*
