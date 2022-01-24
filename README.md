# Python Webservice Architecture

Base Python3 webservice architecture for future projects.

## Object

The main object of this architecture is split all components into 5 parts and remove
correlation between them.

Be side that, detach the entrypoint layer from the others so that we can easily change
framework or communication protocol. Eg: change FastAPI to Flask or HTTP to GRPC.

See [components](#components) session for more information.

## Requirements (Programs & Libs)


## Components

The HTTP Layer 

![architecture diagram](images/architecture/diagram.png)

## How to use
