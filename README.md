
# usain

A fast lightweight task scheduler framework based on schedule

[![Build Status](https://travis-ci.com/adhaamehab/usian.svg?branch=master)](https://travis-ci.com/adhaamehab/usian)


<img src="./icon.svg"
     width="170" height="190" align="middle" hspace="12" />



### Installation

```shell
pip install usian
```

### Usage

```python
from usain import Task, Runner


t1 = Task('test-task',
        pipe=[
            lambda x: x + 1,
            lambda x: x ** 2,
            lambda x: print(x)
        ],
        init_data=1
)

runner = Runner()

runner.add(t1, 3)

if __name__ == "__main__":
    runner.run()

```

### Features

- Simple Task Pipelines

- Multithreading Task Runner

- Handling exception

- Minimal Interface

### TODO

- Depndancy control in Runner/Task

- Use multiple interval unit than seconds (already supported in schedule)

- Task pipeline retry on fail

- Task visualization dashboard

- Visualization dashboard

- Background tasks

- Custome logging

- Tasks shared memory


Free software: MIT license

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
