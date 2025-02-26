# colav-protobuf-utils

[![PyPI - Version](https://img.shields.io/pypi/v/colav-protobuf-utils.svg)](https://pypi.org/project/colav-protobuf-utils)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/colav-protobuf-utils.svg)](https://pypi.org/project/colav-protobuf-utils)

This package simplifies the generation of COLAV Protobuf messages as defined in [colav-protobuf](https://pypi.org/project/colav-protobuf/), allowing you to work with structured data without needing in-depth knowledge of Protobuf. Simply provide the required data to the relevant functions, and they will return the corresponding Protobuf messages. Additionally, the package includes built-in serialization and deserialization functionality for seamless data handling.

-----

## Table of Contents

- [Installation](#installation)
- [Structure](#structure)
- [Usage](#usage)
- [License](#license)

## Installation

```bash
pip install colav-protobuf-utils
```
## Structure
The src code in [colav_protobuf_utils](https://github.com/RyanMcKeeQUB/colav-protobuf-utils) shows that the project is organised into main directories: 
- [Tests](https://github.com/RyanMcKeeQUB/colav-protobuf-utils/tree/master/tests): tests that play a part in the CI/CD workflow ensuring the continued working state of this pkg
- [src/colav_protobuf_utils](https://github.com/RyanMcKeeQUB/colav-protobuf-utils/tree/master/src/colav_protobuf_utils): contains the pkg source code
    - [protobuf_generator](https://github.com/RyanMcKeeQUB/colav-protobuf-utils/tree/master/src/colav_protobuf_utils/protobuf_generator): Contains several python functions for simplication of the generation of different colav_protobuf messages, examples of usage for this pkg can be found in (usage)[]
    - [deserialization](https://github.com/RyanMcKeeQUB/colav-protobuf-utils/tree/master/src/colav_protobuf_utils/deserialization): Contains Override functions which deserialise provide abstract deserialization functionlity and validation for different colav-protobuf messages
    - [serialization](https://github.com/RyanMcKeeQUB/colav-protobuf-utils/tree/master/src/colav_protobuf_utils/serialization): Contains Override functions which abstract protobuf serialization functionality and validate that the different colav-protobuf messages are valid.

## Usage
Once pkg has been installed into your environment usage is simple.

### [protobuf_generator] (https://github.com/RyanMcKeeQUB/colav-protobuf-utils/tree/master/src/colav_protobuf_utils/protobuf_generator)

## License

`colav-protobuf-utils` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
