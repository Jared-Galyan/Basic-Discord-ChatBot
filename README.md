# Basic-Discord-ChatBot

This is a more up to date and a bit faster version of the ChattyCathy bot that I have recoded. 

# Support Server

https://discord.gg/C2FJ8jF

# Installing

Download the files for the bot. 

Requirements:
- Python 3.6 or higher
- pip install aiml
- Most up to date version of discord.py

Once you have the files and the requirements you need to create a file called `std-startup.xml` in that file insert the following and save it.
```
<aiml version="1.0.1" encoding="UTF-8">
    <!-- std-startup.xml -->

    <!-- Category is an atomic AIML unit -->
    <category>

        <!-- Pattern to match in user input -->
        <!-- If user enters "LOAD AIML B" -->
        <pattern>LOAD AIML B</pattern>

        <!-- Template is the response to the pattern -->
        <!-- This learn an aiml file -->
        <template>
            <learn>./aiml/*/*</learn>
            <!-- All aiml files are relative to the run dir and must be subdirs,
                 E.g. ./aiml/alice/one.aiml, ./aiml/custom/mine.aiml -->

        </template>

    </category>

</aiml>
```
Once that is complete go into the `bot.py` and change the `token` AND `channel_name` to your own things. After you have changed that simply start the bot with `python bot.py` or however your version of python allows you to execute files.
