# HOW TO SETUP

Run ```cd ~``` (change to home directory)
Run ```git clone https://github.com/blue9057/cs6262-assignment```
Run ```cd cs6262-assignment```
Run ```./setup.py``` (run setup)

# HOW TO ANALYZE
1. After the setup, you can find ```complex.exe``` at ```~/shared/complex.exe```. You can access this file in the VM through the shared directory (on the Desktop of the VM).

2. Edit the code in ```~/tools/sym-exec/symbolic-executor.py``` to analyze ```complex.exe``` to find the command that the malware can interpret (and in upper case).

3. You can edit ```~/tools/c2-command/complex-command.txt``` to test your command against ```complex.exe```.

4. Fill answers in the ```~/report/complex-questionnaire.txt```

5. Submit your results to T-Square: 1) symbolic-executor.py and 2) complex-questionnaire.txt
