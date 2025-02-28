# CMSC 126 | Lab 1: Simulating the OSI Model from Scratch in Python

## Prerequesites
- Python installed

## Running
Run the simulation using:
```bash
python osi.py
```

## Features

- Complete implementation of all 7 OSI layers:
  - Application Layer (Layer 7)
  - Presentation Layer (Layer 6)
  - Session Layer (Layer 5)
  - Transport Layer (Layer 4)
  - Network Layer (Layer 3)
  - Data Link Layer (Layer 2)
  - Physical Layer (Layer 1)
- Detailed logging with timestamps
- Error handling and validation
- Simulated network protocols and headers
- Real-time visualization of data flow
- Example email transmission scenario

## Layer Descriptions

### Physical Layer (Layer 1)
- Converts data to binary streams
- Simulates physical transmission
- Handles bit-level operations

### Data Link Layer (Layer 2)
- Manages MAC addressing
- Implements frame creation
- Includes CRC checksums

### Network Layer (Layer 3)
- Handles IP addressing
- Manages packet routing
- Implements TTL and versioning

### Transport Layer (Layer 4)
- Manages TCP segments
- Handles sequencing
- Controls flow and windows

### Session Layer (Layer 5)
- Manages session establishment
- Handles session tracking
- Implements basic authentication

### Presentation Layer (Layer 6)
- Handles data encoding/decoding
- Manages data compression
- Implements data formatting

### Application Layer (Layer 7)
- Creates HTTP-like requests
- Manages application data
- Handles user data formatting