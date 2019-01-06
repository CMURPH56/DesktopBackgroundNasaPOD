# Update Background With Nasa Image of the Day #

## Get Api Key ##

1. Go to https://api.nasa.gov/index.html , and fill out the short web form to get your api key.
2. Update the code with your api key

## Setup Windows Task Sheduler ##

a.
1. Type Task Scheduler into Windows Search
2. Click the create task button on the right handside tool bar. 
3. Give it any name you want
4. Change the configuration for Windows 10
5. Choose to run when user is logged on

b.
1. Click the actions tab
2. Click New 
3. In the Program/script: box enter where you have python installed.
    get this by running python -c "import sys; print(sys.executable") in the command line
4. For the arguments give the name of the file i.e. Set_Desktop.py
5. For the Start in give the name of the directory where the file is located.
    i.e. c:\users\your_name\documents\
6. Click the triggers tab choosing the daily option with whatever time is fine
    I am not sure when nasa updates the photo
7. Ok out of all the windows and select the task and click run to ensure that everything is correct

c.
1. Choose the your desktop background to be the space.jpg that the program creates.
