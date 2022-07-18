# Intro to Reverse Engineering 1
This WriteUp describes the approach to solve the challenge `intro-rev-1`

# Tools
The tools you need to solve are dependent on the plattform you use. In General we need the following tools:
 - PE-Analyzer<br> To checkout what kind of Application we have (used Compiler, Packed, obfuscated)
   - Linux
     - file
   - Windows
     - [ExeInfo by ASL](https://github.com/ExeinfoASL/ASL)
     - [CFF Explorer](https://ntcore.com/?page_id=388) - see `Identifier` Function
 - Decompiler<br> If we deal with a programming language which utilize Just-in-Time Compilation
   - Linux
     - VScode with IlSpy extension
     - [AvalonSpy](https://github.com/icsharpcode/AvaloniaILSpy)
   - Windows
     - VScode with IlSpy extension
     - [dnSpyEx](https://github.com/dnSpyEx/dnSpy) - contains an integrated debugger
 - a Debugger/Disassembler <br> If we deal with a programming language which use Ahead-of-time-compilation or we can't find a good decompiler
   - Linux
     - GDB
     - [Binary Ninja](https://binary.ninja/)
     - [Ghidra](https://ghidra-sre.org/)
   - Windows
     - [x64dbg](https://github.com/x64dbg/x64dbg)
     - [Binary Ninja](https://binary.ninja/)
     - [Ghidra](https://ghidra-sre.org/)

# Analyzing the File

## Linux
Within Linux we could checkout the file via command `file`
```
> file rev01.dll
rev01.dll: PE32 executable (console) Intel 80386 Mono/.Net assembly, for MS Windows
```

## Windows
We drag and drop the `rev01.dll` in ExeInfo and we get the result:

`[ Linker 48 ] - MS Visual C# / Basic.NET  ]  - EP Token : 06000008`

If you load the binary with `CFF Explorer` you need to use the identifier function and scan the binary.

# Checking out the Code

As we see, we deal with an Mono/.Net assembly. .Net is using a Just-in-time compilation approach. This means the program will be first compiled in an intermediate language (IL). If you execute the binary the IL-Code will be on the fly (just-in-time) compiled and translated into assembly code.
Due to this approach it is possible to read out the IL-Code and translate it back into readably .Net-Code. 

To decompile the IL-Code we will use the vscode-extension IlSpy. With `Strg + Shift + P`, using the option `IlSpy: Pick assembly from file system` and loading our target file `rev01.dll`.

The following Structure is shown in IlSpy:
 - Name of the binary
   - namespace
     - Classes
       - Function

For our Binary it should look like this:
 - rev01 (1.0.0.0, .NETCoreApp, v6.0)
   - {}
     - \<Module>
     - Program
     - \<PrivateImplementationDetails>

If we want to analyze a specific class, we only need to double click on the class and we get the decompiled code based on the IL-Code:

```C# 
#Program-Class:
/* 1*/ using System;
/* 2*/ using System.Runtime.CompilerServices;
/* 3*/ 
/* 4*/ [CompilerGenerated]
/* 5*/ internal class Program
/* 6*/ {
/* 7*/ 	private static void <Main>$(string[] args)
/* 8*/ 	{
/* 9*/ 		char[] array = new char[6] { 'y', 'l', 'l', 'a', 'e', 'r' };
/*10*/  		string text = "Welcome to your 1st Reverse-Engineering Challenge. Take a Decompiler of your choice and check out the source code. :)";
/*11*/  		Console.WriteLine(text);
/*12*/  		Array.Reverse(array);
/*13*/  		string text2 = text.Split(' ')[8] + "s_are_" + new string(array);
/*14*/  		Console.WriteLine("Please Provide the secret Message: ");
/*15*/  		string text3 = Console.ReadLine();
/*16*/  		text = "_powerfull!";
/*17*/  		if (text3 == text2 + text)
/*18*/  		{
/*19*/  			Console.WriteLine("That Is correct!");
/*20*/  			Console.WriteLine("The Flag is CSCG{" + text2 + text + "}");
/*21*/  		}
/*22*/  		else
/*23*/  		{
/*24*/  			Console.WriteLine("Oh no, false flag :(");
/*25*/  		}
/*26*/  	}
/*27*/  }
```

# Solution
After receiving the decompiled code, we can check statically the code. We could also take the code and try to reimplement the program.

In Summary the programm does the following things:
 - create an array `{ 'y', 'l', 'l', 'a', 'e', 'r' }`
 - setting a text Message: `Welcome to your 1st Reverse-Engineering Challenge. Take a Decompiler of your choice and check out the source code. :)`
 - print out this Message in the Console
 - Reverse the array so it looks now like this: `{ 'r', 'e', 'a', 'l', 'l', 'y', }`
 - concatinate strings and save them in text2
   - first string is the 9th word of the text Message `Decompiler`
   - second string is `s_are_`
   - third string is the array converted into a string: `really`
   - which means we have now the following value: `Decompilers_are_really`
 - text3 is set to whatever the user is typing in and confirm with Enter
 - The text Message is overwritten with `_powerfull!`
 - Now we getting to the check if the user input equals text2 and text (`Decompilers_are_really_powerfull!`)
   - if that is true, the following message is printed: `That Is correct! The Flag is CSCG{Decompilers_are_really_powerfull!}`
   - if we provided the wrong input we get the following message in the console: `Oh no, false flag :(`

# Comparison Decompiled Code & Original Source Code

It is good to know that there are differences between decompiled code and the original code.

The Decompiler translates the IL-Code and if it sees that variables are set, these variables will be set by the decompiler (see `text`,`text2`,`text3`). In the original source code these are (`msg`, `hiddenmsg`, `flag_data`).
Sure the original source code would be with these variables a little bit better to read, but sometimes the decompiled code has also an advantage. In our case the example where the message gets overwritten by `_powerfull!`

Original Code:
```C#
msg = "\x5F\x70\x6F\x77\x65\x72\x66\x75\x6C\x6C\x21";
```

Decompiled Code:
```C#
text = "_powerfull!";
```