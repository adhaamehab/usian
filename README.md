
# usain

A native fast lightweight task scheduler framework and background jobs

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
    runner.run() # will run in the background
    print('hello usain') # will be printed while the task running

'''

| INFO     | usain.usain:_run_job:61 -
| INFO     | usain.usain:_run:34 - Running pipeline for task test-task with intial data
hello usain
| DEBUG    | usain.usain:_run:35 - Task test-task running at node 1 out of 3
| DEBUG    | usain.usain:_run:38 - Task test-task running at node 2 out of 3
| DEBUG    | usain.usain:_run:38 - Task test-task running at node 3 out of 3
4
| INFO     | usain.usain:_run_job:61 -
| INFO     | usain.usain:_run:34 - Running pipeline for task test-task with intial data
| DEBUG    | usain.usain:_run:35 - Task test-task running at node 1 out of 3
| DEBUG    | usain.usain:_run:38 - Task test-task running at node 2 out of 3
| DEBUG    | usain.usain:_run:38 - Task test-task running at node 3 out of 3
4
'''
# will keep going

```

### Features

- Simple Task Pipelines

- Multithreading Task Runner

- Handling exception

- Minimal Interface

- Background jobs

- Non-blocking runner

- Add new tasks on runtime

### TODO

- Depndancy control in Runner/Task

- Use multiple interval unit than seconds (already supported in schedule)

- Task pipeline retry on fail

- Task visualization dashboard

- Custome logging

- Tasks shared memory



Free software: MIT license

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
