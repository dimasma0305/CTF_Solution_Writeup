Source: https://hackmethod.com/overthewire-narnia-0/?v=b718adec73e0
# OverTheWire – Narnia 0

by [hellor00t](https://hackmethod.com/author/scott/?v=b718adec73e0 "Posts by hellor00t") | Jan 25, 2016 | [hacking](https://hackmethod.com/category/hacking/?v=b718adec73e0), [tutorials](https://hackmethod.com/category/tutorials/?v=b718adec73e0)

[Introduction](https://hackmethod.com/overthewire-narnia-0/?v=b718adec73e0#introduction) [Source Code vs Executable Code](https://hackmethod.com/overthewire-narnia-0/?v=b718adec73e0#sourcevsexecutable) [Narnia Level 0 – Source Code](https://hackmethod.com/overthewire-narnia-0/?v=b718adec73e0#narniasourcecode) [Narnia Level 0 – Exploitation](https://hackmethod.com/overthewire-narnia-0/?v=b718adec73e0#narniaexploitation) [Narnia Level 0 – Solution](https://hackmethod.com/overthewire-narnia-0/?v=b718adec73e0#narniasolution)

#### **Introduction**

This is an introduction to reverse engineering. I will be going through a series of reverse engineering puzzles developed by OverTheWire and explaining the methodology I used to solve these puzzles.

In the challenges that are provided, you are given an executable and the source code to a program. The goal is to figure out a way to exploit or PWN the executable. Exploitation in this context typically refers to overwriting system memory to achieve some unintended outcome. Lets first talk about the files that are give to you.

#### **Source Code vs Executable Code**

Source code is the original language that a program is written in. Source code is then compiled into a set of instructions that the computer processor can execute. This translation from source code to executable code must happen, because computer processors do not understand source code, but they do understand the machine instructions inside executable code. Lets take a look at the difference

![HelloWorld.c](https://i0.wp.com/www.hackmethod.com/wp-content/uploads/2016/01/HelloWorld.c.jpg?resize=424%2C147&ssl=1)    Figure 1. Example C Source Code

[![HelloWorld.obj](https://i0.wp.com/www.hackmethod.com/wp-content/uploads/2016/01/HelloWorld.obj_.jpg?resize=629%2C230&ssl=1)](https://i0.wp.com/www.hackmethod.com/wp-content/uploads/2016/01/HelloWorld.obj_.jpg?ssl=1)Figure 2. Example C Executable Code

As you can see from the examples above, even for a small “Hello World!” program, machine instructions are not easy to read, which is why high level source code exists in the first place. High level programming languages such as C, C++ and Java, are easier to understand and are human readable. Even without being a programmer, you can probably determine that the source code in figure 1 prints the text “Hello World” to the screen.

Unfortunately for the reverse engineer, most compiled programs do not come with the source code that was used to generate them. This is done for a couple of reasons, first, the source code is not needed for a program to run, the only thing a computer needs is the compiled object code, therefore shipping a program without the source code makes it smaller. Second, people who sell their programs for a profit, don’t want you to see how they created the program, or else anyone could steal the code and compile it for themselves without paying. 

# **Narnia Level 0 – Source Code**

Lets get started…

First we must ssh into the game server using the following credentials:

**Server**: narnia.labs.overthewrite.org **Username**: narnia0 **Password**: narnia0

The **/narnia** folder holds all of the challanges for each level, but our current permissions level only allows us access to the level 0 files, which are: **narnia0** and **narnia0.c** . What are these two files? The first one is the compiled program and the second one is the source code.

Lets first look at the source code

[![Narnia0Source1](https://i0.wp.com/www.hackmethod.com/wp-content/uploads/2016/01/Narnia0Source1-1.jpg?resize=676%2C74&ssl=1)](https://i0.wp.com/www.hackmethod.com/wp-content/uploads/2016/01/Narnia0Source1-1.jpg?ssl=1)

Here we see two variables being created, **val** is initialized to the hex value _0x41414141_ and **buf** is an array that is not initialized to any value, but space has been reserved for 20 1-byte values. The “char” data type in C is defined as 1-byte in length, therefore char **buf[20]** reserves 20 consecutive 1-byte memory locations. 

[![Narnia0Source2](https://i0.wp.com/www.hackmethod.com/wp-content/uploads/2016/01/Narnia0Source2.jpg?resize=690%2C41&ssl=1)](https://i0.wp.com/www.hackmethod.com/wp-content/uploads/2016/01/Narnia0Source2.jpg?ssl=1)These are the instructions that tell you what your trying to accomplish. The variable **val**, has been initialized to the value _0x41414141_, the program wants you to somehow change it to the value _0xdeadbeef_.

[![Narnia0Source3](https://i0.wp.com/www.hackmethod.com/wp-content/uploads/2016/01/Narnia0Source3.jpg?resize=683%2C22&ssl=1)](https://i0.wp.com/www.hackmethod.com/wp-content/uploads/2016/01/Narnia0Source3.jpg?ssl=1)

 The scanf function is used for user input. The %24s means that the function will accept a 24 byte character string (1 char = 1 byte) and store that into the **buf** variable, but if you remember **buf** was only allocated 20 bytes of memory. This is how we’re going to exploit the program, more on this later.

[![Narnia0Source4](https://i0.wp.com/www.hackmethod.com/wp-content/uploads/2016/01/Narnia0Source4.jpg?resize=684%2C60&ssl=1)](https://i0.wp.com/www.hackmethod.com/wp-content/uploads/2016/01/Narnia0Source4.jpg?ssl=1)These two lines help you see what values were actually stored in **buf** and **val** after **scanf()**received user input.

[![Narnia0Source5](https://i0.wp.com/www.hackmethod.com/wp-content/uploads/2016/01/Narnia0Source5.jpg?resize=696%2C121&ssl=1)](https://i0.wp.com/www.hackmethod.com/wp-content/uploads/2016/01/Narnia0Source5.jpg?ssl=1)If you correctly overwrite **va**l’s memory location to hold _0xdeadbeef_, then this branching statement gives you a shell (command prompt). Otherwise, it prints “_WAY OFF!!!!”_ and then exits. Don’t despair, it doesn’t matter how close you are, it will always print this statement if it is incorrect.

# **Narnia Level 0 – Exploitation**

As I stated before, we will need to take advantage of

**scanf()** in order to exploit this program, but to understand how, we first need to understand how programs get mapped into system memory.

Every program gets mapped into memory and uses a data structure known as “the stack” to store information such as variables, arguments and what instruction to execute next. It make sense to store these variables on the stack so that they can be easily and quickly retrieved as the program runs. Here is a graphical representation of what the stack looks like. [![](https://i0.wp.com/1.bp.blogspot.com/-XskvavAYEiI/VqUQ-0mamuI/AAAAAAAANe8/02h_THxKh7I/s640/stack%2Bexample%2B4.JPG?resize=640%2C334)](https://i0.wp.com/1.bp.blogspot.com/-XskvavAYEiI/VqUQ-0mamuI/AAAAAAAANe8/02h_THxKh7I/s1600/stack%2Bexample%2B4.JPG)

Notice the arrow pointing from high memory to low memory, this is because the stack grows towards the lower memory locations. That means that if a programs defines three variables in the following order… int x= 10 int y = 20 int z = 30 …then they will be stored on the stack as such. 

[![](https://i0.wp.com/3.bp.blogspot.com/-pEY9SqVYqAc/VqURMeSmJcI/AAAAAAAANfI/Jfy0azrzkXI/s640/stack%2Bexample%2B5.JPG?resize=640%2C330)](https://i0.wp.com/3.bp.blogspot.com/-pEY9SqVYqAc/VqURMeSmJcI/AAAAAAAANfI/Jfy0azrzkXI/s1600/stack%2Bexample%2B5.JPG)

In order to exploit **narnia0**, this is all the information that we need to know. Other details about the stack such as the return address and old EBP (base pointer) will be explained in detail as we progress through the other levels. Lets see how the the **narnia0** program looks on the stack.[![](https://i0.wp.com/1.bp.blogspot.com/-1tD-5mJfctw/VqUH87fSZHI/AAAAAAAANeU/crb-bIGpem8/s640/stack%2Bexample%2B2.JPG?resize=640%2C362&ssl=1)](https://i0.wp.com/1.bp.blogspot.com/-1tD-5mJfctw/VqUH87fSZHI/AAAAAAAANeU/crb-bIGpem8/s1600/stack%2Bexample%2B2.JPG)

Since the stack grows from high memory to low memory, **val** is stored at a higher memory address than **buf**, because **val** was declared first in the program. Notice that the main program does not take any arguments on the command line, so those memory locations on the stack have been grey out (in reality they don’t even exist), and since this challenge only require us to manipulate **buf** and **val**, I’ve also grayed out Old EBP and Return Address, again we’ll discuss the purpose of these during future levels. How are we going to change **val** on the stack, so that it reads _0xdeadbeef_? Remember the **scanf()** function that reads in 24 bytes of data? For the visual learners, here’s how that looks in memory. [![](https://i0.wp.com/www.hackmethod.com/wp-content/uploads/2016/01/NarniaStackFrame.jpg?resize=594%2C681&ssl=1)](https://i0.wp.com/www.hackmethod.com/wp-content/uploads/2016/01/NarniaStackFrame.jpg?ssl=1)

Each square in the illustration above represents 1-byte. **val** is of type long and long is defined as being 8-bytes. Again, we see that **scanf()** is set to take in 24-bytes of input and store them in the memory location of **buf**. The **scanf()** function does not check or care how big the destination location is; therefore, by filling up the **scanf()** buffer, we can overwrite the adjacent memory location of **val**.

# **Narnia Level 0 – Solution**

Armed with the knowledge above, you may be temped (as I was) to try and solve the puzzle. **Attempt 1:**

[![NarniaAttemp1](https://i0.wp.com/www.hackmethod.com/wp-content/uploads/2016/01/NarniaAttemp1-1.jpg?resize=540%2C137&ssl=1)](https://i0.wp.com/www.hackmethod.com/wp-content/uploads/2016/01/NarniaAttemp1-1.jpg?ssl=1)

Although this did not work, important information can be gleaned from our failure. The first thing to notice is that value 0x64616564 is no where close to 0xdeadbeef. The answer to why lies on the second line that says “Correct val’s value from 0x4141414141 to 0xdeadbeef”. The 0x portion means that it wants the value of val to be in hex, but instead we passed it ASCII. The second thing to notice is that 0x64616564 is the ASCII equivalent of daed (or dead backwards). The reason our input was displayed backwards is because most x86 architectures store data in little-endian format when it is pushed onto the stack. This means that the least significant byte (far right value) gets stored in the lowest memory location, for example, if we set **val** to _Hello_, it would be stored in memory like this…[![](https://i0.wp.com/2.bp.blogspot.com/-I2l_k31qqI0/VqVEWB06_4I/AAAAAAAANf4/NK0LpvBpbmc/s640/little-endian.JPG?resize=640%2C168)](https://i0.wp.com/2.bp.blogspot.com/-I2l_k31qqI0/VqVEWB06_4I/AAAAAAAANf4/NK0LpvBpbmc/s1600/little-endian.JPG)

Using this information lets try again. **Attempt 2:**[![NarniaAttemp2](https://i0.wp.com/www.hackmethod.com/wp-content/uploads/2016/01/NarniaAttemp2.jpg?resize=806%2C161&ssl=1)](https://i0.wp.com/www.hackmethod.com/wp-content/uploads/2016/01/NarniaAttemp2.jpg?ssl=1)

First we need to figure out how to get hex into our ASCII input. The BASH shell has the ability to represent hex using the _\x_ escape sequence, but in order for echo to parse escape sequence we have to add the -e option. Since hex values outside the ASCII range contain non-printable characters that are not easily copied and pasted, we are going to pipe the output directly to the program. This has the affect of storing our custom string into a buffer and waiting for scanf() to read it. Success? Sort of. The program didn’t yell at us and the **val** has been overwritten to the correct value, but the program closes immediately without allowing us to use our newly acquired privileges. **Attempt 3:** SUCCESS!

[![NarniaAttemp3](https://i0.wp.com/www.hackmethod.com/wp-content/uploads/2016/01/NarniaAttemp3.jpg?resize=865%2C213&ssl=1)](https://i0.wp.com/www.hackmethod.com/wp-content/uploads/2016/01/NarniaAttemp3.jpg?ssl=1)

If you create a command group _( command 1 ; command 2; )_ and pipe the result to your program, each command is provided as a separate input to the program. The first input is our custom string which gets fed to the **scanf()** function. After the program executes **system(“/bin/sh”)** we are given a command shell, by passing cat to the command shell as a the second input, it keeps the command shell open, we are free to run any commands under the new elevated permissions. (I have scoured the internet high and low to figure out how and why that last part works, but have yet to find a solid answer).

That wasn’t so difficult, was it? Pretty simple tbh. If you’re interested and want to keep going, check out Narnia Level 1 using the button below.