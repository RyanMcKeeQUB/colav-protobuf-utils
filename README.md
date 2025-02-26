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

The source code in [colav_protobuf_utils](https://github.com/RyanMcKeeQUB/colav-protobuf-utils) is organized into the following main directories:

- [Tests](https://github.com/RyanMcKeeQUB/colav-protobuf-utils/tree/master/tests): Contains tests that ensure the continued working state of this package as part of the CI/CD workflow.
- [src/colav_protobuf_utils](https://github.com/RyanMcKeeQUB/colav-protobuf-utils/tree/master/src/colav_protobuf_utils): Contains the package source code.
    - [protobuf_generator](https://github.com/RyanMcKeeQUB/colav-protobuf-utils/tree/master/src/colav_protobuf_utils/protobuf_generator): Contains several Python functions for simplifying the generation of different colav_protobuf messages. Examples of usage for this package can be found in the [Usage](#usage) section.
    - [deserialization](https://github.com/RyanMcKeeQUB/colav-protobuf-utils/tree/master/src/colav_protobuf_utils/deserialization): Contains functions that provide abstract deserialization functionality and validation for different colav-protobuf messages.
    - [serialization](https://github.com/RyanMcKeeQUB/colav-protobuf-utils/tree/master/src/colav_protobuf_utils/serialization): Contains functions that abstract Protobuf serialization functionality and validate the different colav-protobuf messages.

## Usage

Once the package has been installed into your environment, usage is simple.

### Imports

```python
# Protobuf generation imports
from colav_protobuf_utils.protobuf_generator import (
    gen_mission_request,  # Mission Request 
    VesselType,
    gen_mission_response,  # Mission Response
    MissionResponseTypeEnum,
    gen_agent_update,  # Agent Update
    gen_obstacles_update,  # Obstacles update
    gen_static_obstacle, 
    StaticObstacleTypeEnum,
    gen_dynamic_obstacle,
    DynamicObstacleTypeEnum,
    gen_controller_feedback,  # Controller Feedback
    CTRLStatus,
    CTRLMode,
)

# Protobuf serialization import
from colav_protobuf_utils.serialization import serialise_protobuf

# Protobuf deserialization import
from colav_protobuf_utils.deserialization import deserialise_protobuf
```

### Sample Mission Request Creation

```python
mission_req_proto = gen_mission_request(
    tag="sample_mission_tag",
    timestamp="1677256958",
    vessel_tag="sample_vessel",
    vessel_type=VesselType.VESSEL.value,
    vessel_max_acceleration=2.0,
    vessel_max_deceleration=1.0,
    vessel_max_velocity=30.0,
    vessel_min_velocity=15.0,
    vessel_max_yaw_rate=0.2,
    vessel_loa=2.0,
    vessel_beam=0.5,
    vessel_safety_radius=5.0,
    cartesian_init_position=(30002.0, 2312.0, 10.0),
    cartesian_goal_position=(30402.0, 2000.0, 10.0),
    goal_safety_radius=10
)
```

### Sample Serialization

```python
serialized_msg = serialise_protobuf(mission_req_proto)
```

### Sample Deserialization

```python
deserialized_msg = deserialise_protobuf(serialized_msg)
```

## License

`colav-protobuf-utils` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
