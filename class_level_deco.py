import time
import dateutil

def decorator(cls):
    def wrapper(*args,**kwargs):
        for i in cls.__dict__:
            start  = time.time()
            if i.startswith('__'):
                continue
            (eval(i))()
            # end = time.time()
            # x = end-time
            # print(x)
    return wrapper


@decorator
class Mlass:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def method(self):
        self.x + self.y

    def method2(self):
        self.x**self.y

obj=Mlass()

#
# library(stringr)
# library(stringi)
#
# #1
# var <- "The Gurus is a fast-growing company assembling highly qualified professionals in the industry."
#
# #2
# word(var,3)
#
# #3
# variable <-"GURUS"
# if (grepl(tolower(variable),tolower(var))){
#   cat("Yes")
# } else {
#   cat("No")
# }
#
# #4
# print(str_replace(var,"industry","field"))
#
# #5
#
# words <- strsplit(var, " ")[[1]]
# selected_words <- words[c(1, 2, 3, 4,5, 6)]
# print(paste(c(1,2,3,4,"well known", selected_words), collapse = ", "))
#
# #6
# var1 <- "180.5kg"
# substring <- substr(var1,0,5)
# var2 <- as.numeric(substring)
# cat(class(var2))
# cat(var2)
#
# #7
# date <- as.Date("2020-12-11")
# date <- date+5
# cat(as.character(date))















