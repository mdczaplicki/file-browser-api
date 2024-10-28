# File Browser API
This is a simple API that allows you to do a set of operations on files & directories

## Dependencies
1. [Docker Desktop](https://www.docker.com/products/docker-desktop/)
2. [Justfile](https://github.com/casey/just) (optional)

## Development workflow
Whole application is containerized, 
it means that you don't need to install poetry or any other tool to run or work with the repository. 
All you need is `Docker` & `just` (optionally).

Read through `Justfile`/`Justscripts` to understand the recipies.

There are volumes mounted into the container, so that all the changes are reflected on both sides (host & container).

## Starting the application

*If you haven't installed `just`, you need to run `source Justscripts` and then you can use the recipies without `just`*

1. Run `just build`/`build`
2. Run `just up`/`up`
3. Visit http://localhost:8000/docs. You can play with the API through OpenAPI documentation.
The initial playground is present in `_playground` directory on the host. When building the image - the playground
is copied to `/opt/playground`. The container doesn't have the playground mounted to host machine, so all the changes
done through the API only occur in the container.

## Missing parts
1. Write tests for the routers using an [httpx](https://www.python-httpx.org/) client
2. Write tests for controller