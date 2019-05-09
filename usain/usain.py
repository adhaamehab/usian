# -*- coding: utf-8 -*-
from loguru import logger
import threading

from schedule import Scheduler
import datetime
import time


"""Main module."""


class Task:

    def __init__(self, name, pipe, init_data=None,):
        self.name = name
        self.status = 'stopped'
        self._init_data = init_data
        self._pipeline = pipe

    def __str__(self):

        return 'Task: {name} is {status}'.format(
            name=self.name,
            status=self.status,
        )

    def _run(self):
        if self._init_data is None:
            logger.info('Running pipeline for task {} without intial data'.format(self.name))
            logger.debug("Task {} running at node 1 out of {}".format(self.name, len(self._pipeline)))
            res = self._pipeline[0]()
        else:
            logger.info('Running pipeline for task {} with intial data'.format(self.name))
            logger.debug("Task {} running at node 1 out of {}".format(self.name, len(self._pipeline)))
            res = self._pipeline[0](self._init_data)
        for idx, fn in enumerate(self._pipeline[1:]):
            logger.debug("Task {} running at node {} out of {}".format(self.name, idx + 2, len(self._pipeline)))
            res = fn(res)

    def run(self):
        """
        Run the pipeline on the data
        """
        job_thread = threading.Thread(target=self._run)
        job_thread.start()



class Runner(Scheduler):
    """Tasks runner
    """

    def __init__(self, name='Global Runner'):
        self.name = name
        self.status = 'stopped'
        super().__init__()

    def _run_job(self, job):
        try:
            logger.info("")
            super()._run_job(job)
        except Exception as e:
            logger.error(e)
            job.last_run = datetime.datetime.now()
            job._schedule_next_run()

    def add(self, task, seconds):
        """Add task to task list"""
        if seconds == 1:
            self.every(seconds).second.do(task.run)
        else:
            self.every(seconds).seconds.do(task.run)


    def run(self):
        while True:
            super().run_pending()
            time.sleep(1)


