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
