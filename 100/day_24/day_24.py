# 1. modifying the snake game keep track of highscore
# - achieved by writing the highscore into a file and reading from it when running the application next time.

# reading from file
with open("test.txt") as file:
    contents = file.read()
    print(contents)

# file.close()

# why close the file?
# resouces spent on opening
# resouces are freed by closing
# can omit if using 'with-as' syntax

# if the file you are 'writing' to doesn't exit
# python will create it for you
with open("test.txt", mode = 'a') as file:
    file.write("New text.")