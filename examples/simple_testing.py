import asyncio

from huputs import TestThingsOut

lets = TestThingsOut()


@lets.inject
def my_print_fn(s: str):
    print(s)


@lets.inject
async def test1_fn(s: str):
    await asyncio.sleep(0.1)
    my_print_fn(s)
    return


@lets.add_test("Test 1").for_fn(test1_fn)
async def test1():
    global my_print_fn
    my_print_fn = lets.override(my_print_fn).makeItDoNothing()
    my_print_fn = lets.inject(my_print_fn)
    await test1_fn("works!")
    lets.make_sure(test1_fn).ran_with_exactly("works!")
    # the line below should raise TestError
    lets.make_sure(my_print_fn).ran_with_exactly("does not work!")


lets.do_this()
