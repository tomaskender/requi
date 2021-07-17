# REQUI

Requi is a tool used to check for formal and behavioral requirements of submitted school projects.  
  
Formal checks include checking file structure in folders, names of files, the type and compression type of archive and other things that differ from subject to subject and can be a cause for loss of points for submitted projects.
  
Behavioral requirements check for expected return codes and outputs for different sets of provided arguments to the evaluated program.  

## Launching the tool

`python3 requi.py --rule example-rule.requi --project xlogin.zip`

## Writing rules

You can define specifications for expected format and behavior of projects using rule files. These rule files are written in YAML format and follow a specific file format that you can find in "*example-rule.requi*".  

As of right now, you can launch external console commands supported by your operating system and set the expected return code and output.

### Supported actions
* `custom`  
Launches a console command specified in `action-cmd` and compares it's return code to `action-code` and it's output to `action-output`. Not specifying code or output means that the value won't be checked.

```
name: "a custom command"
action: custom
action-cmd: "cd example-folder && make all"
action-code: 0
action-output: "gcc -c -o main.o main.c -I.\ngcc -o main main.o\n"
```

* `check-files`  
Checks if working directory contains files with attributes specified in `action-formal-rule`.

```
name: "a rule to check file structure"
action: check-files
action-formal-rule:
    -
        name: example-folder
        type: folder
    -
        name: example-folder/main.c
        type: file
    -
        name: example-folder/Makefile
        type: file
    -
        name: example-folder/README.md
        type: file
    -
        name: 'xlogin00.tar.gz'
        type: file
        archive:
            format: tar
            compression: off
            max-size: 5MB
```