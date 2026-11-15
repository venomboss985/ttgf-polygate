<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

*TODO: Explain how your project works*

Each channel on the device acts as it's own individually configurable gate. They can be configured as an inverter, AND gate, OR gate, or XOR gate (in that order). It starts on Invert mode on power up.

To change the gate function, pulse that channels control pin to the desired gate function.

*Ex. Switch channel 1 to OR mode from power up by sending 2 pulses to `uio_in[1]`*

### Output Enable

*TODO: describe output enable*

### Gate functions

#### Invert mode

*Note: This mode is functionally similar to XOR, but is here as a placeholder until another function is implemented*

`Q = B ? ~A : A`

| A | B | Q |
|:-:|:-:|:-:|
| 0 | 0 | 0 |
| 1 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 1 | 0 |

#### AND mode

`Q = A & B`

| A | B | Q |
|:-:|:-:|:-:|
| 0 | 0 | 0 |
| 1 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 1 | 1 |

#### OR mode

`Q = A | B`

| A | B | Q |
|:-:|:-:|:-:|
| 0 | 0 | 0 |
| 1 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 1 | 1 |

#### XOR mode

`Q = A ^ B`

| A | B | Q |
|:-:|:-:|:-:|
| 0 | 0 | 0 |
| 1 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 1 | 0 |

## How to test

*TODO: Explain how to use your project*

## External hardware

*TODO: CircuitPython module for hardware control*

* Recommend using a microcontroller for precise control

### IO Map

| # | Inputs | Outputs | Bidirectional |
|:-:|:------:|:-------:|:-------------:|
| 0 | A(CH0) |  Q(CH0) | CTRL(CH0) |
| 1 | B(CH0) | nQ(CH0) | CTRL(CH1) |
| 2 | A(CH1) |  Q(CH1) | CTRL(CH2) |
| 3 | B(CH1) | nQ(CH1) | CTRL(CH3) |
| 4 | A(CH2) |  Q(CH2) | OE(CH0)   |
| 5 | B(CH2) | nQ(CH2) | OE(CH1)   |
| 6 | A(CH3) |  Q(CH3) | OE(CH2)   |
| 7 | B(CH3) | nQ(CH3) | OE(CH3)   |

**Legend:**
* *CHx = channel x (ex. CH0 = channel 0)*
* *A/B = A input or B input*
* *Q = channel output*
* *nQ = channel inverted output*
* *CTRL = channel control pin*
* *OE = channel output enable*
